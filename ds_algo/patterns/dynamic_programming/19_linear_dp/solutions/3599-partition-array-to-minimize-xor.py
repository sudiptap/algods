"""
3599. Partition Array to Minimize XOR
https://leetcode.com/problems/partition-array-to-minimize-xor/

Pattern: 19 - Linear DP

---
APPROACH: DP partitioning into k groups
- Partition array into exactly k contiguous subarrays.
- Cost of a subarray = XOR of all elements in it.
- Minimize sum of costs.
- dp[i][j] = min total XOR cost for first i elements split into j groups.
- dp[i][j] = min over all m < i of (dp[m][j-1] + XOR(nums[m..i-1])).
- Precompute prefix XOR for range XOR queries.

Time: O(n^2 * k)  Space: O(n * k)
---
"""

from typing import List


class Solution:
    def minXorSum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix_xor = [0] * (n + 1)
        for i in range(n):
            prefix_xor[i + 1] = prefix_xor[i] ^ nums[i]

        def range_xor(l, r):  # XOR of nums[l..r] inclusive
            return prefix_xor[r + 1] ^ prefix_xor[l]

        INF = float('inf')
        dp = [[INF] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 0

        for i in range(1, n + 1):
            for j in range(1, min(i, k) + 1):
                for m in range(j - 1, i):
                    val = dp[m][j - 1] + range_xor(m, i - 1)
                    if val < dp[i][j]:
                        dp[i][j] = val

        return dp[n][k]


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    # [1,2,3,4] into 2 groups: [1,2],[3,4] -> 3+7=10; [1],[2,3,4] -> 1+5=6; etc.
    # [1,2,3],[4] -> 0+4=4; best
    res = sol.minXorSum([1, 2, 3, 4], 2)
    assert res == 4, f"Got {res}"

    # Single group
    res = sol.minXorSum([3, 5], 1)
    assert res == 6, f"Got {res}"  # 3^5 = 6

    # Each element its own group
    res = sol.minXorSum([1, 2, 3], 3)
    assert res == 6, f"Got {res}"  # 1+2+3

    print("All tests passed!")
