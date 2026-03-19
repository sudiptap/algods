"""
3693. Climbing Stairs II
https://leetcode.com/problems/climbing-stairs-ii/

Pattern: 01 - Fibonacci Pattern

---
APPROACH: Extended Fibonacci
- Like climbing stairs but can take 1, 2, or 3 steps at a time.
- dp[i] = dp[i-1] + dp[i-2] + dp[i-3] (tribonacci).
- Base cases: dp[0]=1, dp[1]=1, dp[2]=2.

Time: O(n)  Space: O(1)
---
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return 1
        if n == 2:
            return 2

        a, b, c = 1, 1, 2  # dp[0], dp[1], dp[2]
        for i in range(3, n + 1):
            a, b, c = b, c, a + b + c
        return c


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.climbStairs(0) == 1
    assert sol.climbStairs(1) == 1
    assert sol.climbStairs(2) == 2
    assert sol.climbStairs(3) == 4  # {1+1+1, 1+2, 2+1, 3}
    assert sol.climbStairs(4) == 7  # {1111, 112, 121, 211, 13, 31, 22}
    assert sol.climbStairs(5) == 13

    print("All tests passed!")
