# DP Weekly Study Plan — Problem-by-Problem Roadmap

Master DP patterns progressively. Each week builds on the last.
Within each pattern: **Easy → Medium → Hard**. Don't skip ahead until you can solve the current level without hints.

---

## Week 1 — Build DP Intuition (Fibonacci + Grid + Kadane's)

The goal this week is to internalize the DP thinking process: define state, write recurrence, handle base cases.

### Day 1-2: Fibonacci Pattern
| # | Problem | Difficulty | Focus |
|---|---------|-----------|-------|
| 509 | Fibonacci Number | Easy | Pure DP warmup, top-down vs bottom-up |
| 70 | Climbing Stairs | Easy | Same as fib but disguised — recognize the pattern |
| 746 | Min Cost Climbing Stairs | Easy | Add cost dimension to climbing stairs |
| 198 | House Robber | Medium | Non-adjacent selection — classic recurrence |
| 213 | House Robber II | Medium | Circular array trick (two passes) |
| 91 | Decode Ways | Medium | Tricky base cases, builds counting intuition |
| 740 | Delete and Earn | Medium | Reduce to House Robber — pattern recognition |

**Checkpoint:** Can you write the recurrence for a new Fibonacci-style problem in under 2 minutes?

### Day 3-4: Grid DP
| # | Problem | Difficulty | Focus |
|---|---------|-----------|-------|
| 62 | Unique Paths | Medium | 2D DP foundation, space optimization |
| 63 | Unique Paths II | Medium | Handle obstacles — modify base cases |
| 64 | Minimum Path Sum | Medium | Optimization on grid — min instead of count |
| 120 | Triangle | Medium | Variable-width grid, bottom-up is cleaner |
| 931 | Minimum Falling Path Sum | Medium | Reinforce grid DP with slight twist |
| 221 | Maximal Square | Medium | State = side length, not area |
| 174 | Dungeon Game | Hard | **Reverse DP** — must go bottom-right to top-left |

**Checkpoint:** Given a new grid problem, can you immediately decide: top-down or bottom-up? Row-by-row space optimization?

### Day 5-6: Kadane's Pattern
| # | Problem | Difficulty | Focus |
|---|---------|-----------|-------|
| 53 | Maximum Subarray | Medium | The classic — dp[i] = max(nums[i], dp[i-1]+nums[i]) |
| 152 | Maximum Product Subarray | Medium | Track both min and max (negatives flip) |
| 918 | Maximum Sum Circular Subarray | Medium | Two cases: normal Kadane's OR total - min subarray |
| 1186 | Max Subarray Sum with One Deletion | Medium | Two states: deleted or not deleted |
| 1567 | Max Length Subarray with Positive Product | Medium | Track positive/negative lengths separately |
| 689 | Max Sum of 3 Non-Overlapping Subarrays | Hard | Prefix/suffix + Kadane's combination |

**Checkpoint:** Can you identify when a problem is Kadane's variant vs sliding window vs prefix sum?

### Day 7: Review & Practice
- Re-solve 3 problems from this week **without** looking at solutions (timed: 20 min each)
- Pick: 198 (Fibonacci), 174 (Grid), 918 (Kadane's)

---

## Week 2 — Core String & Sequence DP (LCS + Unbounded Knapsack + 0/1 Knapsack)

This week focuses on two-sequence DP and knapsack thinking — the two most important DP families.

### Day 1-2: Longest Common Subsequence
| # | Problem | Difficulty | Focus |
|---|---------|-----------|-------|
| 1143 | Longest Common Subsequence | Medium | The 2D template — understand every cell |
| 583 | Delete Operation for Two Strings | Medium | LCS variant — min deletions = m+n - 2*LCS |
| 712 | Min ASCII Delete Sum for Two Strings | Medium | Weighted LCS — cost instead of count |
| 1035 | Uncrossed Lines | Medium | Literally LCS in disguise — recognize it |
| 72 | Edit Distance | Medium | **MUST MASTER** — insert/delete/replace transitions |
| 97 | Interleaving String | Medium | Three-string DP — tricky state definition |
| 115 | Distinct Subsequences | Hard | Counting paths in the LCS grid |

**Checkpoint:** Given two strings, can you write the 2D recurrence in 1 minute? Can you optimize to 1D?

### Day 3-4: Unbounded Knapsack
| # | Problem | Difficulty | Focus |
|---|---------|-----------|-------|
| 322 | Coin Change | Medium | **THE** knapsack problem — min coins |
| 518 | Coin Change II | Medium | Count combinations — inner loop order matters! |
| 279 | Perfect Squares | Medium | Same as coin change with squares as coins |
| 377 | Combination Sum IV | Medium | Count permutations (not combinations!) — loop order flipped |
| 983 | Minimum Cost for Tickets | Medium | Days as "coins", great interview problem |
| 1449 | Form Largest Integer with Digits That Add Up to Target | Hard | Knapsack + greedy reconstruction |

**Key insight:** Unbounded = left-to-right inner loop. Items can be reused.

### Day 5-6: 0/1 Knapsack
| # | Problem | Difficulty | Focus |
|---|---------|-----------|-------|
| 416 | Partition Equal Subset Sum | Medium | Subset sum = knapsack with target = sum/2 |
| 494 | Target Sum | Medium | Count subsets — transform to subset sum |
| 474 | Ones and Zeroes | Medium | 2D knapsack (two constraints) |
| 1049 | Last Stone Weight II | Medium | Minimize difference = partition problem |
| 879 | Profitable Schemes | Hard | 3D knapsack — members + profit constraints |
| 805 | Split Array with Same Average | Hard | Tricky knapsack with fractional target |

**Key insight:** 0/1 = right-to-left inner loop. Each item used at most once.

### Day 7: Review & Practice
- **Critical comparison:** Solve 322 (unbounded) then 416 (0/1) back-to-back. Feel the loop direction difference.
- Timed practice: 72 (Edit Distance) — aim for < 15 minutes

---

## Week 3 — Sequence Patterns & State Machines (LIS + State Machine + Palindromic)

### Day 1-2: Longest Increasing Subsequence
| # | Problem | Difficulty | Focus |
|---|---------|-----------|-------|
| 300 | Longest Increasing Subsequence | Medium | O(n²) first, then **O(n log n) with bisect** |
| 673 | Number of Longest Increasing Subsequence | Medium | Count LIS — track both length and count arrays |
| 646 | Maximum Length of Pair Chain | Medium | Sort + LIS / greedy — know both approaches |
| 1048 | Longest String Chain | Medium | LIS on strings with word removal |
| 354 | Russian Doll Envelopes | Hard | Sort trick + LIS — the classic hard variant |
| 1671 | Min Removals to Make Mountain Array | Hard | LIS from left + LIS from right |

**Checkpoint:** Can you code the O(n log n) bisect LIS from memory? Interviewers expect this.

### Day 3-4: State Machine DP (Stock Problems)
| # | Problem | Difficulty | Focus |
|---|---------|-----------|-------|
| 121 | Best Time to Buy and Sell Stock | Easy | One transaction — track min so far |
| 122 | Best Time to Buy and Sell Stock II | Medium | Unlimited transactions — state machine intro |
| 309 | Best Time with Cooldown | Medium | 3 states: hold, sold, rest — draw the diagram! |
| 714 | Best Time with Transaction Fee | Medium | 2 states: hold, cash — add fee on sell |
| 123 | Best Time to Buy and Sell Stock III | Hard | At most 2 transactions — generalize to k |
| 188 | Best Time to Buy and Sell Stock IV | Hard | At most k transactions — the general solution |
| 1220 | Count Vowels Permutation | Hard | Non-stock state machine — shows the pattern is general |

**Approach:** Always draw the state transition diagram first. States = (day, holding?, transactions, cooldown?).

### Day 5-6: Palindromic DP
| # | Problem | Difficulty | Focus |
|---|---------|-----------|-------|
| 647 | Palindromic Substrings | Medium | Expand-around-center OR 2D DP |
| 5 | Longest Palindromic Substring | Medium | Same technique, track the longest |
| 516 | Longest Palindromic Subsequence | Medium | **Key:** LPS(s) = LCS(s, reverse(s)) |
| 131 | Palindrome Partitioning | Medium | Backtracking + isPalindrome DP cache |
| 132 | Palindrome Partitioning II | Hard | Min cuts — precompute palindrome table |
| 1312 | Min Insertion Steps to Make Palindrome | Hard | len - LPS = answer |
| 1216 | Valid Palindrome III | Hard | Remove at most k chars — LPS variant |

**Checkpoint:** Can you see how LPS reduces to LCS? This insight solves many palindrome problems instantly.

### Day 7: Review & Practice
- Code O(n log n) LIS from scratch (no reference)
- Solve stock problem 309 from the state diagram alone
- Solve 516 using both direct DP and the LCS reduction

---

## Week 4 — Advanced Patterns I (Linear DP + Range DP + String DP)

### Day 1-2: Linear DP (Scheduling & Jump Games)
| # | Problem | Difficulty | Focus |
|---|---------|-----------|-------|
| 55 | Jump Game | Medium | Greedy is better here — know when NOT to DP |
| 45 | Jump Game II | Medium | Greedy BFS approach — but understand the DP too |
| 139 | Word Break | Medium | Linear scan + set lookup — O(n²) or Trie |
| 256 | Paint House | Medium | 3-state linear DP |
| 1235 | Maximum Profit in Job Scheduling | Hard | Sort + binary search + DP — **top interview problem** |
| 1696 | Jump Game VI | Medium | DP + monotonic deque optimization |
| 887 | Super Egg Drop | Hard | Binary search on DP — impressive if you nail it |

### Day 3-4: Range DP (Matrix Chain Multiplication)
| # | Problem | Difficulty | Focus |
|---|---------|-----------|-------|
| 241 | Different Ways to Add Parentheses | Medium | Divide & conquer introduction to range DP |
| 312 | Burst Balloons | Hard | **THE** range DP problem — think "last burst" not "first burst" |
| 1039 | Min Score Triangulation of Polygon | Medium | Classic MCM on polygon |
| 1547 | Minimum Cost to Cut a Stick | Hard | Sort cuts, then range DP on intervals |
| 1000 | Minimum Cost to Merge Stones | Hard | Range DP with constraint k — challenging |

**Template:** `for length in range(2, n+1): for i in range(...): j = i + length - 1: for k in range(i, j):`

### Day 5-6: String DP
| # | Problem | Difficulty | Focus |
|---|---------|-----------|-------|
| 139 | Word Break | Medium | Already seen in linear DP — revisit with Trie |
| 140 | Word Break II | Hard | Word break + backtracking to collect all paths |
| 87 | Scramble String | Hard | 3D DP or memoized recursion |
| 2707 | Extra Characters in a String | Medium | Modern variant of word break — very common now |
| 1531 | String Compression II | Hard | Delete at most k chars to minimize run-length — tricky |

### Day 7: Review & Practice
- Timed: 1235 (Job Scheduling) — must finish in 25 min
- Timed: 312 (Burst Balloons) — write the range DP template from memory

---

## Week 5 — Advanced Patterns II (Tree DP + Interval/Game + Prefix/Suffix)

### Day 1-2: Tree DP
| # | Problem | Difficulty | Focus |
|---|---------|-----------|-------|
| 543 | Diameter of Binary Tree | Easy | Post-order, return height, track global max |
| 337 | House Robber III | Medium | Return (rob, skip) tuple from each node |
| 124 | Binary Tree Maximum Path Sum | Hard | Same pattern as diameter but with values |
| 968 | Binary Tree Cameras | Hard | 3 states per node: covered, has camera, not covered |
| 834 | Sum of Distances in Tree | Hard | **Rerooting DP** — two-pass technique, very impressive |
| 2246 | Longest Path with Different Adjacent Characters | Hard | Tree diameter variant |

**Pattern:** Always think post-order. Return a tuple of states from each subtree.

### Day 3-4: Interval / Game Theory DP
| # | Problem | Difficulty | Focus |
|---|---------|-----------|-------|
| 486 | Predict the Winner | Medium | Minimax DP — my best = total - opponent's best |
| 877 | Stone Game | Medium | Same as 486 — Alice always wins (math proof exists) |
| 464 | Can I Win | Medium | Bitmask + game theory |
| 1140 | Stone Game II | Medium | More complex game state — (index, M) |
| 1406 | Stone Game III | Hard | Three choices per turn |
| 664 | Strange Printer | Hard | Range DP + game-like thinking |

### Day 5-6: Prefix/Suffix DP
| # | Problem | Difficulty | Focus |
|---|---------|-----------|-------|
| 42 | Trapping Rain Water | Hard | Left-max and right-max arrays — **the** prefix/suffix problem |
| 32 | Longest Valid Parentheses | Hard | Stack or DP approach |
| 907 | Sum of Subarray Minimums | Medium | Monotonic stack + contribution technique |
| 828 | Count Unique Characters of All Substrings | Hard | Last-occurrence tracking |
| 2262 | Total Appeal of a String | Hard | Similar to 828 — contribution counting |

### Day 7: Review & Practice
- Solve 834 (rerooting) from scratch — this one impresses interviewers
- Game theory: solve 486 and explain the minimax recurrence out loud

---

## Week 6 — Expert Patterns (Bitmask + Digit DP + Probability + Graph DP)

Only go here if Weeks 1-5 are solid. These are rare in interviews but show deep expertise.

### Day 1-2: Bitmask DP
| # | Problem | Difficulty | Focus |
|---|---------|-----------|-------|
| 526 | Beautiful Arrangement | Medium | Permutation with bitmask — the intro problem |
| 698 | Partition to K Equal Sum Subsets | Medium | Bitmask over subset assignment |
| 847 | Shortest Path Visiting All Nodes | Hard | BFS + bitmask — TSP variant |
| 943 | Find the Shortest Superstring | Hard | TSP-style DP on strings |
| 1125 | Smallest Sufficient Team | Hard | Bitmask over skills — set cover |
| 1799 | Maximize Score After N Operations | Hard | Pair selection with GCD |

**Basics to memorize:** `mask & (1 << i)` (check bit), `mask | (1 << i)` (set bit), subset enumeration.

### Day 3-4: Digit DP
| # | Problem | Difficulty | Focus |
|---|---------|-----------|-------|
| 357 | Count Numbers with Unique Digits | Medium | Intro — can solve without digit DP |
| 233 | Number of Digit One | Hard | Classic digit DP |
| 902 | Numbers At Most N Given Digit Set | Hard | Count valid numbers digit by digit |
| 1012 | Numbers with Repeated Digits | Hard | Complement counting + digit DP |
| 2376 | Count Special Integers | Hard | Clean digit DP template problem |

**Template state:** `(position, tight, started, ...extra)` — memoize on these.

### Day 5: Probability DP
| # | Problem | Difficulty | Focus |
|---|---------|-----------|-------|
| 576 | Out of Boundary Paths | Medium | Grid + steps DP — count paths |
| 688 | Knight Probability in Chessboard | Medium | Same structure as 576 |
| 837 | New 21 Game | Medium | Sliding window probability |
| 808 | Soup Servings | Medium | 2D probability with early termination |

### Day 6: Graph DP
| # | Problem | Difficulty | Focus |
|---|---------|-----------|-------|
| 787 | Cheapest Flights Within K Stops | Medium | Bellman-Ford style DP |
| 1334 | Find the City with Smallest Number of Neighbors | Medium | Floyd-Warshall |
| 1857 | Largest Color Value in Directed Graph | Hard | Topological sort + DP |
| 2050 | Parallel Courses III | Hard | DAG DP — longest path |

### Day 7: Final Review
- Pick your 3 weakest patterns and re-solve one problem from each
- Do a mock interview: pick a random problem from Weeks 1-3, solve in 25 min

---

## Quick Reference: The 30 Must-Know Problems

If you're short on time, these 30 problems cover the most critical DP concepts:

| # | Problem | Pattern | Priority |
|---|---------|---------|----------|
| 70 | Climbing Stairs | Fibonacci | ★★★ |
| 198 | House Robber | Fibonacci | ★★★ |
| 53 | Maximum Subarray | Kadane's | ★★★ |
| 152 | Maximum Product Subarray | Kadane's | ★★★ |
| 62 | Unique Paths | Grid | ★★★ |
| 64 | Minimum Path Sum | Grid | ★★★ |
| 221 | Maximal Square | Grid | ★★★ |
| 322 | Coin Change | Unbounded Knapsack | ★★★ |
| 518 | Coin Change II | Unbounded Knapsack | ★★★ |
| 416 | Partition Equal Subset Sum | 0/1 Knapsack | ★★★ |
| 494 | Target Sum | 0/1 Knapsack | ★★★ |
| 1143 | Longest Common Subsequence | LCS | ★★★ |
| 72 | Edit Distance | LCS | ★★★ |
| 300 | Longest Increasing Subsequence | LIS | ★★★ |
| 354 | Russian Doll Envelopes | LIS | ★★★ |
| 121 | Best Time to Buy Stock | State Machine | ★★★ |
| 309 | Best Time with Cooldown | State Machine | ★★★ |
| 5 | Longest Palindromic Substring | Palindromic | ★★★ |
| 516 | Longest Palindromic Subsequence | Palindromic | ★★★ |
| 139 | Word Break | String/Linear | ★★★ |
| 1235 | Max Profit Job Scheduling | Linear | ★★★ |
| 312 | Burst Balloons | Range DP | ★★☆ |
| 337 | House Robber III | Tree DP | ★★☆ |
| 124 | Binary Tree Max Path Sum | Tree DP | ★★☆ |
| 42 | Trapping Rain Water | Prefix/Suffix | ★★☆ |
| 486 | Predict the Winner | Game Theory | ★★☆ |
| 698 | Partition to K Equal Sum Subsets | Bitmask | ★★☆ |
| 787 | Cheapest Flights Within K Stops | Graph DP | ★★☆ |
| 233 | Number of Digit One | Digit DP | ★☆☆ |
| 688 | Knight Probability in Chessboard | Probability | ★☆☆ |

---

## Progress Tracker

### Week 1: Fibonacci + Grid + Kadane's
- [ ] Day 1-2: Fibonacci (7 problems)
- [ ] Day 3-4: Grid DP (7 problems)
- [ ] Day 5-6: Kadane's (6 problems)
- [ ] Day 7: Review (3 problems)
- **Total: 23 problems**

### Week 2: LCS + Unbounded Knapsack + 0/1 Knapsack
- [ ] Day 1-2: LCS (7 problems)
- [ ] Day 3-4: Unbounded Knapsack (6 problems)
- [ ] Day 5-6: 0/1 Knapsack (6 problems)
- [ ] Day 7: Review (3 problems)
- **Total: 22 problems**

### Week 3: LIS + State Machine + Palindromic
- [ ] Day 1-2: LIS (6 problems)
- [ ] Day 3-4: State Machine (7 problems)
- [ ] Day 5-6: Palindromic (7 problems)
- [ ] Day 7: Review (3 problems)
- **Total: 23 problems**

### Week 4: Linear DP + Range DP + String DP
- [ ] Day 1-2: Linear DP (7 problems)
- [ ] Day 3-4: Range DP (5 problems)
- [ ] Day 5-6: String DP (5 problems)
- [ ] Day 7: Review (2 problems)
- **Total: 19 problems**

### Week 5: Tree DP + Game Theory + Prefix/Suffix
- [ ] Day 1-2: Tree DP (6 problems)
- [ ] Day 3-4: Game Theory (6 problems)
- [ ] Day 5-6: Prefix/Suffix (5 problems)
- [ ] Day 7: Review (3 problems)
- **Total: 20 problems**

### Week 6: Bitmask + Digit + Probability + Graph
- [ ] Day 1-2: Bitmask DP (6 problems)
- [ ] Day 3-4: Digit DP (5 problems)
- [ ] Day 5: Probability DP (4 problems)
- [ ] Day 6: Graph DP (4 problems)
- [ ] Day 7: Final Review (3 problems)
- **Total: 22 problems**

### Grand Total: ~129 carefully selected problems across 6 weeks

---

*All solutions already exist in this repo under `patterns/dynamic_programming/{pattern}/solutions/`.*
*When stuck, read your own solution — but try for 20 minutes first.*
