"""
1578. Minimum Time to Make Rope Colorful (Medium)

Pattern: Fibonacci Pattern (01)
Approach:
    For each group of consecutive balloons with the same color, we must
    remove all but the one with the highest neededTime.

    Greedily scan left to right. When colors[i] == colors[i-1], we are in
    a consecutive group. Track the max cost in the group and accumulate
    the sum. The removal cost for the group = sum - max.

Complexity:
    Time:  O(n)
    Space: O(1)
"""

from typing import List


class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        """Return the minimum time to make the rope colorful (no two adjacent same color)."""
        total = 0
        group_max = neededTime[0]
        group_sum = neededTime[0]

        for i in range(1, len(colors)):
            if colors[i] == colors[i - 1]:
                group_sum += neededTime[i]
                group_max = max(group_max, neededTime[i])
            else:
                total += group_sum - group_max
                group_sum = neededTime[i]
                group_max = neededTime[i]

        total += group_sum - group_max
        return total


# ---------- Tests ----------
import unittest


class TestMinCostColorful(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        self.assertEqual(self.sol.minCost("abaac", [1, 2, 3, 4, 5]), 3)

    def test_example2(self):
        self.assertEqual(self.sol.minCost("abc", [1, 2, 3]), 0)

    def test_example3(self):
        self.assertEqual(self.sol.minCost("aabaa", [1, 2, 3, 4, 1]), 2)

    def test_all_same(self):
        self.assertEqual(self.sol.minCost("aaaa", [1, 2, 3, 4]), 6)

    def test_single(self):
        self.assertEqual(self.sol.minCost("a", [5]), 0)

    def test_two_same(self):
        self.assertEqual(self.sol.minCost("aa", [3, 7]), 3)

    def test_alternating(self):
        self.assertEqual(self.sol.minCost("ababab", [1, 2, 3, 4, 5, 6]), 0)

    def test_multiple_groups(self):
        self.assertEqual(self.sol.minCost("aabbc", [1, 3, 2, 4, 5]), 3)


if __name__ == "__main__":
    unittest.main()
