"""
233. Number of Digit One (Hard)

Pattern: Digit DP
Approach:
    Math-based counting of the contribution of each digit position.

    For each position (ones, tens, hundreds, ...) with place value = 10^k,
    split n into:
        high = n // (place * 10)   -- digits above current position
        cur  = (n // place) % 10   -- current digit
        low  = n % place           -- digits below current position

    Count of 1s at this position:
        if cur == 0:  high * place
        if cur == 1:  high * place + (low + 1)
        if cur >= 2:  (high + 1) * place

    Sum across all positions.

Complexity:
    Time:  O(log n)  -- one pass per digit
    Space: O(1)
"""


class Solution:
    def countDigitOne(self, n: int) -> int:
        if n <= 0:
            return 0

        count = 0
        place = 1  # 1, 10, 100, ...

        while place <= n:
            high = n // (place * 10)
            cur = (n // place) % 10
            low = n % place

            if cur == 0:
                count += high * place
            elif cur == 1:
                count += high * place + (low + 1)
            else:
                count += (high + 1) * place

            place *= 10

        return count


# ---------- Tests ----------
def test():
    sol = Solution()

    # Example 1: 1 -> 1 (just "1")
    assert sol.countDigitOne(1) == 1

    # Example 2: 13 -> 1,10,11,12,13 => ones digit: 1,11 = 2; tens digit: 10,11,12,13 = 4 => 6
    assert sol.countDigitOne(13) == 6, f"Expected 6, got {sol.countDigitOne(13)}"

    # n = 0
    assert sol.countDigitOne(0) == 0

    # n = 10: 1,10 => 1 appears in {1,10,11...} but n=10: 1,10 => count ones in 1..10
    # 1: 1; 10: 1 => total 2
    assert sol.countDigitOne(10) == 2

    # n = 100
    assert sol.countDigitOne(100) == 21

    # Large value
    assert sol.countDigitOne(1000000000) == 900000001

    # n = -1
    assert sol.countDigitOne(-1) == 0

    print("All tests passed!")


if __name__ == "__main__":
    test()
