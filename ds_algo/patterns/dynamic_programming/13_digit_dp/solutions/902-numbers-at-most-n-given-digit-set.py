"""
902. Numbers At Most N Given Digit Set (Hard)
https://leetcode.com/problems/numbers-at-most-n-given-digit-set/

Given an array of string digits and an integer n, return the number of positive
integers that can be formed using only the given digits and are <= n.

Pattern: Digit DP
Approach:
- Count numbers with fewer digits than n: for k digits (k < len(str(n))),
  there are len(digits)^k choices.
- Count numbers with same number of digits as n using digit DP:
  go digit by digit. If we place a digit < n's digit, remaining positions
  are free (len(digits)^remaining). If equal, continue to next position.

Time:  O(len(str(n)) * len(digits))
Space: O(1) beyond the digit string.
"""

from typing import List


class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        """Return count of numbers <= n formable from given digits.

        Args:
            digits: Sorted list of digit strings from '1' to '9'.
            n: Upper bound, 1 <= n <= 10^9.

        Returns:
            Count of valid numbers.
        """
        s = str(n)
        num_len = len(s)
        d = len(digits)
        ans = 0

        # Count numbers with fewer digits: d^1 + d^2 + ... + d^(num_len-1)
        for k in range(1, num_len):
            ans += d ** k

        # Count numbers with exactly num_len digits that are <= n
        for i, ch in enumerate(s):
            # Count digits strictly less than ch
            less = sum(1 for dig in digits if dig < ch)
            ans += less * (d ** (num_len - 1 - i))

            # If ch is not in digits, we can't continue (no equal digit to place)
            if ch not in digits:
                break
        else:
            # All digits of n matched exactly -> n itself is valid
            ans += 1

        return ans


# ---------- tests ----------
def test_at_most_n_given_digit_set():
    sol = Solution()

    # Example 1: digits=["1","3","5","7"], n=100
    # 1-digit: 4, 2-digit: 16, 3-digit (<=100): "1"+"1..7"+"1..7" but <=100
    # only 11,13,15,17 -> total 4+16+4 = 20? Let's verify.
    # Actually: 3-digit numbers starting with "1": 1xx where x in {1,3,5,7}
    # "1" < "1" -> 0 less. "1" == "1", continue.
    # "0" not in digits, break. So 0 three-digit numbers from tight.
    # Wait n=100, s="100". digit 0: '1' in digits. digit 1: '0' not in digits.
    # less than '0' = 0. break. So ans = 4 + 16 = 20.
    assert sol.atMostNGivenDigitSet(["1", "3", "5", "7"], 100) == 20

    # Example 2: digits=["1","4","9"], n=1000000000
    assert sol.atMostNGivenDigitSet(["1", "4", "9"], 1000000000) == 29523

    # Example 3: digits=["7"], n=8 -> just "7" -> 1
    assert sol.atMostNGivenDigitSet(["7"], 8) == 1

    # Single digit, n matches
    assert sol.atMostNGivenDigitSet(["3"], 3) == 1

    # digits=["1","2"], n=21 -> 1-digit: 2, 2-digit: "11","12","21" = 3. Total 5.
    assert sol.atMostNGivenDigitSet(["1", "2"], 21) == 5

    print("All tests passed for 902. Numbers At Most N Given Digit Set")


if __name__ == "__main__":
    test_at_most_n_given_digit_set()
