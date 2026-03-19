"""
1012. Numbers With Repeated Digits (Hard)

Pattern: 13_digit_dp
- Count numbers in [1, n] that have at least one repeated digit.

Approach:
- count_with_repeated = n - count_unique_digits(n).
- count_unique_digits(n): use digit DP on the digits of n.
  - For numbers with fewer digits than n: count permutations of d digits with
    all unique, choosing from 1-9 for first digit, then remaining for rest.
  - For numbers with same number of digits as n: iterate digit by digit, tracking
    tight bound and which digits have been used (bitmask or set).

Complexity:
- Time:  O(10 * 2^10 * d) where d = number of digits, but simplified to O(d * 10)
  with the combinatorial counting approach
- Space: O(d)
"""


class Solution:
    def numDupDigitsAtMostN(self, n: int) -> int:
        # n - count of numbers with all unique digits in [1, n]
        digits = [int(c) for c in str(n)]
        k = len(digits)

        # Count numbers with all unique digits

        # Helper: permutation P(m, r) = m * (m-1) * ... * (m-r+1)
        def perm(m, r):
            result = 1
            for i in range(r):
                result *= (m - i)
            return result

        # 1) Count numbers with fewer digits (1 to k-1 digits), all unique
        count = 0
        for d in range(1, k):
            # first digit: 9 choices (1-9), remaining d-1 digits from 9 remaining
            count += 9 * perm(9, d - 1)

        # 2) Count numbers with exactly k digits <= n, all unique
        used = set()
        for i, d in enumerate(digits):
            # Try digits smaller than d at position i
            start = 0 if i > 0 else 1
            for smaller in range(start, d):
                if smaller not in used:
                    # remaining positions: k - i - 1 digits from (10 - i - 1) unused
                    count += perm(10 - i - 1, k - i - 1)

            if d in used:
                break
            used.add(d)

            if i == k - 1:
                # n itself has all unique digits
                count += 1

        return n - count


# ---------- Tests ----------
def test():
    sol = Solution()

    # Example 1: n=20 -> 1 (only 11 has repeated digits)
    assert sol.numDupDigitsAtMostN(20) == 1

    # Example 2: n=100 -> 10 (11,22,33,44,55,66,77,88,99,100... wait 100 has no repeat)
    assert sol.numDupDigitsAtMostN(100) == 10

    # Example 3: n=1000
    assert sol.numDupDigitsAtMostN(1000) == 262

    # n=1: no repeated digits possible
    assert sol.numDupDigitsAtMostN(1) == 0

    # n=11: just 11
    assert sol.numDupDigitsAtMostN(11) == 1

    print("All tests passed!")


if __name__ == "__main__":
    test()
