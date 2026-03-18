"""
338. Counting Bits (Easy)

Given an integer n, return an array ans of length n+1 such that ans[i] is
the number of 1-bits in the binary representation of i.

Approach:
    dp[i] = dp[i >> 1] + (i & 1)
    The number of set bits in i equals the number of set bits in i//2
    plus whether i is odd.

    Alternative: dp[i] = dp[i & (i-1)] + 1  (clear lowest set bit)

Time:  O(n)
Space: O(n) for output (O(1) extra)
"""

from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        """Return list where index i contains the count of 1-bits in i."""
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            dp[i] = dp[i >> 1] + (i & 1)
        return dp


# ---------- Tests ----------

def test():
    s = Solution()

    assert s.countBits(2) == [0, 1, 1]
    assert s.countBits(5) == [0, 1, 1, 2, 1, 2]
    assert s.countBits(0) == [0]
    assert s.countBits(1) == [0, 1]
    assert s.countBits(8) == [0, 1, 1, 2, 1, 2, 2, 3, 1]

    # Verify against bin().count('1')
    n = 100
    result = s.countBits(n)
    for i in range(n + 1):
        assert result[i] == bin(i).count('1'), f"Mismatch at {i}"

    print("All tests passed!")


if __name__ == "__main__":
    test()
