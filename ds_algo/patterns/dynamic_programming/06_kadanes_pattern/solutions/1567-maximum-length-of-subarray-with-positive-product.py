"""
1567. Maximum Length of Subarray With Positive Product (Medium)

Pattern: Kadane's Pattern (06)
Approach:
    Track two lengths at each index:
        pos_len: length of longest subarray ending here with positive product
        neg_len: length of longest subarray ending here with negative product

    For each element nums[i]:
        - If nums[i] == 0: reset both to 0.
        - If nums[i] > 0:
            pos_len = pos_len + 1
            neg_len = neg_len + 1 if neg_len > 0 else 0
        - If nums[i] < 0:
            new_pos = neg_len + 1 if neg_len > 0 else 0
            new_neg = pos_len + 1
            pos_len, neg_len = new_pos, new_neg

    Answer: max of all pos_len values.

Complexity:
    Time:  O(n)
    Space: O(1)
"""

from typing import List


class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        """Return the maximum length of a subarray with positive product."""
        pos_len = 0
        neg_len = 0
        ans = 0

        for num in nums:
            if num == 0:
                pos_len = 0
                neg_len = 0
            elif num > 0:
                pos_len += 1
                neg_len = neg_len + 1 if neg_len > 0 else 0
            else:  # num < 0
                new_pos = neg_len + 1 if neg_len > 0 else 0
                new_neg = pos_len + 1
                pos_len, neg_len = new_pos, new_neg
            ans = max(ans, pos_len)

        return ans


# ---------- Tests ----------
import unittest


class TestMaxLenPositiveProduct(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        self.assertEqual(self.sol.getMaxLen([1, -2, -3, 4]), 4)

    def test_example2(self):
        self.assertEqual(self.sol.getMaxLen([0, 1, -2, -3, -4]), 3)

    def test_example3(self):
        self.assertEqual(self.sol.getMaxLen([-1, -2, -3, 0, 1]), 2)

    def test_all_positive(self):
        self.assertEqual(self.sol.getMaxLen([1, 2, 3, 4]), 4)

    def test_single_negative(self):
        self.assertEqual(self.sol.getMaxLen([-1]), 0)

    def test_two_negatives(self):
        self.assertEqual(self.sol.getMaxLen([-1, -2]), 2)

    def test_zeros_split(self):
        self.assertEqual(self.sol.getMaxLen([1, 0, 1, 0, 1]), 1)

    def test_all_zeros(self):
        self.assertEqual(self.sol.getMaxLen([0, 0, 0]), 0)

    def test_negative_positive_mix(self):
        self.assertEqual(self.sol.getMaxLen([5, -20, -20, -6, -5, 1]), 6)


if __name__ == "__main__":
    unittest.main()
