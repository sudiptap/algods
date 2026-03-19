"""
956. Tallest Billboard (Hard)
https://leetcode.com/problems/tallest-billboard/

Given an array of rods, find the largest possible height of a billboard
installation. A billboard requires two steel supports of equal height.
You can weld rods together; unused rods are allowed. Return 0 if impossible.

Pattern: 0/1 Knapsack
Approach:
- dp[diff] = maximum height of the taller support when the difference between
  the two supports is exactly diff.
- For each rod, we can: skip it, add to taller support, or add to shorter support.
- Base case: dp[0] = 0 (both supports empty, height 0).
- For each rod r, update dp considering all three choices.
- Answer: dp[0] at the end.

Time:  O(n * S) where S = sum of all rods.
Space: O(S)
"""

from typing import List


class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        """Return tallest billboard height using equal-height supports.

        Args:
            rods: Array of rod lengths, 1 <= len(rods) <= 20, 1 <= rods[i] <= 1000.

        Returns:
            Maximum height of equal-height supports, or 0 if impossible.
        """
        # dp[diff] = max height of taller rod with given difference
        dp = {0: 0}

        for r in rods:
            new_dp = dict(dp)  # skip this rod
            for diff, taller in dp.items():
                shorter = taller - diff

                # Add rod to taller support
                new_diff = diff + r
                new_taller = taller + r
                if new_diff not in new_dp or new_dp[new_diff] < new_taller:
                    new_dp[new_diff] = new_taller

                # Add rod to shorter support
                new_diff2 = abs(diff - r)
                if diff >= r:
                    # Shorter + r still <= taller, taller stays same
                    new_taller2 = taller
                else:
                    # Shorter + r > taller, so new taller = shorter + r
                    new_taller2 = shorter + r
                if new_diff2 not in new_dp or new_dp[new_diff2] < new_taller2:
                    new_dp[new_diff2] = new_taller2

            dp = new_dp

        return dp.get(0, 0)


# ---------- tests ----------
def test_tallest_billboard():
    sol = Solution()

    # Example 1: [1,2,3,6] -> supports of height 6 (6 and 1+2+3)
    assert sol.tallestBillboard([1, 2, 3, 6]) == 6

    # Example 2: [1,2,3,4,5,6] -> supports of height 10 (e.g., 4+6 and 1+2+3+4? No)
    # 1+2+3+4+5+6 = 21. Half = 10.5. So max equal = 10 (e.g., 4+6=10, 1+2+3+4=10? 1+2+3+4=10)
    # Actually 1+4+5=10, 4+6=10. Wait, can't reuse rod 4.
    # 5+6-1=10? Not how it works. Let me just trust the expected: 10
    assert sol.tallestBillboard([1, 2, 3, 4, 5, 6]) == 10

    # Example 3: [1,2] -> can't make equal supports
    assert sol.tallestBillboard([1, 2]) == 0

    # Single rod: can't split
    assert sol.tallestBillboard([5]) == 0

    # Two equal rods
    assert sol.tallestBillboard([5, 5]) == 5

    # Empty (edge case)
    assert sol.tallestBillboard([]) == 0

    print("All tests passed for 956. Tallest Billboard")


if __name__ == "__main__":
    test_tallest_billboard()
