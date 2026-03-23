# Week 2: LCS + Unbounded Knapsack + 0/1 Knapsack

> **Goal**: Pattern recognition on sight. You should identify the pattern within 30 seconds of reading a problem, then write the recurrence from memory.

---

## Day 1-2: Longest Common Subsequence (LCS) Pattern

### Pattern Recognition

If you see any of these, think LCS / 2D string DP:

1. **Two strings (or sequences) compared element-by-element** — classic LCS setup
2. **"Minimum operations to convert X to Y"** — edit distance variant
3. **"How many ways to match/align two sequences"** — count-paths on the 2D grid
4. **Subsequence matching with ordering constraints** — if relative order matters but not contiguity, it is LCS
5. **Interleaving or merging two sequences into a third** — dp[i][j] over prefixes of both inputs

### The Core Technique

**State**: `dp[i][j]` = answer considering `s1[0..i-1]` and `s2[0..j-1]`

**Base cases**: `dp[0][j] = 0` and `dp[i][0] = 0` (empty prefix matches nothing)

**Recurrence (standard LCS)**:
```python
if s1[i-1] == s2[j-1]:
    dp[i][j] = dp[i-1][j-1] + 1
else:
    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
```

**Space optimization**: Only need previous row. Use `dp[2][n+1]` or a single 1D array with a `prev` variable for the diagonal.

```python
# 1D space-optimized LCS
prev_row = [0] * (n + 1)
for i in range(1, m + 1):
    prev = 0  # this is dp[i-1][j-1] before update
    for j in range(1, n + 1):
        temp = prev_row[j]
        if s1[i-1] == s2[j-1]:
            prev_row[j] = prev + 1
        else:
            prev_row[j] = max(prev_row[j], prev_row[j-1])
        prev = temp
```

### Problems

| # | Problem | Diff | Aha Insight |
|---|---------|------|-------------|
| 1143 | Longest Common Subsequence | Med | Pure template — match adds 1, mismatch takes max of skip-either |
| 583 | Delete Operation for Two Strings | Med | `ans = m + n - 2 * LCS(s1, s2)` — just find LCS length |
| 712 | Min ASCII Delete Sum | Med | Same grid but add ASCII costs instead of counting; minimize cost of skipped chars |
| 1035 | Uncrossed Lines | Med | It IS LCS — drawing non-crossing lines between matching elements is exactly LCS |
| 72 | Edit Distance | Med | Three operations map to three neighbors: `dp[i-1][j]+1`, `dp[i][j-1]+1`, `dp[i-1][j-1]+(0 or 1)` |
| 97 | Interleaving String | Med | `dp[i][j]` = can `s1[:i]` + `s2[:j]` form `s3[:i+j]`; check which string contributed `s3[i+j-1]` |
| 115 | Distinct Subsequences | Hard | Match: `dp[i-1][j-1] + dp[i-1][j]` (use it AND skip it); no match: `dp[i-1][j]` only |
| 1092 | Shortest Common Supersequence | Hard | Build LCS table, then backtrack to reconstruct — emit unmatched chars + LCS chars |
| 10 | Regular Expression Matching | Hard | `'*'` means zero-or-more of prev char: `dp[i][j] = dp[i][j-2]` (zero) or `dp[i-1][j]` if match (more) |

### Variations to Watch For

- **Weighted LCS**: Instead of `+1` on match, add a cost/value (712).
- **Count paths instead of optimal value**: Changes `max` to `+` (115).
- **Reconstruct the actual sequence**: Backtrack through the DP table from `dp[m][n]` (1092).
- **3 operations instead of 2**: Edit distance adds replace; interviewers love asking "what if we add swap?"
- **Boolean DP on two strings**: Interleaving (97) — the value is true/false, not a count.

### Common Mistakes

- **Off-by-one on indices**: `dp[i][j]` corresponds to `s1[i-1]` and `s2[j-1]`. Mixing this up is the #1 bug.
- **Forgetting the diagonal in space optimization**: When updating `prev_row[j]`, you need the old `prev_row[j]` (which is `dp[i-1][j]`) before overwriting it. Save it in `prev`.
- **Edit Distance: forgetting replace is `dp[i-1][j-1] + 1`** not `dp[i-1][j-1]`. The `+0` only happens on exact match.
- **Distinct Subsequences overflow**: Values grow exponentially. In interviews mention this; in Python it is fine, in C++/Java use modular arithmetic.

---

## Day 3-4: Unbounded Knapsack

### Pattern Recognition

If you see any of these, think unbounded knapsack:

1. **"Unlimited supply" / items can be reused** — coins, stamps, rod cutting
2. **"Minimum number of X to reach target"** — min-cost knapsack (322)
3. **"Number of ways to make amount/target"** — counting knapsack (518)
4. **"Can use same item multiple times"** — explicitly stated or implied
5. **Items are abstract (squares, ticket durations) and obviously reusable**

### The Core Technique

**State**: `dp[j]` = answer for capacity/amount `j`

**Key rule**: Iterate capacity **LEFT to RIGHT** (small to large). This allows the same item to contribute multiple times in one pass.

**Recurrence (min-cost variant, Coin Change)**:
```python
dp = [float('inf')] * (amount + 1)
dp[0] = 0
for coin in coins:              # outer: items
    for j in range(coin, amount + 1):  # inner: LEFT to RIGHT
        dp[j] = min(dp[j], dp[j - coin] + 1)
```

**Recurrence (count-combinations variant, Coin Change II)**:
```python
dp = [0] * (amount + 1)
dp[0] = 1
for coin in coins:              # outer: items
    for j in range(coin, amount + 1):  # inner: LEFT to RIGHT
        dp[j] += dp[j - coin]
```

**Count-permutations variant (377)** — flip the loops:
```python
dp = [0] * (target + 1)
dp[0] = 1
for j in range(1, target + 1):        # outer: amount
    for num in nums:                   # inner: items
        if j >= num:
            dp[j] += dp[j - num]
```

> **Critical**: outer=items inner=amount gives **combinations** (each combo counted once). outer=amount inner=items gives **permutations** (order matters). This is a top interview question.

### Problems

| # | Problem | Diff | Aha Insight |
|---|---------|------|-------------|
| 322 | Coin Change | Med | THE template — `dp[j] = min(dp[j], dp[j-coin]+1)`, left-to-right, init `inf` |
| 518 | Coin Change II | Med | Count combos: outer=coins, inner=amount, `dp[j] += dp[j-coin]` |
| 279 | Perfect Squares | Med | Coins are `{1,4,9,16,...,sqrt(n)^2}` — same as 322 with generated coin set |
| 377 | Combination Sum IV | Med | Count **permutations** — flip loops: outer=target, inner=nums |
| 983 | Min Cost for Tickets | Med | `dp[i]` = min cost for days `1..i`; tickets are "coins" covering 1/7/30 day windows |
| 1155 | Dice Rolls with Target Sum | Med | `n` dice each with `f` faces — bounded repetition; iterate dice outer, sum inner |
| 1449 | Form Largest Integer | Hard | Knapsack on digit cost to maximize value; greedy comparison for digit string |

### Variations to Watch For

- **Permutations vs combinations**: The loop order question. Expect this in interviews.
- **Minimum cost vs count ways vs boolean feasibility**: Same skeleton, different merge operation (`min` vs `+` vs `or`).
- **Non-uniform item "sizes"**: Ticket problem (983) — items cover ranges, not single units.
- **Bounded repetition disguised as unbounded**: Dice (1155) — each die is one "round" with faces as choices.
- **Reconstruction**: "Which coins did you use?" — track choices in a separate array.

### Common Mistakes

- **Wrong loop direction**: Left-to-right is unbounded. Right-to-left is 0/1. Mixing them up gives wrong answers silently — hard to debug.
- **Initializing dp[0]**: For min-cost, `dp[0] = 0` (zero cost for zero amount). For counting, `dp[0] = 1` (one way to make zero). Getting this wrong zeros out everything.
- **Forgetting `inf` check**: In min-cost, before doing `dp[j-coin] + 1`, the subtracted state must be reachable. In Python `inf + 1 = inf` so it is fine, but in Java/C++ you need an explicit check.
- **377 vs 518 confusion**: Read the problem carefully. "How many combinations" = 518 (outer=coins). "How many ordered sequences" = 377 (outer=target). The word "combination" in 377's title is misleading.

---

## Day 5-6: 0/1 Knapsack

### Pattern Recognition

If you see any of these, think 0/1 knapsack:

1. **"Each item used at most once"** — partition, subset sum, assignment problems
2. **"Partition array into two groups"** — knapsack on `sum/2`
3. **"Assign +/- signs to elements"** — transform to subset sum (494)
4. **Boolean: "Is it possible to achieve X?"** — `dp[j] = dp[j] or dp[j - w[i]]`
5. **Two resource constraints** — 2D knapsack (474)

### The Core Technique

**State**: `dp[j]` = answer for capacity `j`

**Key rule**: Iterate capacity **RIGHT to LEFT** (large to small). This ensures each item is used at most once per round.

**Recurrence (boolean subset sum, 416)**:
```python
dp = [False] * (target + 1)
dp[0] = True
for num in nums:                          # outer: items
    for j in range(target, num - 1, -1):  # inner: RIGHT to LEFT
        dp[j] = dp[j] or dp[j - num]
```

**Recurrence (count ways, 494)**:
```python
dp = [0] * (target + 1)
dp[0] = 1
for num in nums:
    for j in range(target, num - 1, -1):
        dp[j] += dp[j - num]
```

**2D knapsack (474)**:
```python
dp = [[0] * (n1 + 1) for _ in range(m1 + 1)]
for zeros, ones in items:
    for i in range(m1, zeros - 1, -1):     # RIGHT to LEFT on both dims
        for j in range(n1, ones - 1, -1):
            dp[i][j] = max(dp[i][j], dp[i - zeros][j - ones] + 1)
```

### Problems

| # | Problem | Diff | Aha Insight |
|---|---------|------|-------------|
| 416 | Partition Equal Subset Sum | Med | Boolean knapsack — target is `sum/2`; if sum is odd, return False immediately |
| 494 | Target Sum | Med | Transform: positive subset sums to `(total + target) / 2` — then count subset sums |
| 474 | Ones and Zeroes | Med | Each string has a (zeros, ones) cost — 2D knapsack, iterate both dims right-to-left |
| 1049 | Last Stone Weight II | Med | Minimize `|S1 - S2|` = find largest subset sum <= `sum/2` — same as 416 |
| 879 | Profitable Schemes | Hard | 3D: `dp[members][profit]` per crime; cap profit at `minProfit` to limit state |
| 956 | Tallest Billboard | Hard | State = difference between two rod groups; `dp[diff]` = max sum of taller group |
| 805 | Split Array with Same Avg | Hard | Pick subset of size `k` with sum `= k * totalSum / n`; knapsack over size + sum |

### Variations to Watch For

- **Partition problems are knapsack in disguise**: 416, 1049 — always check if `sum` is even first.
- **Algebraic transformation to convert +/- to subset sum**: 494 — `P - N = target` and `P + N = total`, so `P = (total + target) / 2`. If not integer, answer is 0.
- **Multiple constraints**: 474 (2D), 879 (3D) — same right-to-left logic, just more dimensions.
- **Difference as state**: 956 — instead of tracking two groups separately, track their difference. Reduces from exponential to polynomial states.
- **Bounded quantities**: "You have `k` copies of item `i`" — binary decomposition or bounded knapsack trick.

### Common Mistakes

- **Left-to-right instead of right-to-left**: This is the single most common knapsack bug. You will count items multiple times and get unbounded-knapsack answers for a 0/1 problem.
- **Forgetting the early exit on odd sum** (416, 1049): If `total_sum % 2 != 0`, no valid partition exists.
- **494 transformation: not checking `(total + target) % 2 == 0`**: If the sum is odd, answer is 0. Also check `abs(target) <= total`.
- **879: not capping profit at minProfit**: The state `dp[j][k]` where `k > minProfit` is redundant — collapse all `k >= minProfit` into one bucket, otherwise you blow memory.

---

## The Critical Distinction: Unbounded vs 0/1

This is the single most important thing to internalize this week.

```
UNBOUNDED (items reusable)          0/1 (each item once)
─────────────────────────           ─────────────────────
for item in items:                  for item in items:
    for j in range(w, cap+1):          for j in range(cap, w-1, -1):
        dp[j] = ...                        dp[j] = ...
              ↑                                  ↑
        LEFT → RIGHT                      RIGHT → LEFT
```

**Why it works**:
- **Left-to-right**: When computing `dp[j]`, `dp[j - w]` has ALREADY been updated in this round. So the current item's effect is baked in — meaning we can pick it again. Unbounded.
- **Right-to-left**: When computing `dp[j]`, `dp[j - w]` has NOT been updated yet (it is still from the previous item's round). So the current item can only be picked once. 0/1.

**Drill**: Solve 322 (unbounded) and 416 (0/1) back-to-back. The only structural difference is the inner loop direction. Burn this into muscle memory.

---

## Day 7: Review Protocol

### Timed Drills

| Problem | Target Time | What You're Testing |
|---------|-------------|---------------------|
| 322 Coin Change | 8 min | Unbounded template from memory |
| 416 Partition Equal Subset Sum | 8 min | 0/1 template + early-exit check |
| 322 then 416 back-to-back | 12 min | Feel the loop direction difference in your hands |
| 72 Edit Distance | 15 min | 2D string DP under pressure — this WILL appear |
| 494 Target Sum | 10 min | Algebraic transformation speed |

### Self-Test Questions

1. You see "minimum number of X to reach Y, items reusable." What pattern? What loop direction?
   → Unbounded knapsack. Left-to-right.

2. You see "partition array into two subsets minimizing difference." What pattern? First check?
   → 0/1 knapsack on `sum/2`. Check if sum is even.

3. You see "two strings, minimum operations to transform." State definition?
   → `dp[i][j]` = min ops for `s1[0..i-1]` → `s2[0..j-1]`. Edit distance.

4. What changes between counting combinations vs permutations in unbounded knapsack?
   → Loop order. Combinations: outer=items, inner=amount. Permutations: outer=amount, inner=items.

5. In 0/1 knapsack with 1D array, why iterate right-to-left?
   → So `dp[j - w]` still holds the value from the previous item round, preventing reuse.

### Red Flags During Interview

- You are iterating left-to-right but the problem says "each element used once" → **STOP, reverse the loop**.
- You see two strings and start thinking about a 1D DP → **STOP, it is almost certainly 2D**.
- Your count-ways DP returns 0 for everything → **Check `dp[0]` initialization. It should be 1, not 0**.
- Edit Distance returns `m + n` for similar strings → **Check your match case. Match = `dp[i-1][j-1] + 0`, not `+ 1`**.

---

## Quick Reference Card

| Pattern | State | Direction | Init | Merge Op |
|---------|-------|-----------|------|----------|
| LCS | `dp[i][j]` over two prefixes | N/A (2D fill) | `dp[0][*] = dp[*][0] = 0` | `max` or `+` |
| Edit Distance | `dp[i][j]` = min ops | N/A (2D fill) | `dp[i][0]=i, dp[0][j]=j` | `min` of 3 neighbors |
| Unbounded (min) | `dp[j]` = min cost for `j` | Left → Right | `dp[0]=0`, rest `inf` | `min` |
| Unbounded (count) | `dp[j]` = ways to make `j` | Left → Right | `dp[0]=1`, rest `0` | `+` |
| 0/1 (boolean) | `dp[j]` = reachable? | Right → Left | `dp[0]=True` | `or` |
| 0/1 (count) | `dp[j]` = ways to make `j` | Right → Left | `dp[0]=1`, rest `0` | `+` |
| 0/1 (max value) | `dp[j]` = max value for cap `j` | Right → Left | `dp[0]=0` | `max` |
