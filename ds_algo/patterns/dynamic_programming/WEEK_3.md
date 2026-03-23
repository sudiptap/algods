# Week 3: LIS + State Machine DP + Palindromic DP

> Target companies: Google, Microsoft, NVIDIA | Timeline: 2-3 weeks out
> You have 646 DP solutions. This week is about **instant pattern recognition**, not grinding new problems.

---

## Day 1-2: Longest Increasing Subsequence (LIS) Pattern

### Pattern Recognition

| If you see...                                      | Think LIS                        |
| -------------------------------------------------- | -------------------------------- |
| "longest increasing/decreasing" anything            | Classic LIS                     |
| Sequence of pairs/tuples that must nest or chain    | Sort + LIS on one dimension     |
| "minimum removals to make sorted/monotone"          | `n - LIS_length`                |
| 2D nesting (envelopes, boxes, dolls)                | Sort dim1 asc, dim2 desc → LIS  |
| "longest chain" of items where `a < b`              | Sort by end → greedy or LIS     |
| Word ladder / string chain by single char changes   | Sort by length → LIS variant    |

### The Core Technique

**O(n^2) DP — must know, easy to derive:**
```
dp[i] = length of LIS ending at index i
dp[i] = 1 + max(dp[j] for j < i if nums[j] < nums[i])
Answer = max(dp)
```

**O(n log n) with patience sorting — Google EXPECTS this:**
```python
import bisect

def lengthOfLIS(nums):
    tails = []  # tails[i] = smallest tail element for IS of length i+1
    for x in nums:
        pos = bisect.bisect_left(tails, x)
        if pos == len(tails):
            tails.append(x)
        else:
            tails[pos] = x  # replace with smaller tail
    return len(tails)
```
- `tails` is always sorted — that is the invariant.
- `bisect_left` for strictly increasing; `bisect_right` for non-decreasing.
- `tails` is NOT the actual LIS. It only gives the length. To reconstruct, track parent pointers.

**Base case:** every element alone is an IS of length 1.

**Key optimization:** the O(n log n) version replaces a full inner loop with a binary search on the `tails` array.

### Problems

| #    | Name                                       | Diff   | Aha hint                                                                 |
| ---- | ------------------------------------------ | ------ | ------------------------------------------------------------------------ |
| 300  | Longest Increasing Subsequence             | Medium | Textbook. Code both O(n^2) and O(n log n). bisect_left = strict.        |
| 673  | Number of Longest Increasing Subsequence   | Medium | Two arrays: `length[i]` AND `count[i]`. When equal length found, ADD counts, don't replace. |
| 646  | Maximum Length of Pair Chain                | Medium | Sort by second element. Greedy (interval scheduling) is O(n log n). LIS on pairs also works. |
| 1048 | Longest String Chain                       | Medium | Sort by word length. For each word, try removing each char → check if predecessor exists in set. HashMap DP. |
| 354  | Russian Doll Envelopes                     | Hard   | Sort by width ASC, then height DESC (kills same-width cheating). LIS on heights only. |
| 1671 | Min Removals for Mountain Array            | Hard   | Compute LIS from left (`left[i]`) and LIS from right (`right[i]`). Mountain peak at i: `left[i] + right[i] - 1`. Answer = `n - max_mountain`. Both sides must be >= 2. |
| 1626 | Best Team With No Conflicts                | Hard   | Sort by (age, score). Now it reduces to LIS on scores (since ages are non-decreasing). dp[i] = max total score ending at player i. |

### Variations to Watch For

- **Non-decreasing vs strictly increasing:** `bisect_left` vs `bisect_right`. Off-by-one here fails interviews.
- **2D LIS (envelopes):** the "sort dim2 descending" trick is the entire problem. Without it, same-width envelopes stack illegally.
- **LIS reconstruction:** interviewers sometimes ask "print the actual subsequence." Track a `parent[]` array alongside `tails` indices.
- **Counting LIS (673):** can't use O(n log n) naively — need segment tree or BIT for O(n log n) counting.
- **"Minimum operations to make X"** often means `n - LIS` in disguise.

### Common Mistakes

1. Using `bisect_right` when the problem says "strictly increasing" (need `bisect_left`).
2. Forgetting the height-descending sort trick in 354. Without it, `[3,3], [3,4]` both get picked.
3. In 673, resetting `count[i] = count[j]` instead of `count[i] += count[j]` when lengths are equal.
4. In 1671, not checking that both left and right LIS lengths are >= 2 at a peak (a mountain needs both sides).
5. Returning `tails` as the LIS — it is NOT the actual subsequence, only its length is correct.

---

## Day 3-4: State Machine DP

### Pattern Recognition

| If you see...                                         | Think State Machine DP           |
| ----------------------------------------------------- | -------------------------------- |
| "buy/sell stock" with constraints                      | Classic state machine            |
| Cooldown periods between actions                       | Add a "cooldown/rest" state      |
| "at most k transactions"                               | k layers of (hold, cash) states  |
| Counting sequences with adjacency constraints          | States = last element, transitions = allowed next |
| "consecutive" limits (lates, absences, etc.)           | State tracks streak count        |
| Flip/convert string with monotonicity constraint       | States = what the last char was  |

### The Core Technique

**Step 1: DRAW THE STATE DIAGRAM.** This is non-negotiable.

Every state machine DP has:
- **States** (nodes): what situation am I in right now?
- **Transitions** (edges): what actions move me between states?
- **Recurrence**: for each state, take the best incoming transition.

**General stock template (covers 121, 122, 123, 188, 309, 714):**
```python
# Two fundamental states: HOLD (have stock), CASH (no stock)
# On day i:
hold[i] = max(hold[i-1],        # do nothing
              cash[i-?] - price) # buy (? depends on cooldown)
cash[i] = max(cash[i-1],        # do nothing
              hold[i-1] + price - fee)  # sell (fee if applicable)
```

**For k transactions (problems 123, 188):**
```python
# hold[k][i] = best profit holding stock, having done at most k buys
# cash[k][i] = best profit not holding, having done at most k sells
for t in range(1, k+1):
    hold[t] = max(hold[t], cash[t-1] - price)
    cash[t] = max(cash[t], hold[t] + price)
```
Space-optimize: you only need previous day, so drop the `i` dimension.

**Base cases:**
- `hold = -infinity` (can't hold stock before buying)
- `cash = 0` (start with no stock, no profit)

### Problems

| #    | Name                                    | Diff   | Aha hint                                                                 |
| ---- | --------------------------------------- | ------ | ------------------------------------------------------------------------ |
| 121  | Best Time to Buy and Sell Stock         | Easy   | One pass: track `min_price`, answer = `max(price - min_price)`. This IS a 1-txn state machine simplified. |
| 122  | Best Time to Buy and Sell Stock II      | Medium | Unlimited txns. Sum all `price[i] - price[i-1]` where positive. Or: hold/cash states, no txn limit. |
| 309  | Best Time with Cooldown                 | Medium | 3 states: `hold`, `sold` (just sold, must rest next), `rest`. `hold[i] = max(hold[i-1], rest[i-1] - price)`. |
| 714  | Best Time with Transaction Fee          | Medium | Same as 122 but subtract fee on sell: `cash[i] = max(cash[i-1], hold[i-1] + price - fee)`. |
| 123  | Best Time to Buy and Sell Stock III     | Hard   | 4 variables: `buy1, sell1, buy2, sell2`. Process left-to-right, each builds on previous. |
| 188  | Best Time to Buy and Sell Stock IV      | Hard   | Generalize 123 to k. When `k >= n//2`, it degenerates to problem 122 (unlimited). Handle that edge case or TLE. |
| 552  | Student Attendance Record II            | Hard   | State = `(total_absences, consecutive_lates)`. 3 choices each day: P/A/L. Transitions: P resets lates, A increments absences + resets lates, L increments lates. Use matrix exponentiation for O(log n). |
| 1220 | Count Vowels Permutation                | Hard   | 5 states (a,e,i,o,u). Given transition rules, build adjacency. `dp[vowel] = sum(dp[predecessors])`. Matrix exponentiation for large n. |
| 926  | Flip String to Monotone Increasing      | Medium | State: `last_is_0` or `last_is_1`. Process each char: if original is 0, `last_is_1` pays a flip cost. Track min cost for each state. |

### The Stock Problem Decision Tree

```
Is it one transaction?
  └─ YES → 121: track min, compute max diff

Is it unlimited transactions?
  ├─ No cooldown, no fee → 122: sum positive diffs
  ├─ With cooldown → 309: add "rest" state
  └─ With fee → 714: subtract fee on sell

Is it at most k transactions?
  ├─ k = 2 → 123: 4 variables
  └─ k general → 188: array of states, degenerate check
```

### Variations to Watch For

- **Matrix exponentiation:** problems 552 and 1220 have large n. The state transitions are linear, so represent as matrix multiply. Goes from O(n * S) to O(S^3 * log n).
- **Non-stock state machines:** 1220 (vowels), 552 (attendance), 926 (flipping). Same framework: define states, draw transitions, code recurrence.
- **"Profit" vs "count" objectives:** stocks maximize profit, 552/1220 count valid sequences. Same structure, different aggregation (max vs sum).

### Common Mistakes

1. Forgetting `hold` starts at `-infinity`, not `0`. Starting at 0 means you "sold stock you never bought."
2. In 309 (cooldown), buying from `cash[i-1]` instead of `rest[i-1]`. The cooldown means you can only buy after resting.
3. In 188, not handling `k >= n//2` as unlimited. Without this, you allocate O(k) arrays where k can be 10^9.
4. In 123, updating `buy2` using the OLD `sell1` vs the just-updated `sell1`. Process in order: `buy1 → sell1 → buy2 → sell2` and it works because each uses the "best so far."
5. In 552, confusing "total absences" (global) with "consecutive lates" (resets). They are independent state dimensions.

---

## Day 5-6: Palindromic DP

### Pattern Recognition

| If you see...                                          | Think Palindromic DP              |
| ------------------------------------------------------ | --------------------------------- |
| "palindromic substring" — contiguous                    | Expand around center OR dp[i][j]  |
| "palindromic subsequence" — non-contiguous              | dp[i][j] on substrings, or LCS trick |
| "minimum insertions/deletions to make palindrome"       | `len - LPS` (longest palindromic subsequence) |
| "palindrome partitioning"                               | Precompute isPalin[][], then partition DP |
| "remove at most k chars to make palindrome"             | LPS >= len - k                    |
| "count palindromic subsequences"                        | Interval DP with inclusion-exclusion |

### The Core Technique

**Two distinct sub-patterns:**

**A. Palindromic Substrings (contiguous) — expand around center:**
```python
def countSubstrings(s):
    count = 0
    for center in range(2 * len(s) - 1):
        left = center // 2
        right = left + center % 2
        while left >= 0 and right < len(s) and s[left] == s[right]:
            count += 1
            left -= 1
            right += 1
    return count
```
O(n^2) time, O(1) space. Handles both odd and even length palindromes.

**B. Palindromic Subsequence (non-contiguous) — interval DP:**
```python
# dp[i][j] = length of longest palindromic subsequence in s[i..j]
if s[i] == s[j]:
    dp[i][j] = dp[i+1][j-1] + 2
else:
    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
```
Base case: `dp[i][i] = 1` (single char is a palindrome).
Fill order: by increasing length `j - i`.

**The LCS reduction (critical insight for 516):**
```
LPS(s) = LCS(s, reverse(s))
```
This means you can solve 516 with your existing LCS code. Interviewers love asking "can you reduce this to a known problem?"

**Base cases:**
- Single character: palindrome of length 1.
- Two characters: palindrome of length 2 if equal, else 1.

### Problems

| #    | Name                                          | Diff   | Aha hint                                                                |
| ---- | --------------------------------------------- | ------ | ----------------------------------------------------------------------- |
| 647  | Palindromic Substrings                        | Medium | Expand around center. 2n-1 centers (n odd + n-1 even). Count expansions. |
| 5    | Longest Palindromic Substring                 | Medium | Same expand technique as 647, but track max length + start index.       |
| 516  | Longest Palindromic Subsequence               | Medium | Interval DP or `LCS(s, rev(s))`. Both O(n^2). LCS version is less code. |
| 131  | Palindrome Partitioning                       | Medium | Backtracking. Precompute `isPalin[i][j]` to avoid recomputing. Return all partitions. |
| 132  | Palindrome Partitioning II                    | Hard   | `cuts[i]` = min cuts for `s[0..i]`. Precompute isPalin. `cuts[i] = min(cuts[j-1] + 1)` for all valid `j` where `s[j..i]` is palindrome. |
| 1312 | Min Insertion Steps to Make Palindrome        | Hard   | `answer = len(s) - LPS(s)`. The chars NOT in the LPS each need one insertion to mirror. |
| 1216 | Valid Palindrome III                          | Hard   | Can remove at most k chars → is `LPS(s) >= len(s) - k`? Compute LPS, one comparison. |
| 730  | Count Different Palindromic Subsequences      | Hard   | Interval DP with 4 chars (a,b,c,d). For each char, find first/last occurrence in range. Inclusion-exclusion to avoid double-counting. |

### The Palindromic DP Decision Tree

```
Is it about substrings (contiguous)?
  └─ YES → Expand around center (647, 5)

Is it about subsequences (non-contiguous)?
  ├─ Longest? → 516: interval DP or LCS(s, rev(s))
  ├─ Min insertions? → 1312: len - LPS
  ├─ Remove ≤ k? → 1216: LPS ≥ len - k
  └─ Count distinct? → 730: interval DP + char-based tracking

Is it about partitioning into palindromes?
  ├─ All partitions? → 131: backtrack + isPalin cache
  └─ Min cuts? → 132: DP on cuts + precomputed isPalin
```

### Variations to Watch For

- **Manacher's algorithm:** O(n) for longest palindromic substring. Rarely asked to code it, but knowing it exists shows depth. If interviewer asks "can you do better than O(n^2)?" — mention it.
- **1312 and 1216 are the same core problem** (LPS), just different wrapping questions. Recognize this instantly.
- **730 (counting) is significantly harder** than 516 (longest). The counting version needs careful dedup: "aba" contains "a" palindrome twice positionally, but we count it once as a distinct string.
- **Palindrome partitioning variants:** some ask for min cuts (132), some ask to enumerate all (131). Very different algorithms despite similar names.

### Common Mistakes

1. In expand-around-center, forgetting even-length palindromes. You need 2n-1 centers, not n.
2. In interval DP, filling in wrong order. You MUST fill by increasing interval length (gap = j - i), not row by row.
3. In 132, recomputing `isPalin` inside the cuts DP loop. Precompute it in a separate O(n^2) pass first.
4. Confusing substring (contiguous) and subsequence (non-contiguous) in the problem statement. Read carefully — they need completely different approaches.
5. In 1312, trying to build the palindrome explicitly. You don't need to — just compute `len - LPS`.

---

## Day 7: Review & Drill

### Timed Drills (simulate interview pressure)

| Drill | Target Time | What to Do |
| ----- | ----------- | ---------- |
| Code O(n log n) LIS | 5 min | From blank file. No references. Must include `bisect_left`. |
| Solve 309 (Cooldown) | 10 min | Draw 3-state diagram first (hold/sold/rest). Then code from diagram only. |
| Solve 516 two ways | 15 min | First: direct interval DP. Second: LCS(s, rev(s)). Compare. |
| Explain 354 sort trick | 2 min | Verbally explain why height must be sorted descending for same width. |
| Solve 132 from scratch | 15 min | Precompute isPalin, then cuts DP. Watch the fill order. |

### Cross-Pattern Connections

| Connection | Why it matters |
| ---------- | -------------- |
| LIS + Sorting | Almost every LIS variant starts with a sort. The sort transforms the problem into a 1D LIS. |
| State Machine + Greedy | Stock problem 122 (unlimited) can be solved greedily. Recognize when state machine simplifies to greedy. |
| Palindromic Subsequence = LCS | `LPS(s) = LCS(s, rev(s))` bridges Week 3 back to LCS from earlier study. |
| LIS + Palindromic | 1671 (mountain array) uses LIS from both directions — similar bidirectional thinking to palindrome expand-around-center. |

### Final Checklist Before Moving On

- [ ] Can code O(n log n) LIS in under 5 minutes, cold
- [ ] Know when to use `bisect_left` vs `bisect_right`
- [ ] Can draw stock state diagrams for 309, 714, 123, 188 from memory
- [ ] Know the `k >= n//2` degeneration trick for problem 188
- [ ] Can derive `min_insertions = len - LPS` without looking it up
- [ ] Can solve interval DP palindrome problems in correct fill order
- [ ] Can explain the LCS reduction for palindromic subsequence

---

**Week 3 velocity target:** 0 new problems. 100% pattern lock-in. If you see any of these in an interview, recognition should be instant and code should flow from the pattern, not from memory of a specific solution.
