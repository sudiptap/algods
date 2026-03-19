"""
2100. Find Good Days to Rob the Bank (Medium)
https://leetcode.com/problems/find-good-days-to-rob-the-bank/

Day i is good if security[i-time..i] is non-increasing and
security[i..i+time] is non-decreasing. Return all good days sorted.

Pattern: Linear DP (Prefix/Suffix Arrays)
Approach:
- dec[i] = length of non-increasing run ending at i.
- inc[i] = length of non-decreasing run starting at i.
- Day i is good if dec[i] >= time and inc[i] >= time.

Time:  O(n)
Space: O(n)
"""

from typing import List


class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        """Return sorted list of good days to rob the bank.

        Args:
            security: Security values per day.
            time: Required number of days before and after.

        Returns:
            List of good day indices.
        """
        n = len(security)
        # dec[i] = how many consecutive non-increasing days ending at i (excluding i itself)
        dec = [0] * n
        for i in range(1, n):
            if security[i] <= security[i - 1]:
                dec[i] = dec[i - 1] + 1

        # inc[i] = how many consecutive non-decreasing days starting at i (excluding i itself)
        inc = [0] * n
        for i in range(n - 2, -1, -1):
            if security[i] <= security[i + 1]:
                inc[i] = inc[i + 1] + 1

        return [i for i in range(n) if dec[i] >= time and inc[i] >= time]


# ---------- tests ----------
def test_good_days():
    sol = Solution()

    # Example 1
    assert sol.goodDaysToRobBank([5,3,3,3,5,6,2], 2) == [2, 3]

    # Example 2
    assert sol.goodDaysToRobBank([1,1,1,1,1], 0) == [0, 1, 2, 3, 4]

    # Example 3
    assert sol.goodDaysToRobBank([1,2,3,4,5,6], 2) == []

    # Single day
    assert sol.goodDaysToRobBank([1], 0) == [0]

    print("All tests passed for 2100. Find Good Days to Rob the Bank")


if __name__ == "__main__":
    test_good_days()
