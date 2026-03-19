"""
2902. Count of Sub-Multisets With Bounded Sum
https://leetcode.com/problems/count-of-sub-multisets-with-bounded-sum/

Pattern: 03 - Unbounded Knapsack (Bounded knapsack with frequency optimization)

---
APPROACH: Count frequency of each element. For element 0, multiply by (freq+1).
For other elements with value v and count c, use sliding window bounded knapsack:
dp[j] += dp[j-v] - dp[j-(c+1)*v]. Process each distinct value with prefix sums.

Time: O(n * r) where n = distinct values  Space: O(r)
---
"""

from typing import List
from collections import Counter

MOD = 10**9 + 7


class Solution:
    def countSubMultisets(self, nums: List[int], l: int, r: int) -> int:
        freq = Counter(nums)
        zeros = freq.pop(0, 0)

        dp = [0] * (r + 1)
        dp[0] = 1

        for val, cnt in freq.items():
            # Bounded knapsack: can use val at most cnt times
            # Use prefix sum trick on residue classes mod val
            new_dp = [0] * (r + 1)
            for remainder in range(val):
                # Process indices: remainder, remainder+val, remainder+2*val, ...
                window_sum = 0
                j = remainder
                count = 0
                while j <= r:
                    window_sum = (window_sum + dp[j]) % MOD
                    # If we've used more than cnt copies, subtract the oldest
                    if count > cnt:
                        window_sum = (window_sum - dp[j - (cnt + 1) * val]) % MOD
                    new_dp[j] = window_sum
                    j += val
                    count += 1
            dp = new_dp

        # Multiply by (zeros + 1) for choosing how many 0s
        # Sum dp[l..r]
        ans = sum(dp[l:r + 1]) % MOD
        ans = ans * (zeros + 1) % MOD
        return ans


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.countSubMultisets([1, 2, 2, 3], 6, 6) == 1
    assert sol.countSubMultisets([2, 1, 4, 2, 7], 1, 5) == 7
    assert sol.countSubMultisets([1, 2, 1, 3, 5, 2], 3, 5) == 9

    print("All tests passed!")
