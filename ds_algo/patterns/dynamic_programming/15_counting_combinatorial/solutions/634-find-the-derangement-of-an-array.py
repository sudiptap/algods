"""
634. Find the Derangement of An Array
https://leetcode.com/problems/find-the-derangement-of-an-array/

Pattern: 15 - Counting / Combinatorial DP

---
APPROACH: Classic derangement formula with DP
- A derangement is a permutation where no element appears in its original position.
- dp[n] = (n-1) * (dp[n-1] + dp[n-2])
  - Pick any of (n-1) positions for element n.
  - If element at that position goes to n's spot: derangement of remaining n-2 -> dp[n-2]
  - If it goes elsewhere: derangement of remaining n-1 -> dp[n-1]
- Base cases: dp[1] = 0, dp[2] = 1

Time: O(n)  Space: O(1)
---
"""

MOD = 10**9 + 7


class Solution:
    def findDerangement(self, n: int) -> int:
        if n == 1:
            return 0
        if n == 2:
            return 1

        prev2, prev1 = 0, 1  # dp[1], dp[2]
        for i in range(3, n + 1):
            curr = (i - 1) * (prev1 + prev2) % MOD
            prev2, prev1 = prev1, curr

        return prev1


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.findDerangement(1) == 0
    assert sol.findDerangement(2) == 1
    assert sol.findDerangement(3) == 2   # {2,3,1}, {3,1,2}
    assert sol.findDerangement(4) == 9
    assert sol.findDerangement(5) == 44
    # Large n to test modular arithmetic
    assert sol.findDerangement(100) > 0

    print("all tests passed")
