"""
96. Unique Binary Search Trees
https://leetcode.com/problems/unique-binary-search-trees/

Pattern: 09 - DP on Trees (Catalan number — counting version of #95)

---
APPROACH: DP (Catalan recurrence)
- dp[n] = number of structurally unique BSTs with n nodes
- Pick root i (1..n): left subtree has i-1 nodes, right has n-i
- dp[n] = sum(dp[i-1] * dp[n-i] for i in 1..n)
- This is exactly the Catalan number recurrence

Time: O(n^2)  Space: O(n)
---
"""


class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = dp[1] = 1

        for nodes in range(2, n + 1):
            for root in range(1, nodes + 1):
                dp[nodes] += dp[root - 1] * dp[nodes - root]

        return dp[n]


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.numTrees(3) == 5
    assert sol.numTrees(1) == 1
    assert sol.numTrees(4) == 14
    assert sol.numTrees(5) == 42
    assert sol.numTrees(19) == 1767263190

    print("all tests passed")
