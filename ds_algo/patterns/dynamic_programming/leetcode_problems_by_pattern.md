# LeetCode Dynamic Programming Problems by Pattern

Quick-reference study sheet — every DP-tagged problem grouped by its dominant pattern, sorted by difficulty (Easy → Medium → Hard) then by problem number within each group.

**Total problems: ~646 | Patterns: 20**

---

## 01 — Fibonacci Pattern
*Current state depends on previous 1–2 states (linear recurrence).*

| # | Problem | Difficulty | Solved | Solution |
|---|---------|------------|--------|----------|
| 70 | Climbing Stairs | Easy | Y | [solution](01_fibonacci_pattern/solutions/70-climbing-stairs.py) |
| 509 | Fibonacci Number | Easy | | |
| 746 | Min Cost Climbing Stairs | Easy | | |
| 1025 | Divisor Game | Easy | | |
| 1137 | N-th Tribonacci Number | Easy | | |
| 91 | Decode Ways | Medium | Y | [solution](01_fibonacci_pattern/solutions/91-decode-ways.py) |
| 198 | House Robber | Medium | Y | [solution](01_fibonacci_pattern/solutions/198-house-robber.py) |
| 213 | House Robber II | Medium | Y | [solution](01_fibonacci_pattern/solutions/213-house-robber-ii.py) |
| 276 | Paint Fence | Medium | Y | [solution](01_fibonacci_pattern/solutions/276-paint-fence.py) |
| 338 | Counting Bits | Easy | Y | [solution](01_fibonacci_pattern/solutions/338-counting-bits.py) |
| 740 | Delete and Earn | Medium | | |
| 790 | Domino and Tromino Tiling | Medium | | |
| 935 | Knight Dialer | Medium | | |
| 1578 | Minimum Time to Make Rope Colorful | Medium | | |
| 2466 | Count Ways To Build Good Strings | Medium | | |
| 2320 | Count Number of Ways to Place Houses | Medium | | |
| 2745 | Construct the Longest New String | Medium | | |
| 2957 | Remove Adjacent Almost-Equal Characters | Medium | | |
| 3259 | Maximum Energy Boost From Two Drinks | Medium | | |
| 3693 | Climbing Stairs II | Medium | | |
| 639 | Decode Ways II | Hard | | |

---

## 02 — 0/1 Knapsack
*Include or exclude each item exactly once.*

| # | Problem | Difficulty | Solved | Solution |
|---|---------|------------|--------|----------|
| 416 | Partition Equal Subset Sum | Medium | Y | [solution](02_knapsack_01/solutions/416-partition-equal-subset-sum.py) |
| 474 | Ones and Zeroes | Medium | | |
| 494 | Target Sum | Medium | | |
| 1049 | Last Stone Weight II | Medium | | |
| 1981 | Minimize the Difference Between Target and Chosen Elements | Medium | | |
| 2291 | Maximum Profit From Trading Stocks | Medium | | |
| 2431 | Maximize Total Tastiness of Purchased Fruits | Medium | | |
| 2915 | Length of the Longest Subsequence That Sums to Target | Medium | | |
| 3366 | Minimum Array Sum | Medium | | |
| 3489 | Zero Array Transformation IV | Medium | | |
| 3647 | Maximum Weight in Two Bags | Medium | | |
| 879 | Profitable Schemes | Hard | | |
| 956 | Tallest Billboard | Hard | | |
| 805 | Split Array With Same Average | Hard | | |
| 1255 | Maximum Score Words Formed by Letters | Hard | | |
| 2518 | Number of Great Partitions | Hard | | |
| 2585 | Number of Ways to Earn Points | Hard | | |
| 2742 | Painting the Walls | Hard | | |
| 3444 | Minimum Increments for Target Multiples in an Array | Hard | | |
| 3509 | Maximum Product of Subsequences With an Alternating Sum Equal to K | Hard | | |

---

## 03 — Unbounded Knapsack
*Items can be reused unlimited times.*

| # | Problem | Difficulty | Solved | Solution |
|---|---------|------------|--------|----------|
| 279 | Perfect Squares | Medium | Y | [solution](03_unbounded_knapsack/solutions/279-perfect-squares.py) |
| 322 | Coin Change | Medium | Y | [solution](03_unbounded_knapsack/solutions/322-coin-change.py) |
| 377 | Combination Sum IV | Medium | Y | [solution](03_unbounded_knapsack/solutions/377-combination-sum-iv.py) |
| 518 | Coin Change II | Medium | | |
| 983 | Minimum Cost For Tickets | Medium | | |
| 1155 | Number of Dice Rolls With Target Sum | Medium | | |
| 2787 | Ways to Express an Integer as Sum of Powers | Medium | | |
| 2979 | Most Expensive Item That Can Not Be Bought | Medium | | |
| 3183 | The Number of Ways to Make the Sum | Medium | | |
| 3592 | Inverse Coin Change | Medium | | |
| 3610 | Minimum Number of Primes to Sum to Target | Medium | | |
| 1449 | Form Largest Integer With Digits That Add up to Target | Hard | | |
| 2902 | Count of Sub-Multisets With Bounded Sum | Hard | | |

---

## 04 — Longest Common Subsequence
*Two-sequence alignment / comparison.*

| # | Problem | Difficulty | Solved | Solution |
|---|---------|------------|--------|----------|
| 392 | Is Subsequence | Easy | Y | [solution](04_longest_common_subsequence/solutions/392-is-subsequence.py) |
| 583 | Delete Operation for Two Strings | Medium | | |
| 712 | Minimum ASCII Delete Sum for Two Strings | Medium | | |
| 718 | Maximum Length of Repeated Subarray | Medium | | |
| 1035 | Uncrossed Lines | Medium | | |
| 1143 | Longest Common Subsequence | Medium | | |
| 1458 | Max Dot Product of Two Subsequences | Hard | | |
| 72 | Edit Distance | Medium | Y | [solution](04_longest_common_subsequence/solutions/72-edit-distance.py) |
| 97 | Interleaving String | Medium | Y | [solution](04_longest_common_subsequence/solutions/97-interleaving-string.py) |
| 10 | Regular Expression Matching | Hard | Y | [solution](04_longest_common_subsequence/solutions/10-regular-expression-matching.py) |
| 44 | Wildcard Matching | Hard | Y | [solution](04_longest_common_subsequence/solutions/44-wildcard-matching.py) |
| 115 | Distinct Subsequences | Hard | Y | [solution](04_longest_common_subsequence/solutions/115-distinct-subsequences.py) |
| 1092 | Shortest Common Supersequence | Hard | | |
| 727 | Minimum Window Subsequence | Hard | | |
| 2060 | Check if an Original String Exists Given Two Encoded Strings | Hard | | |
| 3135 | Equalize Strings by Adding or Removing Characters at Ends | Medium | | |
| 3316 | Find Maximum Removals From Source String | Medium | | |

---

## 05 — Longest Increasing Subsequence
*Single-sequence ordering / subsequence problems.*

| # | Problem | Difficulty | Solved | Solution |
|---|---------|------------|--------|----------|
| 300 | Longest Increasing Subsequence | Medium | Y | [solution](05_longest_increasing_subsequence/solutions/300-longest-increasing-subsequence.py) |
| 368 | Largest Divisible Subset | Medium | Y | [solution](05_longest_increasing_subsequence/solutions/368-largest-divisible-subset.py) |
| 376 | Wiggle Subsequence | Medium | Y | [solution](05_longest_increasing_subsequence/solutions/376-wiggle-subsequence.py) |
| 646 | Maximum Length of Pair Chain | Medium | | |
| 673 | Number of Longest Increasing Subsequence | Medium | | |
| 1027 | Longest Arithmetic Subsequence | Medium | | |
| 1048 | Longest String Chain | Medium | | |
| 1218 | Longest Arithmetic Subsequence of Given Difference | Medium | | |
| 1626 | Best Team With No Conflicts | Medium | | |
| 2370 | Longest Ideal Subsequence | Medium | | |
| 2501 | Longest Square Streak in an Array | Medium | | |
| 2826 | Sorting Three Groups | Medium | | |
| 2900 | Longest Unequal Adjacent Groups Subsequence I | Easy | | |
| 2901 | Longest Unequal Adjacent Groups Subsequence II | Medium | | |
| 354 | Russian Doll Envelopes | Hard | Y | [solution](05_longest_increasing_subsequence/solutions/354-russian-doll-envelopes.py) |
| 446 | Arithmetic Slices II - Subsequence | Hard | Y | [solution](05_longest_increasing_subsequence/solutions/446-arithmetic-slices-ii-subsequence.py) |
| 873 | Length of Longest Fibonacci Subsequence | Medium | | |
| 1187 | Make Array Strictly Increasing | Hard | | |
| 1671 | Minimum Number of Removals to Make Mountain Array | Hard | | |
| 1691 | Maximum Height by Stacking Cuboids | Hard | | |
| 1964 | Find the Longest Valid Obstacle Course at Each Position | Hard | | |
| 2407 | Longest Increasing Subsequence II | Hard | | |
| 2926 | Maximum Balanced Subsequence Sum | Hard | | |
| 3041 | Maximize Consecutive Elements in an Array After Modification | Hard | | |
| 3176 | Find the Maximum Length of a Good Subsequence I | Medium | | |
| 3177 | Find the Maximum Length of a Good Subsequence II | Hard | | |
| 3201 | Find the Maximum Length of Valid Subsequence I | Medium | | |
| 3202 | Find the Maximum Length of Valid Subsequence II | Medium | | |
| 3409 | Longest Subsequence With Decreasing Adjacent Difference | Medium | | |

---

## 06 — Kadane's Pattern
*Max/min contiguous subarray.*

| # | Problem | Difficulty | Solved | Solution |
|---|---------|------------|--------|----------|
| 53 | Maximum Subarray | Medium | Y | [solution](06_kadanes_pattern/solutions/53-maximum-subarray.py) |
| 152 | Maximum Product Subarray | Medium | Y | [solution](06_kadanes_pattern/solutions/152-maximum-product-subarray.py) |
| 413 | Arithmetic Slices | Medium | Y | [solution](06_kadanes_pattern/solutions/413-arithmetic-slices.py) |
| 845 | Longest Mountain in Array | Medium | | |
| 918 | Maximum Sum Circular Subarray | Medium | | |
| 978 | Longest Turbulent Subarray | Medium | | |
| 1186 | Maximum Subarray Sum with One Deletion | Medium | | |
| 1191 | K-Concatenation Maximum Sum | Medium | | |
| 1567 | Maximum Length of Subarray With Positive Product | Medium | | |
| 1746 | Maximum Subarray Sum After One Operation | Medium | | |
| 1749 | Maximum Absolute Sum of Any Subarray | Medium | | |
| 2036 | Maximum Alternating Subarray Sum | Medium | | |
| 2110 | Number of Smooth Descent Periods of a Stock | Medium | | |
| 2393 | Count Strictly Increasing Subarrays | Medium | | |
| 2606 | Find the Substring With Maximum Cost | Medium | | |
| 3284 | Sum of Consecutive Subarrays | Medium | | |
| 689 | Maximum Sum of 3 Non-Overlapping Subarrays | Hard | | |
| 2272 | Substring With Largest Variance | Hard | | |
| 2321 | Maximum Score Of Spliced Array | Hard | | |
| 3077 | Maximum Strength of K Disjoint Subarrays | Hard | | |
| 3165 | Maximum Sum of Subsequence With Non-adjacent Elements | Hard | | |
| 3410 | Maximize Subarray Sum After Removing All Occurrences of One Element | Hard | | |
| 3473 | Sum of K Subarrays With Length at Least M | Medium | | |
| 3830 | Longest Alternating Subarray After Removing At Most One Element | Hard | | |

---

## 07 — Matrix Chain Multiplication / Range DP
*Find optimal split point in a range [i, j].*

| # | Problem | Difficulty | Solved | Solution |
|---|---------|------------|--------|----------|
| 241 | Different Ways to Add Parentheses | Medium | Y | [solution](07_matrix_chain_multiplication/solutions/241-different-ways-to-add-parentheses.py) |
| 375 | Guess Number Higher or Lower II | Medium | Y | [solution](07_matrix_chain_multiplication/solutions/375-guess-number-higher-or-lower-ii.py) |
| 1039 | Minimum Score Triangulation of Polygon | Medium | | |
| 1130 | Minimum Cost Tree From Leaf Values | Medium | | |
| 312 | Burst Balloons | Hard | Y | [solution](07_matrix_chain_multiplication/solutions/312-burst-balloons.py) |
| 1000 | Minimum Cost to Merge Stones | Hard | | |
| 1547 | Minimum Cost to Cut a Stick | Hard | | |
| 813 | Largest Sum of Averages | Medium | | |
| 410 | Split Array Largest Sum | Hard | Y | [solution](07_matrix_chain_multiplication/solutions/410-split-array-largest-sum.py) |
| 1335 | Minimum Difficulty of a Job Schedule | Hard | | |
| 1478 | Allocate Mailboxes | Hard | | |
| 2463 | Minimum Total Distance Traveled | Hard | | |
| 3277 | Maximum XOR Score Subarray Queries | Hard | | |
| 3801 | Minimum Cost to Merge Sorted Lists | Hard | | |

---

## 08 — Palindromic Subsequence
*Palindrome structure on strings/subsequences.*

| # | Problem | Difficulty | Solved | Solution |
|---|---------|------------|--------|----------|
| 5 | Longest Palindromic Substring | Medium | Y | [solution](08_palindromic_subsequence/solutions/5-longest-palindromic-substring.py) |
| 131 | Palindrome Partitioning | Medium | Y | [solution](08_palindromic_subsequence/solutions/131-palindrome-partitioning.py) |
| 516 | Longest Palindromic Subsequence | Medium | | |
| 647 | Palindromic Substrings | Medium | | |
| 1682 | Longest Palindromic Subsequence II | Medium | | |
| 2002 | Maximum Product of Two Palindromic Subsequences | Medium | | |
| 132 | Palindrome Partitioning II | Hard | Y | [solution](08_palindromic_subsequence/solutions/132-palindrome-partitioning-ii.py) |
| 730 | Count Different Palindromic Subsequences | Hard | | |
| 1147 | Longest Chunked Palindrome Decomposition | Hard | | |
| 1216 | Valid Palindrome III | Hard | | |
| 1246 | Palindrome Removal | Hard | | |
| 1278 | Palindrome Partitioning III | Hard | | |
| 1312 | Minimum Insertion Steps to Make a String Palindrome | Hard | | |
| 1745 | Palindrome Partitioning IV | Hard | | |
| 1771 | Maximize Palindrome Length From Subsequences | Hard | | |
| 2472 | Maximum Number of Non-overlapping Palindrome Substrings | Hard | | |
| 2484 | Count Palindromic Subsequences | Hard | | |
| 3260 | Find the Largest Palindrome Divisible by K | Hard | | |
| 3441 | Minimum Cost Good Caption | Hard | | |
| 3472 | Longest Palindromic Subsequence After at Most K Operations | Medium | | |
| 3503 | Longest Palindrome After Substring Concatenation I | Medium | | |
| 3504 | Longest Palindrome After Substring Concatenation II | Hard | | |
| 3615 | Longest Palindromic Path in Graph | Hard | | |
| 3844 | Longest Almost-Palindromic Substring | Medium | | |

---

## 09 — DP on Trees
*Post-order traversal combined with DP.*

| # | Problem | Difficulty | Solved | Solution |
|---|---------|------------|--------|----------|
| 543 | Diameter of Binary Tree | Easy | | |
| 95 | Unique Binary Search Trees II | Medium | Y | [solution](09_dp_on_trees/solutions/95-unique-binary-search-trees-ii.py) |
| 96 | Unique Binary Search Trees | Medium | Y | [solution](09_dp_on_trees/solutions/96-unique-binary-search-trees.py) |
| 310 | Minimum Height Trees | Medium | | |
| 333 | Largest BST Subtree | Medium | Y | [solution](09_dp_on_trees/solutions/333-largest-bst-subtree.py) |
| 337 | House Robber III | Medium | Y | [solution](09_dp_on_trees/solutions/337-house-robber-iii.py) |
| 823 | Binary Trees With Factors | Medium | | |
| 894 | All Possible Full Binary Trees | Medium | | |
| 1372 | Longest ZigZag Path in a Binary Tree | Medium | | |
| 2378 | Choose Edges to Maximize Score in a Tree | Medium | | |
| 2673 | Make Costs of Paths Equal in a Binary Tree | Medium | | |
| 2925 | Maximum Score After Applying Operations on a Tree | Medium | | |
| 3004 | Maximum Subtree of the Same Color | Medium | | |
| 3593 | Minimum Increments to Equalize Leaf Paths | Medium | | |
| 124 | Binary Tree Maximum Path Sum | Hard | Y | [solution](09_dp_on_trees/solutions/124-binary-tree-maximum-path-sum.py) |
| 834 | Sum of Distances in Tree | Hard | | |
| 968 | Binary Tree Cameras | Hard | | |
| 1373 | Maximum Sum BST in Binary Tree | Hard | | |
| 1483 | Kth Ancestor of a Tree Node | Hard | | |
| 1569 | Number of Ways to Reorder Array to Get Same BST | Hard | | |
| 1916 | Count Ways to Build Rooms in an Ant Colony | Hard | | |
| 2003 | Smallest Missing Genetic Value in Each Subtree | Hard | | |
| 2005 | Subtree Removal Game with Fibonacci Tree | Hard | | |
| 2313 | Minimum Flips in Binary Tree to Get Result | Hard | | |
| 2538 | Difference Between Maximum and Minimum Price Sum | Hard | | |
| 2581 | Count Number of Possible Root Nodes | Hard | | |
| 2646 | Minimize the Total Price of the Trips | Hard | | |
| 2867 | Count Valid Paths in a Tree | Hard | | |
| 2920 | Maximum Points After Collecting Coins From All Nodes | Hard | | |
| 2973 | Find Number of Coins to Place in Tree Nodes | Hard | | |
| 3068 | Find the Maximum Sum of Node Values | Hard | | |
| 3241 | Time Taken to Mark All Nodes | Hard | | |
| 3367 | Maximize Sum of Weights after Edge Removals | Hard | | |
| 3544 | Subtree Inversion Sum | Hard | | |
| 3553 | Minimum Weighted Subgraph With the Required Paths II | Hard | | |
| 3559 | Number of Ways to Assign Edge Weights II | Hard | | |
| 3562 | Maximum Profit from Trading Stocks with Discounts | Hard | | |
| 3575 | Maximum Good Subtree Score | Hard | | |
| 3585 | Find Weighted Median Node in Tree | Hard | | |
| 3772 | Maximum Subgraph Score in a Tree | Hard | | |
| 3840 | House Robber V | Medium | | |

---

## 10 — DP on Grids
*2D traversal with state accumulation.*

| # | Problem | Difficulty | Solved | Solution |
|---|---------|------------|--------|----------|
| 62 | Unique Paths | Medium | Y | [solution](10_dp_on_grids/solutions/62-unique-paths.py) |
| 63 | Unique Paths II | Medium | Y | [solution](10_dp_on_grids/solutions/63-unique-paths-ii.py) |
| 64 | Minimum Path Sum | Medium | Y | [solution](10_dp_on_grids/solutions/64-minimum-path-sum.py) |
| 120 | Triangle | Medium | Y | [solution](10_dp_on_grids/solutions/120-triangle.py) |
| 221 | Maximal Square | Medium | Y | [solution](10_dp_on_grids/solutions/221-maximal-square.py) |
| 542 | 01 Matrix | Medium | | |
| 562 | Longest Line of Consecutive One in Matrix | Medium | | |
| 931 | Minimum Falling Path Sum | Medium | | |
| 1277 | Count Square Submatrices with All Ones | Medium | | |
| 1504 | Count Submatrices With All Ones | Medium | | |
| 1594 | Maximum Non Negative Product in a Matrix | Medium | | |
| 2304 | Minimum Path Cost in a Grid | Medium | | |
| 2510 | Check if There is a Path With Equal Number of 0's And 1's | Medium | | |
| 2556 | Disconnect Path in a Binary Matrix by at Most One Flip | Medium | | |
| 2684 | Maximum Number of Moves in a Grid | Medium | | |
| 3148 | Maximum Difference Score in a Grid | Medium | | |
| 3418 | Maximum Amount of Money Robot Can Earn | Medium | | |
| 3466 | Maximum Coin Collection | Medium | | |
| 3603 | Minimum Cost Path with Alternating Directions II | Medium | | |
| 3742 | Maximum Path Score in a Grid | Medium | | |
| 85 | Maximal Rectangle | Hard | Y | [solution](10_dp_on_grids/solutions/85-maximal-rectangle.py) |
| 174 | Dungeon Game | Hard | Y | [solution](10_dp_on_grids/solutions/174-dungeon-game.py) |
| 329 | Longest Increasing Path in a Matrix | Hard | Y | [solution](10_dp_on_grids/solutions/329-longest-increasing-path-in-a-matrix.py) |
| 741 | Cherry Pickup | Hard | | |
| 1139 | Largest 1-Bordered Square | Medium | | |
| 1289 | Minimum Falling Path Sum II | Hard | | |
| 1301 | Number of Paths with Max Score | Hard | | |
| 1463 | Cherry Pickup II | Hard | | |
| 2088 | Count Fertile Pyramids in a Land | Hard | | |
| 2267 | Check if There Is a Valid Parentheses String Path | Hard | | |
| 2328 | Number of Increasing Paths in a Grid | Hard | | |
| 2435 | Paths in Matrix Whose Sum Is Divisible by K | Hard | | |
| 2617 | Minimum Number of Visited Cells in a Grid | Hard | | |
| 2713 | Maximum Strictly Increasing Cells in a Matrix | Hard | | |
| 3225 | Maximum Score From Grid Operations | Hard | | |
| 3363 | Find the Maximum Number of Fruits Collected | Hard | | |
| 3393 | Count Paths With the Given XOR Value | Medium | | |
| 3459 | Length of Longest V-Shaped Diagonal Segment | Hard | | |
| 3665 | Twisted Mirror Path Count | Medium | | |

---

## 11 — Bitmask DP
*State encoded as a bitmask of visited/used items.*

| # | Problem | Difficulty | Solved | Solution |
|---|---------|------------|--------|----------|
| 473 | Matchsticks to Square | Medium | | |
| 526 | Beautiful Arrangement | Medium | | |
| 698 | Partition to K Equal Sum Subsets | Medium | | |
| 1947 | Maximum Compatibility Score Sum | Medium | | |
| 1986 | Minimum Number of Work Sessions to Finish the Tasks | Medium | | |
| 2305 | Fair Distribution of Cookies | Medium | | |
| 2572 | Count the Number of Square-Free Subsets | Medium | | |
| 2741 | Special Permutations | Medium | | |
| 1066 | Campus Bikes II | Medium | | |
| 2850 | Minimum Moves to Spread Stones Over Grid | Medium | | |
| 3376 | Minimum Time to Break Locks I | Medium | | |
| 691 | Stickers to Spell Word | Hard | | |
| 847 | Shortest Path Visiting All Nodes | Hard | | |
| 943 | Find the Shortest Superstring | Hard | | |
| 996 | Number of Squareful Arrays | Hard | | |
| 1125 | Smallest Sufficient Team | Hard | | |
| 1349 | Maximum Students Taking Exam | Hard | | |
| 1434 | Number of Ways to Wear Different Hats to Each Other | Hard | | |
| 1494 | Parallel Courses II | Hard | | |
| 1595 | Minimum Cost to Connect Two Groups of Points | Hard | | |
| 1617 | Count Subtrees With Max Distance Between Cities | Hard | | |
| 1655 | Distribute Repeating Integers | Hard | | |
| 1659 | Maximize Grid Happiness | Hard | | |
| 1681 | Minimum Incompatibility | Hard | | |
| 1723 | Find Minimum Time to Finish All Jobs | Hard | | |
| 1799 | Maximize Score After N Operations | Hard | | |
| 1815 | Maximum Number of Groups Getting Fresh Donuts | Hard | | |
| 1879 | Minimum XOR Sum of Two Arrays | Hard | | |
| 2172 | Maximum AND Sum of Array | Hard | | |
| 2247 | Maximum Cost of Trip With K Highways | Hard | | |
| 2403 | Minimum Time to Kill All Monsters | Hard | | |
| 2992 | Number of Self-Divisible Permutations | Hard | | |
| 3149 | Find the Minimum Cost Array Permutation | Hard | | |
| 3256 | Maximum Value Sum by Placing Three Rooks I | Hard | | |
| 3257 | Maximum Value Sum by Placing Three Rooks II | Hard | | |
| 3276 | Select Cells in Grid With Maximum Score | Hard | | |
| 3287 | Find the Maximum Sequence Value of Array | Hard | | |
| 3533 | Concatenated Divisibility | Hard | | |
| 3725 | Count Ways to Choose Coprime Integers from Rows | Hard | | |

---

## 12 — Interval DP / Game Theory
*Merge or split intervals optimally; minimax / game strategy.*

| # | Problem | Difficulty | Solved | Solution |
|---|---------|------------|--------|----------|
| 464 | Can I Win | Medium | Y | [solution](12_interval_dp/solutions/464-can-i-win.py) |
| 486 | Predict the Winner | Medium | | |
| 877 | Stone Game | Medium | | |
| 1140 | Stone Game II | Medium | | |
| 1690 | Stone Game VII | Medium | | |
| 1908 | Game of Nim | Medium | | |
| 294 | Flip Game II | Medium | Y | [solution](12_interval_dp/solutions/294-flip-game-ii.py) |
| 546 | Remove Boxes | Hard | | |
| 664 | Strange Printer | Hard | | |
| 1406 | Stone Game III | Hard | | |
| 1510 | Stone Game IV | Hard | | |
| 1563 | Stone Game V | Hard | | |
| 1728 | Cat and Mouse II | Hard | | |
| 1872 | Stone Game VIII | Hard | | |
| 1900 | The Earliest and Latest Rounds Where Players Compete | Hard | | |
| 913 | Cat and Mouse | Hard | | |
| 2019 | The Score of Students Solving Math Expression | Hard | | |
| 3040 | Maximum Number of Operations With the Same Score II | Medium | | |

---

## 13 — Digit DP
*Count numbers satisfying digit-level constraints.*

| # | Problem | Difficulty | Solved | Solution |
|---|---------|------------|--------|----------|
| 357 | Count Numbers with Unique Digits | Medium | Y | [solution](13_digit_dp/solutions/357-count-numbers-with-unique-digits.py) |
| 788 | Rotated Digits | Medium | | |
| 3032 | Count Numbers With Unique Digits II | Easy | | |
| 233 | Number of Digit One | Hard | Y | [solution](13_digit_dp/solutions/233-number-of-digit-one.py) |
| 600 | Non-negative Integers without Consecutive Ones | Hard | | |
| 902 | Numbers At Most N Given Digit Set | Hard | | |
| 1012 | Numbers With Repeated Digits | Hard | | |
| 1067 | Digit Count in Range | Hard | | |
| 2376 | Count Special Integers | Hard | | |
| 2719 | Count of Integers | Hard | | |
| 2801 | Count Stepping Numbers in Range | Hard | | |
| 2827 | Number of Beautiful Integers in the Range | Hard | | |
| 2999 | Count the Number of Powerful Integers | Hard | | |
| 3007 | Maximum Number That Sum of the Prices Is Less Than or Equal to K | Medium | | |
| 3352 | Count K-Reducible Numbers Less Than N | Hard | | |
| 3490 | Count Beautiful Numbers | Hard | | |
| 3519 | Count Numbers with Non-Decreasing Digits | Hard | | |
| 3621 | Number of Integers With Popcount-Depth Equal to K I | Hard | | |
| 3751 | Total Waviness of Numbers in Range I | Medium | | |
| 3753 | Total Waviness of Numbers in Range II | Hard | | |
| 3791 | Number of Balanced Integers in a Range | Hard | | |
| 3869 | Count Fancy Numbers in a Range | Hard | | |

---

## 14 — State Machine DP
*Transitions between defined states (e.g., hold/sold/cooldown).*

| # | Problem | Difficulty | Solved | Solution |
|---|---------|------------|--------|----------|
| 121 | Best Time to Buy and Sell Stock | Easy | Y | [solution](14_state_machine_dp/solutions/121-best-time-to-buy-and-sell-stock.py) |
| 122 | Best Time to Buy and Sell Stock II | Medium | Y | [solution](14_state_machine_dp/solutions/122-best-time-to-buy-and-sell-stock-ii.py) |
| 309 | Best Time to Buy and Sell Stock with Cooldown | Medium | Y | [solution](14_state_machine_dp/solutions/309-best-time-to-buy-and-sell-stock-with-cooldown.py) |
| 714 | Best Time to Buy and Sell Stock with Transaction Fee | Medium | | |
| 926 | Flip String to Monotone Increasing | Medium | | |
| 1824 | Minimum Sideway Jumps | Medium | | |
| 2222 | Number of Ways to Select Buildings | Medium | | |
| 3573 | Best Time to Buy and Sell Stock V | Medium | | |
| 123 | Best Time to Buy and Sell Stock III | Hard | Y | [solution](14_state_machine_dp/solutions/123-best-time-to-buy-and-sell-stock-iii.py) |
| 188 | Best Time to Buy and Sell Stock IV | Hard | Y | [solution](14_state_machine_dp/solutions/188-best-time-to-buy-and-sell-stock-iv.py) |
| 552 | Student Attendance Record II | Hard | | |
| 1220 | Count Vowels Permutation | Hard | | |
| 1223 | Dice Roll Simulation | Hard | | |
| 1787 | Make the XOR of All Segments Equal to Zero | Hard | | |
| 1955 | Count Number of Special Subsequences | Hard | | |
| 2318 | Number of Distinct Roll Sequences | Hard | | |
| 3320 | Count The Number of Winning Sequences | Hard | | |
| 3339 | Find the Number of K-Even Arrays | Medium | | |

---

## 15 — Counting / Combinatorial DP
*Counting arrangements, ways, permutations, combinations.*

| # | Problem | Difficulty | Solved | Solution |
|---|---------|------------|--------|----------|
| 118 | Pascal's Triangle | Easy | Y | [solution](15_counting_combinatorial/solutions/118-pascals-triangle.py) |
| 119 | Pascal's Triangle II | Easy | Y | [solution](15_counting_combinatorial/solutions/119-pascals-triangle-ii.py) |
| 22 | Generate Parentheses | Medium | Y | [solution](15_counting_combinatorial/solutions/22-generate-parentheses.py) |
| 343 | Integer Break | Medium | Y | [solution](15_counting_combinatorial/solutions/343-integer-break.py) |
| 634 | Find the Derangement of An Array | Medium | | |
| 1227 | Airplane Seat Assignment Probability | Medium | | |
| 1259 | Handshakes That Don't Cross | Hard | | |
| 1395 | Count Number of Teams | Medium | | |
| 1621 | Number of Sets of K Non-Overlapping Line Segments | Medium | | |
| 1641 | Count Sorted Vowel Strings | Medium | | |
| 1643 | Kth Smallest Instructions | Hard | | |
| 1735 | Count Ways to Make Array With Product | Hard | | |
| 1866 | Number of Ways to Rearrange Sticks With K Sticks Visible | Hard | | |
| 1931 | Painting a Grid With Three Different Colors | Hard | | |
| 1411 | Number of Ways to Paint N × 3 Grid | Hard | | |
| 2400 | Number of Ways to Reach a Position After Exactly k Steps | Medium | | |
| 2338 | Count the Number of Ideal Arrays | Hard | | |
| 903 | Valid Permutations for DI Sequence | Hard | | |
| 920 | Number of Music Playlists | Hard | | |
| 1359 | Count All Valid Pickup and Delivery Options | Hard | | |
| 1692 | Count Ways to Distribute Candies | Hard | | |
| 2184 | Number of Ways to Build Sturdy Brick Wall | Medium | | |
| 2147 | Number of Ways to Divide a Long Corridor | Hard | | |
| 2552 | Count Increasing Quadruplets | Hard | | |
| 2930 | Number of Strings Which Can Be Rearranged to Contain Substring | Medium | | |
| 3250 | Find the Count of Monotonic Pairs I | Hard | | |
| 3251 | Find the Count of Monotonic Pairs II | Hard | | |
| 3317 | Find the Number of Possible Ways for an Event | Hard | | |
| 3343 | Count Number of Balanced Permutations | Hard | | |
| 3336 | Find the Number of Subsequences With Equal GCD | Hard | | |
| 3797 | Count Routes to Climb a Rectangular Grid | Hard | | |
| 3699 | Number of ZigZag Arrays I | Hard | | |
| 3700 | Number of ZigZag Arrays II | Hard | | |
| 3704 | Count No-Zero Pairs That Sum to N | Hard | | |
| 3757 | Number of Effective Subsequences | Hard | | |
| 3686 | Number of Stable Subsequences | Hard | | |
| 2597 | The Number of Beautiful Subsets | Medium | | |
| 2750 | Ways to Split Array Into Good Subarrays | Medium | | |
| 3850 | Count Sequences to K | Hard | | |

---

## 16 — String DP
*Matching, breaking, encoding, transformation — beyond palindrome/LCS.*

| # | Problem | Difficulty | Solved | Solution |
|---|---------|------------|--------|----------|
| 1668 | Maximum Repeating Substring | Easy | | |
| 139 | Word Break | Medium | Y | [solution](16_string_dp/solutions/139-word-break.py) |
| 467 | Unique Substrings in Wraparound String | Medium | | |
| 553 | Optimal Division | Medium | | |
| 1062 | Longest Repeating Substring | Medium | | |
| 1638 | Count Substrings That Differ by One Character | Medium | | |
| 2266 | Count Number of Texts | Medium | | |
| 2645 | Minimum Additions to Make Valid String | Medium | | |
| 2707 | Extra Characters in a String | Medium | | |
| 2746 | Decremental String Concatenation | Medium | | |
| 2767 | Partition String Into Minimum Beautiful Substrings | Medium | | |
| 3144 | Minimum Substring Partition of Equal Character Frequency | Medium | | |
| 3302 | Find the Lexicographically Smallest Valid Sequence | Medium | | |
| 87 | Scramble String | Hard | Y | [solution](16_string_dp/solutions/87-scramble-string.py) |
| 140 | Word Break II | Hard | Y | [solution](16_string_dp/solutions/140-word-break-ii.py) |
| 466 | Count The Repetitions | Hard | | |
| 471 | Encode String with Shortest Length | Hard | | |
| 472 | Concatenated Words | Hard | | |
| 940 | Distinct Subsequences II | Hard | | |
| 1397 | Find All Good Strings | Hard | | |
| 1416 | Restore The Array | Hard | | |
| 1531 | String Compression II | Hard | | |
| 1639 | Number of Ways to Form a Target String Given a Dictionary | Hard | | |
| 1977 | Number of Ways to Separate Numbers | Hard | | |
| 1987 | Number of Unique Good Subsequences | Hard | | |
| 2430 | Maximum Deletions on a String | Hard | | |
| 2478 | Number of Beautiful Partitions | Hard | | |
| 2573 | Find the String with LCP | Hard | | |
| 2851 | String Transformation | Hard | | |
| 2911 | Minimum Changes to Make K Semi-palindromes | Hard | | |
| 2977 | Minimum Cost to Convert String II | Hard | | |
| 3003 | Maximize the Number of Partitions After Operations | Hard | | |
| 3213 | Construct String with Minimum Cost | Hard | | |
| 3291 | Minimum Number of Valid Strings to Form Target I | Medium | | |
| 3292 | Minimum Number of Valid Strings to Form Target II | Hard | | |
| 3333 | Find the Original Typed String II | Hard | | |
| 3335 | Total Characters in String After Transformations I | Medium | | |
| 3337 | Total Characters in String After Transformations II | Hard | | |
| 3388 | Count Beautiful Splits in an Array | Medium | | |
| 3434 | Maximum Frequency After Subarray Operation | Medium | | |
| 3448 | Count Substrings Divisible By Last Digit | Hard | | |
| 3458 | Select K Disjoint Special Substrings | Medium | | |
| 3557 | Find Maximum Number of Non Intersecting Substrings | Medium | | |
| 3563 | Lexicographically Smallest String After Adjacent Removals | Hard | | |
| 3579 | Minimum Steps to Convert String with Operations | Hard | | |

---

## 17 — Probability / Expected Value DP
*Probability, expected value, or stochastic processes.*

| # | Problem | Difficulty | Solved | Solution |
|---|---------|------------|--------|----------|
| 808 | Soup Servings | Medium | | |
| 837 | New 21 Game | Medium | | |
| 1230 | Toss Strange Coins | Medium | | |
| 688 | Knight Probability in Chessboard | Medium | | |
| 576 | Out of Boundary Paths | Medium | | |
| 1467 | Probability of a Two Boxes Having The Same Number of Distinct Balls | Hard | | |

---

## 18 — Graph DP
*Shortest paths with constraints, DAG DP, graph-based DP.*

| # | Problem | Difficulty | Solved | Solution |
|---|---------|------------|--------|----------|
| 787 | Cheapest Flights Within K Stops | Medium | | |
| 1334 | Find the City With the Smallest Number of Neighbors at a Threshold Distance | Medium | | |
| 1786 | Number of Restricted Paths From First to Last Node | Medium | | |
| 1976 | Number of Ways to Arrive at Destination | Medium | | |
| 3332 | Maximum Points Tourist Can Earn | Medium | | |
| 3543 | Maximum Weighted K-Edge Path | Medium | | |
| 1548 | The Most Similar Path in a Graph | Hard | | |
| 1857 | Largest Color Value in a Directed Graph | Hard | | |
| 1928 | Minimum Cost to Reach Destination in Time | Hard | | |
| 2050 | Parallel Courses III | Hard | | |
| 2846 | Minimum Edge Weight Equilibrium Queries in a Tree | Hard | | |
| 2858 | Minimum Edge Reversals So Every Node Is Reachable | Hard | | |
| 2876 | Count Visited Nodes in a Directed Graph | Hard | | |
| 2912 | Number of Ways to Reach Destination in the Grid | Hard | | |
| 3530 | Maximum Profit from Valid Topological Order in DAG | Hard | | |
| 3534 | Path Existence Queries in a Graph II | Hard | | |
| 3620 | Network Recovery Pathways | Hard | | |
| 3651 | Minimum Cost Path with Teleportations | Hard | | |
| 2127 | Maximum Employees to Be Invited to a Meeting | Hard | | |
| 568 | Maximum Vacation Days | Hard | | |

---

## 19 — Linear DP
*Simple linear scan DP not fitting other categories — jump games, scheduling, greedy DP.*

| # | Problem | Difficulty | Solved | Solution |
|---|---------|------------|--------|----------|
| 45 | Jump Game II | Medium | Y | [solution](19_linear_dp/solutions/45-jump-game-ii.py) |
| 55 | Jump Game | Medium | Y | [solution](19_linear_dp/solutions/55-jump-game.py) |
| 256 | Paint House | Medium | Y | [solution](19_linear_dp/solutions/256-paint-house.py) |
| 264 | Ugly Number II | Medium | Y | [solution](19_linear_dp/solutions/264-ugly-number-ii.py) |
| 313 | Super Ugly Number | Medium | Y | [solution](19_linear_dp/solutions/313-super-ugly-number.py) |
| 351 | Android Unlock Patterns | Medium | Y | [solution](19_linear_dp/solutions/351-android-unlock-patterns.py) |
| 396 | Rotate Function | Medium | Y | [solution](19_linear_dp/solutions/396-rotate-function.py) |
| 397 | Integer Replacement | Medium | Y | [solution](19_linear_dp/solutions/397-integer-replacement.py) |
| 418 | Sentence Screen Fitting | Medium | | |
| 435 | Non-overlapping Intervals | Medium | Y | [solution](19_linear_dp/solutions/435-non-overlapping-intervals.py) |
| 487 | Max Consecutive Ones II | Medium | | |
| 650 | 2 Keys Keyboard | Medium | | |
| 651 | 4 Keys Keyboard | Medium | | |
| 678 | Valid Parenthesis String | Medium | | |
| 764 | Largest Plus Sign | Medium | | |
| 792 | Number of Matching Subsequences | Medium | | |
| 799 | Champagne Tower | Medium | | |
| 838 | Push Dominoes | Medium | | |
| 898 | Bitwise ORs of Subarrays | Medium | | |
| 1014 | Best Sightseeing Pair | Medium | | |
| 1024 | Video Stitching | Medium | | |
| 1043 | Partition Array for Maximum Sum | Medium | | |
| 1105 | Filling Bookcase Shelves | Medium | | |
| 1387 | Sort Integers by The Power Value | Medium | | |
| 1477 | Find Two Non-overlapping Sub-arrays Each With Target Sum | Medium | | |
| 1493 | Longest Subarray of 1's After Deleting One Element | Medium | | |
| 1524 | Number of Sub-arrays With Odd Sum | Medium | | |
| 1525 | Number of Good Ways to Split a String | Medium | | |
| 1653 | Minimum Deletions to Make String Balanced | Medium | | |
| 1696 | Jump Game VI | Medium | | |
| 1871 | Jump Game VII | Medium | | |
| 1884 | Egg Drop With 2 Eggs and N Floors | Medium | | |
| 1888 | Minimum Number of Flips to Make the Binary String Alternating | Medium | | |
| 1911 | Maximum Alternating Subsequence Sum | Medium | | |
| 1937 | Maximum Number of Points with Cost | Medium | | |
| 1959 | Minimum Total Space Wasted With K Resizing Operations | Medium | | |
| 1997 | First Day Where You Have Been in All the Rooms | Medium | | |
| 2008 | Maximum Earnings From Taxi | Medium | | |
| 2054 | Two Best Non-Overlapping Events | Medium | | |
| 2063 | Vowels of All Substrings | Medium | | |
| 2100 | Find Good Days to Rob the Bank | Medium | | |
| 2140 | Solving Questions With Brainpower | Medium | | |
| 2297 | Jump Game VIII | Medium | | |
| 2310 | Sum of Numbers With Units Digit K | Medium | | |
| 2311 | Longest Binary Subsequence Less Than or Equal to K | Medium | | |
| 2327 | Number of People Aware of a Secret | Medium | | |
| 2369 | Check if There is a Valid Partition For The Array | Medium | | |
| 2380 | Time Needed to Rearrange a Binary String | Medium | | |
| 2420 | Find All Good Indices | Medium | | |
| 2436 | Minimum Split Into Subarrays With GCD Greater Than One | Medium | | |
| 2439 | Minimize Maximum of Array | Medium | | |
| 2464 | Minimum Subarrays in a Valid Split | Medium | | |
| 2495 | Number of Subarrays Having Even Product | Medium | | |
| 2522 | Partition String Into Substrings With Values at Most K | Medium | | |
| 2533 | Number of Good Binary Strings | Medium | | |
| 2560 | House Robber IV | Medium | | |
| 2052 | Minimum Cost to Separate Sentence Into Rows | Medium | | |
| 2571 | Minimum Operations to Reduce an Integer to 0 | Medium | | |
| 2616 | Minimize the Maximum Difference of Pairs | Medium | | |
| 2638 | Count the Number of K-Free Subsets | Medium | | |
| 2712 | Minimum Cost to Make All Characters Equal | Medium | | |
| 2770 | Maximum Number of Jumps to Reach the Last Index | Medium | | |
| 2771 | Longest Non-decreasing Subarray From Two Arrays | Medium | | |
| 2786 | Visit Array Positions to Maximize Score | Medium | | |
| 2811 | Check if it is Possible to Split Array | Medium | | |
| 2830 | Maximize the Profit as the Salesman | Medium | | |
| 2892 | Minimizing Array After Replacing Pairs With Their Product | Medium | | |
| 2896 | Apply Operations to Make Two Strings Equal | Medium | | |
| 2919 | Minimum Increment Operations to Make Array Beautiful | Medium | | |
| 2944 | Minimum Number of Coins for Fruits | Medium | | |
| 2998 | Minimum Number of Operations to Make X and Y Equal | Medium | | |
| 3122 | Minimum Number of Operations to Satisfy Conditions | Medium | | |
| 3147 | Taking Maximum Energy From the Mystic Dungeon | Medium | | |
| 3186 | Maximum Total Damage With Spell Casting | Medium | | |
| 3192 | Minimum Operations to Make Binary Array Elements Equal to One II | Medium | | |
| 3196 | Maximize Total Cost of Alternating Subarrays | Medium | | |
| 3205 | Maximum Array Hopping Score I | Medium | | |
| 3247 | Number of Subsequences with Odd Sum | Medium | | |
| 3290 | Maximum Score of Non-overlapping Intervals | Medium (also: Interval DP) | | |
| 3628 | Maximum Number of Subsequences After One Inserting | Medium | | |
| 3638 | Maximum Balanced Shipments | Medium | | |
| 3654 | Minimum Sum After Divisible Sum Deletions | Medium | | |
| 3660 | Jump Game IX | Medium | | |
| 3685 | Subsequence Sum After Capping Elements | Medium | | |
| 3717 | Minimum Operations to Make the Array Beautiful | Medium | | |
| 3738 | Longest Non-Decreasing Subarray After Replacing at Most One Element | Medium | | |
| 3811 | Number of Alternating XOR Partitions | Medium | | |
| 265 | Paint House II | Hard | Y | [solution](19_linear_dp/solutions/265-paint-house-ii.py) |
| 403 | Frog Jump | Hard | Y | [solution](19_linear_dp/solutions/403-frog-jump.py) |
| 458 | Poor Pigs | Hard | | |
| 465 | Optimal Account Balancing | Hard | | |
| 488 | Zuma Game | Hard | | |
| 514 | Freedom Trail | Hard | | |
| 629 | K Inverse Pairs Array | Hard | | |
| 656 | Coin Path | Hard | | |
| 773 | Sliding Puzzle | Hard | | |
| 801 | Minimum Swaps To Make Sequences Increasing | Hard | | |
| 818 | Race Car | Hard | | |
| 871 | Minimum Number of Refueling Stops | Hard | | |
| 887 | Super Egg Drop | Hard | | |
| 960 | Delete Columns to Make Sorted III | Hard | | |
| 964 | Least Operators to Express Number | Hard | | |
| 975 | Odd Even Jump | Hard | | |
| 1235 | Maximum Profit in Job Scheduling | Hard | | |
| 1262 | Greatest Sum Divisible by Three | Medium | | |
| 1269 | Number of Ways to Stay in the Same Place After Some Steps | Hard | | |
| 1320 | Minimum Distance to Type a Word Using Two Fingers | Hard | | |
| 1326 | Minimum Number of Taps to Open to Water a Garden | Hard | | |
| 1340 | Jump Game V | Hard | | |
| 1363 | Largest Multiple of Three | Hard | | |
| 1388 | Pizza With 3n Slices | Hard | | |
| 1402 | Reducing Dishes | Hard | | |
| 1420 | Build Array Where You Can Find The Maximum Exactly K Comparisons | Hard | | |
| 1425 | Constrained Subsequence Sum | Hard | | |
| 1444 | Number of Ways of Cutting a Pizza | Hard | | |
| 1473 | Paint House III | Hard | | |
| 1526 | Minimum Number of Increments on Subarrays to Form a Target Array | Hard | | |
| 1537 | Get the Maximum Score | Hard | | |
| 1553 | Minimum Number of Days to Eat N Oranges | Hard | | |
| 1575 | Count All Possible Routes | Hard | | |
| 1611 | Minimum One Bit Operations to Make Integers Zero | Hard | | |
| 1687 | Delivering Boxes from Storage to Ports | Hard | | |
| 1714 | Sum Of Special Evenly-Spaced Elements In Array | Hard | | |
| 1751 | Maximum Number of Events That Can Be Attended II | Hard | | |
| 1755 | Closest Subsequence Sum | Hard | | |
| 1770 | Maximum Score from Performing Multiplication Operations | Hard | | |
| 1774 | Closest Dessert Cost | Medium | | |
| 1883 | Minimum Skips to Arrive at Meeting On Time | Hard | | |
| 1896 | Minimum Cost to Change the Final Value of Expression | Hard | | |
| 1994 | The Number of Good Subsets | Hard | | |
| 2035 | Partition Array Into Two Arrays to Minimize Sum Difference | Hard | | |
| 2143 | Choose Numbers From Two Arrays in Range | Hard | | |
| 2152 | Minimum Number of Lines to Cover Points | Medium | | |
| 2163 | Minimum Difference in Sums After Removal of Elements | Hard | | |
| 2167 | Minimum Time to Remove All Cars Containing Illegal Goods | Hard | | |
| 2188 | Minimum Time to Finish the Race | Hard | | |
| 2189 | Number of Ways to Build House of Cards | Medium | | |
| 2209 | Minimum White Tiles After Covering With Carpets | Hard | | |
| 2218 | Maximum Value of K Coins From Piles | Hard | | |
| 2263 | Make Array Non-decreasing or Non-increasing | Hard | | |
| 2289 | Steps to Make Array Non-decreasing | Medium | | |
| 2312 | Selling Pieces of Wood | Hard | | |
| 2355 | Maximum Number of Books You Can Take | Hard | | |
| 2361 | Minimum Costs Using the Train Line | Hard | | |
| 2547 | Minimum Cost to Split an Array | Hard | | |
| 2681 | Power of Heroes | Hard | | |
| 2708 | Maximum Strength of a Group | Medium | | |
| 2809 | Minimum Time to Make Array Sum At Most x | Hard | | |
| 2836 | Maximize Value of Function in a Ball Passing Game | Hard | | |
| 2945 | Find Maximum Non-decreasing Array Length | Hard | | |
| 2969 | Minimum Number of Coins for Fruits II | Hard | | |
| 3018 | Maximum Number of Removal Queries That Can Be Processed I | Hard | | |
| 3082 | Find the Sum of the Power of All Subsequences | Hard | | |
| 3098 | Find the Sum of Subsequence Powers | Hard | | |
| 3117 | Minimum Sum of Values by Dividing Array | Hard | | |
| 3129 | Find All Possible Stable Binary Arrays I | Medium | | |
| 3130 | Find All Possible Stable Binary Arrays II | Hard | | |
| 3154 | Find Number of Ways to Reach the K-th Stair | Hard | | |
| 3180 | Maximum Total Reward Using Operations I | Medium | | |
| 3181 | Maximum Total Reward Using Operations II | Hard | | |
| 3193 | Count the Number of Inversions | Hard | | |
| 3229 | Minimum Operations to Make Array Equal to Target | Hard | | |
| 3269 | Constructing Two Increasing Arrays | Hard | | |
| 3299 | Sum of Consecutive Subsequences | Hard | | |
| 3351 | Sum of Good Subsequences | Hard | | |
| 3389 | Minimum Operations to Make Character Frequencies Equal | Hard | | |
| 3414 | Maximum Score of Non-overlapping Intervals | Hard | | |
| 3428 | Maximum and Minimum Sums of at Most Size K Subsequences | Hard | | |
| 3429 | Paint House IV | Medium | | |
| 3469 | Find Minimum Cost to Remove Array Elements | Medium | | |
| 3500 | Minimum Cost to Divide Array Into Subarrays | Hard | | |
| 3505 | Minimum Operations to Make Elements Within K Subarrays Equal | Hard | | |
| 3524 | Find X Value of Array I | Medium | | |
| 3538 | Merge Operations for Minimum Travel Time | Hard | | |
| 3539 | Find Sum of Array Product of Magical Sequences | Hard | | |
| 3578 | Count Partitions With Max-Min Difference at Most K | Medium | | |
| 3599 | Partition Array to Minimize XOR | Medium | | |
| 3640 | Trionic Array II | Hard | | |
| 3661 | Maximum Walls Destroyed by Robots | Hard | | |
| 3670 | Maximum Product of Two Integers With No Common Bits | Medium | | |
| 3743 | Maximize Cyclic Partition Score | Hard | | |
| 3747 | Count Distinct Integers After Removing Zeros | Medium | | |
| 3826 | Minimum Partition Score | Hard | | |
| 3836 | Maximum Score Using Exactly K Pairs | Hard | | |
| 3857 | Minimum Cost to Split into Ones | Medium | | |

---

## 20 — Prefix / Suffix DP
*Precomputation-based DP on prefix/suffix arrays.*

| # | Problem | Difficulty | Solved | Solution |
|---|---------|------------|--------|----------|
| 42 | Trapping Rain Water | Hard | Y | [solution](20_prefix_suffix_dp/solutions/42-trapping-rain-water.py) |
| 32 | Longest Valid Parentheses | Hard | Y | [solution](20_prefix_suffix_dp/solutions/32-longest-valid-parentheses.py) |
| 361 | Bomb Enemy | Medium | Y | [solution](20_prefix_suffix_dp/solutions/361-bomb-enemy.py) |
| 750 | Number Of Corner Rectangles | Medium | | |
| 828 | Count Unique Characters of All Substrings of a Given String | Hard | | |
| 907 | Sum of Subarray Minimums | Medium | | |
| 1031 | Maximum Sum of Two Non-Overlapping Subarrays | Medium | | |
| 1162 | As Far from Land as Possible | Medium | | |
| 1182 | Shortest Distance to Target Color | Medium | | |
| 2086 | Minimum Number of Food Buckets to Feed the Hamsters | Medium | | |
| 2262 | Total Appeal of A String | Hard | | |
| 2916 | Subarrays Distinct Element Sum of Squares II | Hard | | |
| 638 | Shopping Offers | Medium | | |
| 3218 | Minimum Cost for Cutting Cake I | Medium | | |

---

## Study Tips
- Start with the **Easy/Medium** problems in each pattern to build intuition.
- After solving 2–3 problems in a pattern, try identifying the pattern **before** looking at the solution.
- For Hard problems, first write the recurrence on paper, then code it.
- Problems marked with "(also: X)" have overlap with another pattern — study the dominant approach first, then revisit with the alternate lens.
