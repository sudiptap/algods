"""
198. House Robber (Medium)

Pattern: Fibonacci Pattern (01)
Approach:
    At each house i, choose max of:
        - Skip house i: keep dp[i-1]
        - Rob house i:  dp[i-2] + nums[i]
    dp[i] = max(dp[i-1], dp[i-2] + nums[i])
    Optimize to O(1) space with two variables (prev2, prev1).

Complexity:
    Time:  O(n)
    Space: O(1)
"""

from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        prev2, prev1 = 0, 0
        for num in nums:
            prev2, prev1 = prev1, max(prev1, prev2 + num)
        return prev1


# ---------- Tests ----------
import unittest


class TestRob(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        self.assertEqual(self.sol.rob([1, 2, 3, 1]), 4)

    def test_example2(self):
        self.assertEqual(self.sol.rob([2, 7, 9, 3, 1]), 12)

    def test_single(self):
        self.assertEqual(self.sol.rob([5]), 5)

    def test_two(self):
        self.assertEqual(self.sol.rob([2, 3]), 3)

    def test_empty(self):
        self.assertEqual(self.sol.rob([]), 0)

    def test_all_same(self):
        self.assertEqual(self.sol.rob([3, 3, 3, 3]), 6)

    def test_large_values(self):
        self.assertEqual(self.sol.rob([100, 1, 1, 100]), 200)


if __name__ == "__main__":
    unittest.main()
