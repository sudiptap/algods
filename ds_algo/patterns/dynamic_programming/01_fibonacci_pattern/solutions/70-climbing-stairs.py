"""
70. Climbing Stairs
https://leetcode.com/problems/climbing-stairs/

Pattern: 01 - Fibonacci Pattern (THE intro problem for this pattern)

---
APPROACH: It's literally Fibonacci.
- dp[i] = ways to reach step i
- dp[i] = dp[i-1] + dp[i-2]  (take 1 step or 2 steps)
- Base: dp[0] = 1, dp[1] = 1
- Only need two previous values → O(1) space

Time: O(n)  Space: O(1)
---
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        prev2, prev1 = 1, 2
        for _ in range(3, n + 1):
            prev2, prev1 = prev1, prev2 + prev1

        return prev1


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.climbStairs(2) == 2
    assert sol.climbStairs(3) == 3
    assert sol.climbStairs(1) == 1
    assert sol.climbStairs(5) == 8
    assert sol.climbStairs(45) == 1836311903

    print("all tests passed")
