"""
2266. Count Number of Texts (Medium)
https://leetcode.com/problems/count-number-of-texts/

Pattern: String DP

Alice sends a text message using an old phone keypad. Each letter maps to
pressing a digit 1-4 times (digits 7 and 9 allow 4 presses; others allow 3).
Given the pressed keys string, return the number of possible messages mod 10^9+7.

Approach:
    Similar to Decode Ways. Process consecutive groups of the same digit.
    For each group of length L with max_press p (3 or 4):
      dp[i] = dp[i-1] + dp[i-2] + ... + dp[i-p]
    This is a linear recurrence within each group. We can compute across the
    whole string in one pass by only combining within runs of the same digit.

    Simpler single-pass: dp[i] = number of ways for pressedKeys[0..i-1].
    For position i, look back at positions i-1, i-2, ..., i-p as long as
    the digit matches pressedKeys[i-1].

Time:  O(n)  -- each position checks at most 4 predecessors.
Space: O(n)
"""

MOD = 10**9 + 7


class Solution:
    def countTexts(self, pressedKeys: str) -> int:
        """Return the number of possible text messages modulo 10^9 + 7."""
        n = len(pressedKeys)
        dp = [0] * (n + 1)
        dp[0] = 1

        for i in range(1, n + 1):
            digit = pressedKeys[i - 1]
            max_press = 4 if digit in ('7', '9') else 3

            for k in range(1, max_press + 1):
                j = i - k
                if j < 0:
                    break
                if pressedKeys[j] != digit:
                    break
                dp[i] = (dp[i] + dp[j]) % MOD

        return dp[n]


# ---------- Tests ----------
import unittest


class TestCountTexts(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        self.assertEqual(self.sol.countTexts("22233"), 8)

    def test_example2(self):
        self.assertEqual(self.sol.countTexts("222222222222222222222222222222222222"), 82876089)

    def test_single_digit(self):
        self.assertEqual(self.sol.countTexts("2"), 1)

    def test_two_same(self):
        self.assertEqual(self.sol.countTexts("22"), 2)

    def test_three_same(self):
        # "222" -> "aaa", "ab", "ba", "c" = 4 ways
        self.assertEqual(self.sol.countTexts("222"), 4)

    def test_four_presses_digit_7(self):
        # "7777" -> 4 presses allowed: like tribonacci+1
        # dp[0]=1, dp[1]=1, dp[2]=2, dp[3]=4, dp[4]=8
        self.assertEqual(self.sol.countTexts("7777"), 8)

    def test_different_digits(self):
        # "23" -> each is one press, only 1 way
        self.assertEqual(self.sol.countTexts("23"), 1)

    def test_mixed(self):
        # "227" -> "22" has 2 ways, "7" has 1 way -> 2
        self.assertEqual(self.sol.countTexts("227"), 2)


if __name__ == "__main__":
    unittest.main()
