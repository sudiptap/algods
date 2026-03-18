"""
2585. Number of Ways to Earn Points
https://leetcode.com/problems/number-of-ways-to-earn-points/

Pattern: 03 - Unbounded Knapsack (Bounded variant)

---
APPROACH: Bounded Knapsack DP
- Each question type i has count[i] questions each worth marks[i] points.
- We want the number of ways to earn exactly `target` points.
- dp[j] = number of ways to earn exactly j points using question types seen so far.
- For each type i, iterate j from target down to 0, and for each j try taking
  k = 0..count[i] questions (as long as k * marks[i] <= j).
- We process types in outer loop (like 0/1 knapsack style) to avoid reuse
  beyond count[i].
- Since we can take multiple of the same type (up to count[i]), we enumerate k.

Time:  O(n * target * max_count)
Space: O(target)
---
"""

from typing import List

MOD = 10**9 + 7


class Solution:
    def waysToReachTarget(self, target: int, types: List[List[int]]) -> int:
        """Return the number of ways to earn exactly target points.

        types[i] = [count_i, marks_i]: up to count_i questions each worth marks_i.
        """
        dp = [0] * (target + 1)
        dp[0] = 1

        for count, marks in types:
            # Traverse in reverse to treat each type independently
            for j in range(target, -1, -1):
                # Try taking k = 1..count questions of this type
                for k in range(1, count + 1):
                    cost = k * marks
                    if cost > j:
                        break
                    dp[j] = (dp[j] + dp[j - cost]) % MOD

        return dp[target]


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    # Example 1
    assert sol.waysToReachTarget(6, [[6, 1], [3, 2], [2, 3]]) == 7
    # Example 2
    assert sol.waysToReachTarget(5, [[50, 1], [50, 2], [50, 5]]) == 4
    # Example 3
    assert sol.waysToReachTarget(18, [[6, 1], [3, 2], [2, 3]]) == 1
    # Single type, exact match
    assert sol.waysToReachTarget(4, [[2, 2]]) == 1
    # Target 0
    assert sol.waysToReachTarget(0, [[5, 1]]) == 1
    # Impossible
    assert sol.waysToReachTarget(3, [[1, 2]]) == 0

    print("Solution: all tests passed")
