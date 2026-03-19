"""
1067. Digit Count in Range (Hard)

Pattern: 13_digit_dp
- Count occurrences of digit d in all integers in range [low, high].

Approach:
- count(n, d) = total occurrences of digit d in [1, n].
- Answer = count(high, d) - count(low - 1, d).
- For count(n, d): iterate over each digit position. For position p (ones=0, tens=1, ...):
  - Let higher = n // (10^(p+1)), cur = (n // 10^p) % 10, lower = n % 10^p.
  - If d > 0:
    - If cur < d: contribution = higher * 10^p
    - If cur == d: contribution = higher * 10^p + lower + 1
    - If cur > d: contribution = (higher + 1) * 10^p
  - If d == 0:
    - Same but higher is reduced by 1 (leading zeros don't count):
    - If cur < d(impossible for d=0 except cur=0): = (higher - 1) * 10^p + lower + 1 when cur==0
    - If cur > 0: = higher * 10^p

Complexity:
- Time:  O(log n) per count call
- Space: O(1)
"""


class Solution:
    def digitsCount(self, d: int, low: int, high: int) -> int:
        return self._count(high, d) - self._count(low - 1, d)

    def _count(self, n: int, d: int) -> int:
        """Count occurrences of digit d in [1, n]."""
        if n <= 0:
            return 0

        result = 0
        power = 1  # 10^p
        while power <= n:
            higher = n // (power * 10)
            cur = (n // power) % 10
            lower = n % power

            if d == 0:
                # For d=0, leading zeros shouldn't count, so higher starts 1 less
                if cur == 0:
                    result += (higher - 1) * power + lower + 1
                elif cur > 0:
                    result += higher * power
            else:
                if cur < d:
                    result += higher * power
                elif cur == d:
                    result += higher * power + lower + 1
                else:
                    result += (higher + 1) * power

            power *= 10

        return result


# ---------- Tests ----------
def test():
    sol = Solution()

    # Example 1: d=1, low=1, high=13 -> 1,10,11(twice),12,13 = 6
    assert sol.digitsCount(1, 1, 13) == 6

    # Example 2: d=3, low=100, high=250 -> 103,113,123,130-139(11),143,...
    assert sol.digitsCount(3, 100, 250) == 35

    # Single number containing digit
    assert sol.digitsCount(5, 5, 5) == 1

    # Single number not containing digit
    assert sol.digitsCount(5, 3, 3) == 0

    # d=0, low=1, high=100 -> count of 0s: 10,20,...,90 (one each)=9, 100(two 0s)=2 => 11
    assert sol.digitsCount(0, 1, 100) == 11

    print("All tests passed!")


if __name__ == "__main__":
    test()
