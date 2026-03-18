"""
264. Ugly Number II (Medium)

Pattern: 19_linear_dp
    Build the sequence of ugly numbers in order using three pointers.

Approach:
    Maintain three pointers i2, i3, i5 into the dp array.
    At each step, the next ugly number is min(dp[i2]*2, dp[i3]*3, dp[i5]*5).
    Advance whichever pointer(s) produced the minimum (handle duplicates by
    advancing all that match).

Complexity:
    Time:  O(n) - single pass to build n ugly numbers.
    Space: O(n) - store all n ugly numbers.
"""


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp = [0] * n
        dp[0] = 1
        i2 = i3 = i5 = 0

        for i in range(1, n):
            next2, next3, next5 = dp[i2] * 2, dp[i3] * 3, dp[i5] * 5
            dp[i] = min(next2, next3, next5)

            if dp[i] == next2:
                i2 += 1
            if dp[i] == next3:
                i3 += 1
            if dp[i] == next5:
                i5 += 1

        return dp[n - 1]


# ---------- Tests ----------
def test():
    sol = Solution()

    assert sol.nthUglyNumber(1) == 1
    assert sol.nthUglyNumber(10) == 12
    # Sequence: 1,2,3,4,5,6,8,9,10,12

    assert sol.nthUglyNumber(2) == 2
    assert sol.nthUglyNumber(7) == 8
    assert sol.nthUglyNumber(11) == 15
    assert sol.nthUglyNumber(1690) == 2123366400

    print("All tests passed!")


if __name__ == "__main__":
    test()
