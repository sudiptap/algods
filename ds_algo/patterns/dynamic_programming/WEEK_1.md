# Week 1: Fibonacci + Grid DP + Kadane's Pattern

Target: Google, Microsoft, NVIDIA interviews in 2-3 weeks.
Goal: Pattern recognition speed. See a problem, identify the pattern in under 2 minutes.

---

## Day 1-2: Fibonacci Pattern

### Pattern Recognition

You're looking at a Fibonacci-style DP when:

1. The current state depends on **only the previous 1-2 states** (constant lookback window).
2. The problem asks "how many ways" or "min/max cost" to reach step N.
3. There's an implicit **linear sequence** where each element has a small fixed number of predecessors.
4. You can reduce the problem to "take or skip" at each position (House Robber structure).
5. The transition graph has **fixed fan-in** — each state receives contributions from a known, small set of prior states.

### The Core Technique

**State definition:** `dp[i]` = answer (count / min cost / max profit) considering elements `0..i`.

**Recurrence template:**
```python
# Counting variant (Climbing Stairs)
dp[i] = dp[i-1] + dp[i-2]

# Optimization variant (House Robber)
dp[i] = max(dp[i-1], dp[i-2] + val[i])

# Cost variant (Min Cost Climbing Stairs)
dp[i] = val[i] + min(dp[i-1], dp[i-2])
```

**Base cases:** `dp[0]` and `dp[1]` always need explicit values. Get these wrong and everything is wrong.

**Space optimization:** You only need `prev` and `prev_prev`. Always optimize to O(1) space in interviews — it signals maturity.

### Problems

| # | Problem | Diff | Aha Insight |
|---|---------|------|-------------|
| 509 | Fibonacci Number | Easy | Pure definition — use as your dp[i] = dp[i-1] + dp[i-2] warmup. |
| 70 | Climbing Stairs | Easy | "Ways to reach step n" IS Fibonacci — dp[n] = dp[n-1] + dp[n-2]. |
| 746 | Min Cost Climbing Stairs | Easy | Pay cost[i] when you step on i; dp[i] = cost[i] + min(dp[i-1], dp[i-2]). |
| 198 | House Robber | Med | At each house: rob it (skip prev) or don't — dp[i] = max(dp[i-1], dp[i-2] + nums[i]). |
| 213 | House Robber II | Med | Circle = two linear runs: solve for nums[0..n-2] and nums[1..n-1], take the max. |
| 91 | Decode Ways | Med | Like climbing stairs but some steps are invalid — '0' can't stand alone, only follows '1' or '2'. |
| 740 | Delete and Earn | Med | Earning value v deletes v-1 and v+1 — bucket by value, then it's literally House Robber on the value array. |
| 935 | Knight Dialer | Med | Fib-like but on a graph — precompute which digits reach which, then dp[step][digit] = sum of predecessors. |
| 790 | Domino and Tromino Tiling | Med | dp[n] = 2*dp[n-1] + dp[n-3]; or derive via matrix exponentiation for O(log n). |

### Variations to Watch For

- **Circular arrays** (213): Split into two linear subproblems. Interviewers love this twist.
- **Invalid states** (91): The recurrence is standard but certain transitions are forbidden. You must handle '0' and leading zeros carefully.
- **Reduce-to-Robber** (740): The problem doesn't look like Fibonacci at all until you transform the input. If "choosing X eliminates nearby X", think House Robber.
- **Multi-state Fibonacci** (935, 790): The transition isn't just i-1 and i-2 but a fixed graph of predecessors. Same idea, wider fan-in.
- **Modular arithmetic**: Knight Dialer and Tiling need `% (10^9+7)`. Apply mod at every addition, not just at the end.

### Common Mistakes

- **Off-by-one on base cases.** For Climbing Stairs: dp[0]=1, dp[1]=1. For Min Cost: you can start at index 0 or 1 — the answer is min(dp[n-1], dp[n-2]), not dp[n].
- **Decode Ways '0' handling.** `"10"` is valid (J), `"01"` is not. If s[i]=='0' and s[i-1] not in {'1','2'}, return 0 immediately.
- **House Robber II: forgetting the single-element case.** When n=1, just return nums[0]. The two-run logic assumes n >= 3.
- **Not reducing to O(1) space.** For Fibonacci-style, if you leave an O(n) array, the interviewer will ask you to optimize. Just do it upfront.

---

## Day 3-4: Grid DP

### Pattern Recognition

You're looking at Grid DP when:

1. Input is a **2D matrix/grid** and you need to traverse from one corner to another (or find an optimal substructure within the grid).
2. Movement is **restricted to specific directions** (right/down, or down/down-left/down-right).
3. Each cell contributes a cost/value and you want **min/max/count** of paths.
4. The answer at cell (i,j) depends on a **small fixed neighborhood** of already-computed cells.
5. The problem involves finding an **optimal rectangular or square sub-region**.

### The Core Technique

**State definition:** `dp[i][j]` = answer considering the subproblem ending at cell (i,j).

**Recurrence templates:**
```python
# Path counting (Unique Paths)
dp[i][j] = dp[i-1][j] + dp[i][j-1]

# Path optimization (Min Path Sum)
dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])

# Square detection (Maximal Square)
dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1  # if grid[i][j] == 1

# Falling path (3 directions)
dp[i][j] = grid[i][j] + min(dp[i-1][j-1], dp[i-1][j], dp[i-1][j+1])
```

**Base cases:** First row and first column are typically initialized directly from the grid. For path counting, dp[0][j]=1 and dp[i][0]=1 (one way to reach any cell in the first row/col).

**Space optimization:** Process row by row, keep only the previous row. For Maximal Square you need prev row + one extra variable for the diagonal.

### Problems

| # | Problem | Diff | Aha Insight |
|---|---------|------|-------------|
| 62 | Unique Paths | Med | Pure combinatorics: C(m+n-2, m-1). DP is dp[i][j] = up + left. |
| 63 | Unique Paths II | Med | Same as 62 but set dp[i][j] = 0 wherever there's an obstacle. |
| 64 | Minimum Path Sum | Med | dp[i][j] = grid[i][j] + min(dp from top, dp from left). In-place works. |
| 120 | Triangle | Med | Bottom-up avoids boundary hassle: dp[j] = tri[i][j] + min(dp[j], dp[j+1]). |
| 931 | Min Falling Path Sum | Med | Three predecessors per cell (up-left, up, up-right). Watch column boundaries. |
| 221 | Maximal Square | Med | dp[i][j] = min(left, top, diagonal) + 1. Answer is max(dp[i][j])^2. |
| 1277 | Count Square Submatrices | Med | Exact same recurrence as 221, but answer = sum of all dp[i][j] values. |
| 85 | Maximal Rectangle | Hard | Build histogram heights row by row, then solve Largest Rectangle in Histogram per row using a stack. |
| 174 | Dungeon Game | Hard | Forward DP fails (can't optimize health and path simultaneously). Go **backward** from (m-1,n-1) to (0,0). dp[i][j] = min health needed to survive from (i,j). |
| 329 | Longest Increasing Path | Hard | Not standard grid DP — use DFS + memo. The strictly-increasing constraint provides a topological order, so no visited array needed. |

### Variations to Watch For

- **Reverse DP** (174): When you can't determine the answer going forward because future states affect current decisions, reverse the direction. Dungeon Game is the classic example.
- **Histogram reduction** (85): 2D rectangle problems often reduce to a 1D histogram problem applied row by row. Know Largest Rectangle in Histogram (84) cold.
- **DFS + memo on grids** (329): When movement isn't restricted to right/down but depends on cell values, standard grid DP doesn't work. Use memoized DFS with all 4 directions.
- **In-place modification**: For 62, 63, 64 — you can often use the input grid itself as your dp table. Mention this as a space optimization.
- **Obstacles and blocked cells** (63): Always check: what if the start or end cell is blocked? Return 0 immediately.

### Common Mistakes

- **Dungeon Game: trying forward DP.** You can't greedily minimize cost forward because you don't know the minimum health threshold until you've seen the whole path. You MUST go backward.
- **Maximal Square: returning dp value instead of dp^2.** dp[i][j] stores the side length, not the area.
- **Forgetting to clamp at 1 in Dungeon Game.** dp[i][j] = max(1, min(dp[i+1][j], dp[i][j+1]) - dungeon[i][j]). Health can never drop below 1.
- **Triangle: using top-down and fighting index bounds.** Bottom-up on Triangle is cleaner — start from the second-to-last row, collapse upward.
- **329: using a visited set.** You don't need one. The strictly-increasing constraint means you can never revisit a cell in the same DFS path. Adding a visited set is wasted work and can actually cause bugs.

---

## Day 5-6: Kadane's Pattern

### Pattern Recognition

You're looking at a Kadane's-style DP when:

1. You need the **optimal contiguous subarray** (max sum, max product, max length with a property).
2. At each index, the decision is: **extend the current subarray or start fresh**.
3. The problem involves a **1D array** and the answer is some aggregate over a contiguous window.
4. There's a constraint that modifies classic Kadane's (one deletion allowed, circular array, product instead of sum).
5. You need to track **auxiliary state** alongside the running value (min product, no-delete vs one-delete).

### The Core Technique

**State definition:** `dp[i]` = optimal answer for a subarray **ending at index i** (not just "considering" — ending at).

**Recurrence template:**
```python
# Classic Kadane's (Max Subarray)
dp[i] = max(nums[i], dp[i-1] + nums[i])
answer = max(dp)

# Product variant — track both min and max
max_dp[i] = max(nums[i], max_dp[i-1]*nums[i], min_dp[i-1]*nums[i])
min_dp[i] = min(nums[i], max_dp[i-1]*nums[i], min_dp[i-1]*nums[i])

# With one deletion
no_del[i] = max(nums[i], no_del[i-1] + nums[i])
one_del[i] = max(no_del[i-1], one_del[i-1] + nums[i])  # delete nums[i], or keep extending after a prior deletion
```

**Base cases:** `dp[0] = nums[0]`. For product: `max_dp[0] = min_dp[0] = nums[0]`.

**Space:** Always O(1) — you only need the previous values.

### Problems

| # | Problem | Diff | Aha Insight |
|---|---------|------|-------------|
| 53 | Maximum Subarray | Med | The original Kadane's: extend or restart. dp[i] = max(nums[i], dp[i-1]+nums[i]). |
| 152 | Max Product Subarray | Med | Negative * negative = positive. Track running min AND max; swap on negative. |
| 918 | Max Sum Circular Subarray | Med | Answer = max(standard Kadane, totalSum - minSubarraySum). Edge case: if all negative, answer is just the max element. |
| 1186 | Max Subarray Sum w/ One Deletion | Med | Two parallel dp arrays: `no_del[i]` and `one_del[i]`. one_del can either delete current element or extend a previous deletion. |
| 1567 | Max Len Positive Product | Med | Track `pos_len` and `neg_len` at each index. When nums[i]<0, swap them. When nums[i]==0, reset both. |
| 2272 | Substring Largest Variance | Hard | For every pair (a, b): run Kadane's treating a as +1, b as -1, others as 0. Must have at least one b — track whether b has appeared. |
| 689 | Max Sum of 3 Non-Overlapping Subarrays | Hard | Precompute window sums, then for each middle window position, pick best left window (prefix max) and best right window (suffix max). |

### Variations to Watch For

- **Product vs Sum** (152): Negatives make product Kadane's tricky. Always carry both min and max forward. A single negative flips min to max.
- **Circular arrays** (918): The maximum circular subarray is totalSum - minSubarray. But if ALL elements are negative, minSubarray = totalSum and you'd get 0, which is wrong. Handle this edge case explicitly.
- **Deletion/skip budget** (1186): Add a second DP dimension for "how many deletions used." This generalizes: k deletions = k+1 parallel DP arrays.
- **Character-pair Kadane's** (2272): Variance = freq(a) - freq(b). This is Kadane's on a transformed array. The trick is iterating all 26*25 pairs and requiring at least one occurrence of b.
- **Fixed-width windows** (689): Not classic Kadane's but related. Precompute prefix sums, then sweep with left-best and right-best arrays.

### Common Mistakes

- **918: returning 0 when all elements are negative.** When totalSum == minSubarray, the circular case gives 0 (empty subarray, which is invalid). Fall back to standard Kadane's result.
- **152: not handling zeros.** Zero resets both min and max product to zero. This is correct behavior, but make sure your initialization handles it.
- **2272: forgetting the "must include at least one b" constraint.** Without it, you'd just count all a's. Track a boolean `has_b` and only update the answer when it's true.
- **1186: confusing the two states.** `one_del[i]` is NOT "delete element i." It's "best subarray ending at position i having used one deletion somewhere in the subarray." The deletion could have been earlier.
- **689: not returning indices when asked.** The problem asks for starting indices of the three subarrays, not just the sum. Track argmax, not just max.

---

## Day 7: Timed Review

Re-solve these three from scratch. No peeking. 20 minutes each.

| Problem | Why This One | What to Verify |
|---------|-------------|----------------|
| 198 House Robber | Foundation of Fibonacci DP. If this isn't instant, the rest won't stick. | O(1) space, clean base cases, under 5 min. |
| 174 Dungeon Game | Tests reverse-DP thinking. Most candidates get this wrong in interviews. | Did you go backward? Did you clamp at 1? |
| 918 Max Sum Circular | Tests Kadane's + edge case handling. The all-negative trap catches many. | Did you handle the all-negative case? Can you explain why totalSum - minSubarray works? |

**Scoring yourself:**
- Solved in < 10 min with no bugs: pattern is locked in.
- Solved in 10-20 min with minor bugs: review the specific mistake, do one more pass tomorrow.
- Couldn't solve or > 20 min: re-read the pattern section, solve 2 more problems from that category.

---

## Quick Reference Card

| Pattern | State | Recurrence | Space |
|---------|-------|-----------|-------|
| Fibonacci | dp[i] = answer at step i | dp[i] = f(dp[i-1], dp[i-2]) | O(1) |
| Grid DP | dp[i][j] = answer at cell (i,j) | dp[i][j] = f(neighbors) + grid[i][j] | O(n) with row compression |
| Kadane's | dp[i] = best ending at i | dp[i] = max(nums[i], dp[i-1] + nums[i]) | O(1) |

**The universal question at each index:** "Do I extend the previous substructure, or do I start fresh here?"
