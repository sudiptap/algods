"""
2167. Minimum Time to Remove All Cars Containing Illegal Goods (Hard)
https://leetcode.com/problems/minimum-time-to-remove-all-cars-containing-illegal-goods/

Given binary string s, remove all '1's. Cost: remove from left end = 1,
remove from right end = 1, remove from middle = 2. Minimize total cost.

Pattern: Linear DP (Prefix/Suffix)
Approach:
- left[i] = min cost to remove all 1s in s[0..i] using only left-end
  removals (cost i+1) or middle removals (cost 2 each).
- right[i] = min cost to remove all 1s in s[i..n-1] similarly from right.
- left[i] = min(left[i-1] + 2*s[i], i+1) — either remove s[i] from
  middle (cost 2 if s[i]='1') plus left[i-1], or remove everything
  up to i from left end (cost i+1).
- Similarly for right.
- Answer = min over split of left[i] + right[i+1].

Time:  O(n)
Space: O(n), reducible to O(1)
"""


class Solution:
    def minimumTime(self, s: str) -> int:
        """Return minimum time to remove all illegal cars.

        Args:
            s: Binary string where '1' means illegal.

        Returns:
            Minimum removal cost.
        """
        n = len(s)

        # left[i] = min cost to clear all 1s in s[0..i]
        left = [0] * n
        left[0] = int(s[0])  # either remove from left (cost 1) or skip if '0'
        for i in range(1, n):
            if s[i] == '0':
                left[i] = left[i - 1]
            else:
                left[i] = min(left[i - 1] + 2, i + 1)

        # right[i] = min cost to clear all 1s in s[i..n-1]
        right = [0] * n
        right[n - 1] = int(s[n - 1])
        for i in range(n - 2, -1, -1):
            if s[i] == '0':
                right[i] = right[i + 1]
            else:
                right[i] = min(right[i + 1] + 2, n - i)

        # Try all splits
        ans = min(right[0], left[n - 1])  # all from right, or all from left
        for i in range(n - 1):
            ans = min(ans, left[i] + right[i + 1])

        return ans


# ---------- tests ----------
def test_minimum_time():
    sol = Solution()

    # Example 1: "1100101" -> 5
    assert sol.minimumTime("1100101") == 5

    # Example 2: "0010" -> 2
    assert sol.minimumTime("0010") == 2

    # All zeros
    assert sol.minimumTime("0000") == 0

    # All ones
    assert sol.minimumTime("111") == 3

    # Single char
    assert sol.minimumTime("1") == 1
    assert sol.minimumTime("0") == 0

    print("All tests passed for 2167. Minimum Time to Remove All Cars")


if __name__ == "__main__":
    test_minimum_time()
