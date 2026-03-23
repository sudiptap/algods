# Week 4: Final Prep Sprint (Condensed Cherry-Pick)

> **Goal:** Cover remaining high-value DP patterns with minimum viable problem count.
> You already know: Fibonacci, Grid, Kadane's, LCS, Knapsack, LIS, State Machine, Palindromic.
> This week: Linear/Scheduling, Range/MCM, Tree DP, Game Theory, Prefix/Suffix, Bitmask.

---

## Day 1: Linear DP — Scheduling & Jump Games

### Pattern Recognition
- "Can I break this string/sequence into valid parts?" -> Word Break style
- "Schedule non-overlapping intervals to maximize profit" -> Sort by end + bisect
- "Minimum cost to reach the end with constraints on jumps" -> Sliding window / deque DP

### Core Template
```python
# Job Scheduling template (sort by end, bisect for last non-overlap)
jobs.sort(key=lambda x: x[1])  # sort by end time
dp[i] = max(dp[i-1],  # skip job i
            profit[i] + dp[last_non_overlapping])  # take job i

# Word Break template
dp[i] = any(dp[j] and s[j:i] in wordSet for j in range(i))

# Jump Game with deque (sliding window max)
dq = deque()  # stores indices, dp[dq[0]] is max in window
for i in range(n):
    dp[i] = nums[i] + dp[dq[0]]
    while dq and dp[dq[-1]] <= dp[i]: dq.pop()
    dq.append(i)
    if dq[0] <= i - k: dq.popleft()
```

### Problems

| # | Problem | Difficulty | Hint |
|---|---------|-----------|------|
| 139 | Word Break | Medium | `dp[i] = True` if any `dp[j]` and `s[j:i]` in set; check all splits |
| 1235 | Max Profit in Job Scheduling | Hard | Sort by end, `bisect_right` to find last compatible job, `dp[i] = max(skip, take)` |
| 887 | Super Egg Drop | Hard | Binary search on `dp[k][m]` = max floors checkable with k eggs, m moves |
| 1696 | Jump Game VI | Medium | `dp[i] = nums[i] + max(dp[i-k..i-1])`, use monotonic deque for O(n) |

### If you only remember one thing
> **Job Scheduling is THE linear DP pattern for interviews:** sort by end time, binary search for the last non-overlapping job, `dp[i] = max(dp[i-1], profit[i] + dp[j])`. This solves a huge family of interval scheduling problems.

---

## Day 2: Range DP / Matrix Chain Multiplication

### Pattern Recognition
- "Merge/split elements and cost depends on what's adjacent" -> Range DP
- "Partition into groups where cost depends on the group" -> MCM
- The key insight is always: **think about the LAST operation**, not the first

### Core Template
```python
# Range DP: iterate by length, then start, then split point
for length in range(2, n + 1):
    for i in range(n - length + 1):
        j = i + length - 1
        for k in range(i, j):
            dp[i][j] = min(dp[i][j],
                           dp[i][k] + dp[k+1][j] + cost(i, j, k))
```

### Problems

| # | Problem | Difficulty | Hint |
|---|---------|-----------|------|
| 312 | Burst Balloons | Hard | Think "last balloon to burst in range [i,j]" — `dp[i][j] = max(dp[i][k] + dp[k][j] + nums[i]*nums[k]*nums[j])` |
| 1039 | Min Score Triangulation | Medium | Classic MCM: pick root of triangle `k` in `[i,j]`, cost = `v[i]*v[k]*v[j] + dp[i][k] + dp[k][j]` |
| 1547 | Min Cost to Cut a Stick | Hard | Sort cuts, add endpoints, `dp[i][j]` = min cost to process cuts between `cuts[i]` and `cuts[j]`, cost = `cuts[j]-cuts[i]` |

### If you only remember one thing
> **Always think about the LAST operation in the range.** In Burst Balloons, k is the last balloon burst (so left/right subarrays are independent). This "last to act" framing is what makes range DP ranges independent.

---

## Day 3: Tree DP

### Pattern Recognition
- "Optimal value for a tree where parent/child choices interact" -> Post-order DFS returning tuples
- "Sum of distances / contributions across all nodes" -> Rerooting DP (two passes)
- "Minimum set of nodes to cover/dominate tree" -> Multi-state DP at each node

### Core Template
```python
# Return-tuple pattern (House Robber III)
def dfs(node):
    if not node: return (0, 0)  # (rob_this, skip_this)
    l, r = dfs(node.left), dfs(node.right)
    rob = node.val + l[1] + r[1]       # rob me, must skip children
    skip = max(l) + max(r)              # skip me, children free to choose
    return (rob, skip)

# Rerooting DP (Sum of Distances in Tree)
# Pass 1: root at 0, compute count[v], dist_sum[0]
# Pass 2: for child v of parent u:
#   ans[v] = ans[u] - count[v] + (n - count[v])
#   (moving root to v: count[v] nodes get 1 closer, n-count[v] get 1 farther)
```

### Problems

| # | Problem | Difficulty | Hint |
|---|---------|-----------|------|
| 337 | House Robber III | Medium | DFS returns `(rob, skip)` per node; rob = val + children's skip; skip = max of each child |
| 124 | Binary Tree Max Path Sum | Hard | DFS returns max single-branch gain; update `global_max` with `left + right + node.val` at each node |
| 968 | Binary Tree Cameras | Hard | 3 states per node: 0=needs cover, 1=has camera, 2=covered. Greedy post-order: place camera at parent of leaf |
| 834 | Sum of Distances in Tree | Hard | Two-pass rerooting: `ans[child] = ans[parent] - count[child] + (n - count[child])` |

### If you only remember one thing
> **Tree DP = post-order DFS returning a tuple of states.** The tuple captures "what does the parent need to know about this subtree?" For House Robber it's (rob, skip). For cameras it's (needs_cover, has_camera, covered). This tuple-return pattern handles every tree DP.

---

## Day 4: Game Theory DP + Prefix/Suffix DP

### Pattern Recognition
- "Two players pick optimally from ends/piles" -> Minimax: `my_best = total - opponent_best`
- "Need left_max and right_max arrays" -> Prefix/suffix precomputation
- "Contribution of each element across all subarrays" -> Monotonic stack + contribution counting

### Core Template
```python
# Minimax (Predict the Winner)
# dp[i][j] = max score current player gets from nums[i..j]
dp[i][j] = max(nums[i] - dp[i+1][j],   # take left
               nums[j] - dp[i][j-1])    # take right
# positive means current player wins

# Trapping Rain Water
left_max[i]  = max(left_max[i-1], height[i])
right_max[i] = max(right_max[i+1], height[i])
water[i] = min(left_max[i], right_max[i]) - height[i]

# Sum of Subarray Minimums (contribution technique)
# For each element, find how many subarrays it's the minimum of:
# left[i] = distance to previous smaller element
# right[i] = distance to next smaller-or-equal element
# contribution of nums[i] = nums[i] * left[i] * right[i]
```

### Problems

| # | Problem | Difficulty | Hint |
|---|---------|-----------|------|
| 486 | Predict the Winner | Medium | `dp[i][j]` = net score advantage for current player in `nums[i..j]`; `max(nums[i]-dp[i+1][j], nums[j]-dp[i][j-1])` |
| 877 | Stone Game | Medium | Same minimax DP as 486; note Alice always wins with even piles (but know the DP proof) |
| 42 | Trapping Rain Water | Hard | `water[i] = min(left_max[i], right_max[i]) - height[i]`; two-pointer version also works |
| 907 | Sum of Subarray Minimums | Medium | Monotonic stack to find PLE/NLE; contribution = `val * left_count * right_count` |

### If you only remember one thing
> **Minimax trick: `my_best = total - opponent_best`.** Instead of tracking two players, track the *advantage* of the current player. `dp[i][j] = max(take_left - dp[i+1][j], take_right - dp[i][j-1])`. Whoever's turn it is, they maximize; the subtraction handles the opponent automatically.

---

## Day 5: Bitmask DP (Google Loves This)

### Pattern Recognition
- N is small (N <= 20) and you need to track "which items are used" -> Bitmask
- "Assign N items to N slots with constraints" -> Permutation bitmask
- "Partition into subsets with constraints" -> Iterate over submasks
- If you see N <= 15-20 in constraints, **think bitmask immediately**

### Core Template
```python
# Permutation bitmask (Beautiful Arrangement)
# dp[mask] = number of valid arrangements using the set of items in mask
for mask in range(1 << n):
    pos = bin(mask).count('1')  # next position to fill
    for i in range(n):
        if not (mask & (1 << i)) and valid(pos+1, i+1):
            dp[mask | (1 << i)] += dp[mask]

# Subset cover (Smallest Sufficient Team)
# dp[mask] = smallest team achieving skill-set mask
for person, skills in enumerate(people):
    person_mask = encode(skills)
    for prev_mask in range(1 << m):
        new_mask = prev_mask | person_mask
        dp[new_mask] = min(dp[new_mask], dp[prev_mask] + [person])
```

### Problems

| # | Problem | Difficulty | Hint |
|---|---------|-----------|------|
| 526 | Beautiful Arrangement | Medium | `dp[mask]` = ways to fill positions 1..popcount(mask) with items in mask; check divisibility |
| 698 | Partition to K Equal Sum Subsets | Medium | Target = sum/k; `dp[mask]` = can items in mask be partitioned; track running sum mod target |
| 1125 | Smallest Sufficient Team | Hard | Skills as bitmask; `dp[skill_mask]` = min team; for each person, `dp[old | person_skills] = min(dp[old] + person)` |

### If you only remember one thing
> **Bitmask DP: `dp[mask]` where mask encodes "which items have been used/covered."** The position or next decision is often implicit from `popcount(mask)`. When N <= 20, this is almost always the intended approach. Google asks this pattern regularly.

---

## Days 6-7: Mock Interview & Weak Spot Patching

### Mock Interview Protocol
1. **Pick 2 problems randomly** from the repo that you haven't solved this week
2. **Set a 30-minute timer per problem** — if stuck at 15 min, write brute force then optimize
3. **Talk out loud** the entire time (Google heavily weights communication)
4. **After solving**, write the time/space complexity without looking it up

### Weak Spot Audit
- Which pattern took you longest this week? Do 1 more from that pattern.
- Which recurrence did you have to look up? Rewrite it from memory.
- Can you explain Range DP's "last operation" insight in 30 seconds? Practice it.

### Interview Day Cheat Sheet (mental checklist)
```
1. Clarify: input size, edge cases, sorted?, duplicates?
2. Brute force first -> optimize
3. State what DP means: "dp[i] represents..."
4. Recurrence in words before code
5. Base cases (don't forget them)
6. Time & space complexity
7. Can space be optimized? (1D instead of 2D?)
```

---

## Quick Reference: All Week 4 Patterns

| Pattern | Key Signal | Core Idea | Complexity |
|---------|-----------|-----------|------------|
| Linear/Scheduling | Non-overlapping intervals | Sort by end + bisect | O(n log n) |
| Range DP / MCM | Merge/split with adjacency cost | Last operation in range | O(n^3) |
| Tree DP | Optimal choices on tree nodes | Post-order DFS, return tuple | O(n) |
| Game Theory | Two players, optimal play | my_score = total - opponent | O(n^2) |
| Prefix/Suffix | Need left/right extremes | Precompute from both ends | O(n) |
| Bitmask DP | N <= 20, track used items | dp[mask], iterate subsets | O(2^n * n) |

---

*You've covered 8 patterns in Weeks 1-3 and 6 more this week. That's 14 DP patterns total. You're ready. Trust your prep and ship it.*
