# DP Mastery Study Plan — Big Tech Interview Prep

Prioritized study order based on interview frequency at FAANG/Big Tech.

---

## Tier 1 — Must Know (Week 1-2)
*These show up in almost every DP interview round.*

| Priority | Pattern | Key Problems to Start With | Why |
|---|---|---|---|
| 1 | **01 Fibonacci** | 70, 198, 213, 91 | Warm-up, builds DP intuition |
| 2 | **10 Grid DP** | 62, 64, 120, 221 | Very common, visual, easy to explain |
| 3 | **06 Kadane's** | 53, 152, 918 | Asked constantly at Google/Meta |
| 4 | **04 LCS** | 1143, 72, 97, 10 | Edit distance is a classic |
| 5 | **03 Unbounded Knapsack** | 322, 518, 279 | Coin change is asked everywhere |

### What to master in Tier 1
- **Recurrence writing:** Given a problem, write the recurrence in < 2 minutes
- **Space optimization:** Convert 2D DP to 1D (row-by-row, right-to-left tricks)
- **Base cases:** Know when to use dp[0]=1 vs dp[0]=0
- **Time complexity analysis:** Be able to state it immediately

---

## Tier 2 — High Frequency (Week 2-3)
*Frequently tested, especially at FAANG.*

| Priority | Pattern | Key Problems to Start With | Why |
|---|---|---|---|
| 6 | **02 0/1 Knapsack** | 416, 494, 474 | Subset sum variants are common |
| 7 | **05 LIS** | 300, 354, 1048 | Google/Amazon favorite |
| 8 | **14 State Machine** | 121→122→123→188, 309, 714 | Stock problems are a classic series |
| 9 | **08 Palindromic** | 5, 516, 647, 131 | String DP staple |
| 10 | **19 Linear DP** | 139, 403, 1235, 983 | Catch-all for scheduling/jump games |

### What to master in Tier 2
- **0/1 vs Unbounded:** Know when to iterate right-to-left (0/1) vs left-to-right (unbounded)
- **LIS O(n log n):** The patience sorting / bisect approach — interviewers expect this
- **State machine drawing:** For stock problems, draw the state diagram on the whiteboard first
- **Pattern recognition:** Given a new problem, identify which Tier 1-2 pattern it maps to

---

## Tier 3 — Differentiators (Week 3-4)
*These separate strong candidates from average ones.*

| Priority | Pattern | Key Problems to Start With | Why |
|---|---|---|---|
| 11 | **07 MCM / Range DP** | 312, 1039, 1547 | Hard but impressive if you nail it |
| 12 | **09 Tree DP** | 337, 124, 968, 834 | Shows tree + DP mastery |
| 13 | **12 Interval / Game** | 486, 877, 464 | Game theory shows up at Google |
| 14 | **16 String DP** | 139, 140, 87 | Common at Amazon/Meta |
| 15 | **20 Prefix/Suffix** | 42, 907 | Often disguised as other problems |

### What to master in Tier 3
- **Range DP template:** `for length in range(2, n+1): for i in range(...): j = i+length-1`
- **Tree DP post-order:** Always process children first, return (state1, state2) tuples
- **Rerooting DP:** Two-pass technique (#834) — very impressive in interviews
- **Game theory minimax:** "My best = total - opponent's best" trick

---

## Tier 4 — Advanced (Week 4+, if time)
*Rarely asked but shows deep expertise.*

| Priority | Pattern | Key Problems to Start With | Why |
|---|---|---|---|
| 16 | **11 Bitmask DP** | 698, 526, 943 | Hard rounds at Google/Apple |
| 17 | **13 Digit DP** | 233, 902, 2376 | Niche but shows math skills |
| 18 | **18 Graph DP** | 787, 1334 | Combines graph + DP |
| 19 | **15 Combinatorial** | 22, 343, 903 | Math-heavy, less common |
| 20 | **17 Probability DP** | 688, 837 | Rare, mostly Google |

### What to master in Tier 4
- **Bitmask basics:** `mask & (1 << i)`, `mask | (1 << i)`, subset enumeration
- **Digit DP template:** Process digits left-to-right with (position, tight, started) state
- **When NOT to use DP:** Some problems are better solved with greedy or binary search

---

## Study Strategy

### Per-pattern workflow
1. Read the `pattern.md` template in the pattern directory
2. Solve 2-3 Easy/Medium problems — build the muscle memory
3. Solve 1-2 Hard problems — test edge case handling
4. Try a new problem **without** looking at the pattern first — can you identify it?

### Daily routine (recommended)
- **Morning (1 hr):** 1 new pattern problem (timed, 30 min max before looking at hints)
- **Evening (30 min):** Review 2-3 solutions from today's pattern, focus on recurrence

### For a 2-week sprint
Tier 1 + Tier 2 (patterns 1-10) covers **~80% of what you'll see** in Big Tech interviews.

### For a 4-week deep dive
All 4 tiers. You'll be able to handle any DP problem thrown at you.

---

## Company-Specific Focus

| Company | Heavy On | Focus Patterns |
|---|---|---|
| **Google** | Game theory, Bitmask, Digit DP | 12, 11, 13 + all Tier 1-2 |
| **Meta** | String DP, Kadane's, Grid DP | 16, 06, 10 + all Tier 1-2 |
| **Amazon** | LIS, Knapsack, Linear DP | 05, 02, 19 + all Tier 1-2 |
| **Apple** | Tree DP, State Machine | 09, 14 + all Tier 1-2 |
| **Microsoft** | Grid DP, LCS, Fibonacci | 10, 04, 01 + all Tier 1-2 |

---

## Interview Day Checklist

When you see a DP problem in an interview:

1. **Identify the pattern** (< 1 min) — what type of DP is this?
2. **Define the state** — what does dp[i] (or dp[i][j]) represent?
3. **Write the recurrence** — transitions between states
4. **Identify base cases** — what's dp[0]? empty string? first element?
5. **Determine traversal order** — bottom-up direction, do you need right-to-left?
6. **Code it** — template from the pattern
7. **Optimize space** — can you reduce from 2D to 1D?
8. **State complexity** — time and space before the interviewer asks

### Common interview mistakes to avoid
- Jumping to code before defining the recurrence
- Forgetting base cases (especially empty string / zero elements)
- Wrong traversal order (causes using not-yet-computed values)
- Not considering space optimization (interviewers often ask as follow-up)
- Over-engineering when greedy works (e.g., Jump Game is greedy, not DP)
