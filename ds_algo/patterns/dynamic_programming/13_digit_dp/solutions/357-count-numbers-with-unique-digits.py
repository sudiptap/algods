"""
357. Count Numbers with Unique Digits (Medium)

Given an integer n, return the count of all numbers with unique digits x
where 0 <= x < 10^n.

Approach (combinatorial math):
- For n = 0: only 0, answer = 1.
- For k-digit numbers (k >= 1):
  - First digit: 9 choices (1-9, cannot be 0).
  - Second digit: 9 choices (0-9 minus the first digit).
  - Third digit: 8 choices, fourth: 7, etc.
  - count_k = 9 * 9 * 8 * 7 * ... * (10 - k + 1)
- Answer = 1 + sum of count_k for k = 1..n.
- For n >= 11 there are no valid numbers with 11+ unique digits (only 10
  distinct digits exist), so cap at n = 10.

Time:  O(n), practically O(1) since n <= 10.
Space: O(1)
"""


class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        """Count numbers in [0, 10^n) with all unique digits."""
        if n == 0:
            return 1

        n = min(n, 10)  # beyond 10 digits, no new unique-digit numbers
        total = 1  # count 0
        for k in range(1, n + 1):
            # k-digit numbers with unique digits
            product = 9  # first digit: 1-9
            for i in range(1, k):
                product *= (10 - i)  # remaining digits
            total += product
        return total


# ---------- Tests ----------

def test_n0():
    sol = Solution()
    assert sol.countNumbersWithUniqueDigits(0) == 1  # only 0

def test_n1():
    sol = Solution()
    assert sol.countNumbersWithUniqueDigits(1) == 10  # 0-9

def test_n2():
    sol = Solution()
    # 10 (1-digit) + 81 (2-digit with unique) = 91
    assert sol.countNumbersWithUniqueDigits(2) == 91

def test_n3():
    sol = Solution()
    assert sol.countNumbersWithUniqueDigits(3) == 739

def test_n4():
    sol = Solution()
    assert sol.countNumbersWithUniqueDigits(4) == 5275

def test_n8():
    sol = Solution()
    assert sol.countNumbersWithUniqueDigits(8) == 2345851

def test_large_n():
    sol = Solution()
    # n=10 and n=100 should give the same result (cap at 10 digits)
    result_10 = sol.countNumbersWithUniqueDigits(10)
    result_100 = sol.countNumbersWithUniqueDigits(100)
    assert result_10 == result_100
    assert result_10 == 8877691


if __name__ == "__main__":
    test_n0()
    test_n1()
    test_n2()
    test_n3()
    test_n4()
    test_n8()
    test_large_n()
    print("All tests passed!")
