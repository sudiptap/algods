"""
1888. Minimum Number of Flips to Make the Binary String Alternating (Medium)
https://leetcode.com/problems/minimum-number-of-flips-to-make-the-binary-string-alternating/

Given binary string s, you can: (Type-1) remove first char and append to end,
(Type-2) flip any char. Return min Type-2 ops to make s alternating.

Pattern: Linear DP / Sliding Window
Approach:
- Type-1 ops are rotations. Consider all rotations by doubling the string.
- For target "010101..." and "101010...", count mismatches in a sliding
  window of length n over the doubled string.
- Maintain running mismatch count, slide window, track minimum.

Time:  O(n)
Space: O(n) for the doubled string
"""


class Solution:
    def minFlips(self, s: str) -> int:
        """Return min flips to make s alternating after optional rotations.

        Args:
            s: Binary string.

        Returns:
            Minimum number of type-2 flips.
        """
        n = len(s)
        doubled = s + s
        # Target patterns of length 2n
        t0 = ''.join('0' if i % 2 == 0 else '1' for i in range(2 * n))
        t1 = ''.join('1' if i % 2 == 0 else '0' for i in range(2 * n))

        ans = n
        diff0 = diff1 = 0

        for i in range(2 * n):
            if doubled[i] != t0[i]:
                diff0 += 1
            if doubled[i] != t1[i]:
                diff1 += 1
            # Remove leftmost element when window exceeds n
            if i >= n:
                if doubled[i - n] != t0[i - n]:
                    diff0 -= 1
                if doubled[i - n] != t1[i - n]:
                    diff1 -= 1
            # Window is full
            if i >= n - 1:
                ans = min(ans, diff0, diff1)

        return ans


# ---------- tests ----------
def test_min_flips():
    sol = Solution()

    # Example 1: "111000" -> rotate to "100011" then flip -> 2
    assert sol.minFlips("111000") == 1

    # Example 2
    assert sol.minFlips("010") == 0

    # Example 3
    assert sol.minFlips("1110") == 1

    # Already alternating
    assert sol.minFlips("01") == 0
    assert sol.minFlips("10") == 0

    # Single char
    assert sol.minFlips("0") == 0

    # All same
    assert sol.minFlips("0000") == 2

    print("All tests passed for 1888. Minimum Number of Flips to Make Binary String Alternating")


if __name__ == "__main__":
    test_min_flips()
