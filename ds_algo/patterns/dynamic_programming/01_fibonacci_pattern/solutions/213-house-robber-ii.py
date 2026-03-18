"""
213. House Robber II (Medium)

Pattern: Fibonacci Pattern (01)
Approach:
    Houses form a circle, so house 0 and house n-1 are adjacent.
    Break the circular constraint by running House Robber twice:
        1. nums[0 : n-1]  (include first, exclude last)
        2. nums[1 : n]    (exclude first, include last)
    Answer = max of both runs.

Complexity:
    Time:  O(n)
    Space: O(1)
"""

from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums) if nums else 0

        def rob_linear(houses: List[int]) -> int:
            prev2, prev1 = 0, 0
            for h in houses:
                prev2, prev1 = prev1, max(prev1, prev2 + h)
            return prev1

        return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))


# ---------- Tests ----------
import unittest


class TestRobII(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        self.assertEqual(self.sol.rob([2, 3, 2]), 3)

    def test_example2(self):
        self.assertEqual(self.sol.rob([1, 2, 3, 1]), 4)

    def test_example3(self):
        self.assertEqual(self.sol.rob([1, 2, 3]), 3)

    def test_single(self):
        self.assertEqual(self.sol.rob([5]), 5)

    def test_two(self):
        self.assertEqual(self.sol.rob([2, 3]), 3)

    def test_empty(self):
        self.assertEqual(self.sol.rob([]), 0)

    def test_all_same(self):
        # Circle of 4 houses each worth 3: rob 2 non-adjacent = 6
        self.assertEqual(self.sol.rob([3, 3, 3, 3]), 6)

    def test_large_values(self):
        # [100, 1, 1, 100]: circular so can't take both 100s -> max(rob([100,1,1]), rob([1,1,100])) = 101
        self.assertEqual(self.sol.rob([100, 1, 1, 100]), 101)


if __name__ == "__main__":
    unittest.main()
