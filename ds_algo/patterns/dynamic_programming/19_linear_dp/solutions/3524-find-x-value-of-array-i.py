"""
3524. Find X Value of Array I
https://leetcode.com/problems/find-x-value-of-array-i/

Pattern: 19 - Linear DP (dp[j][remainder])

---
APPROACH: Count subarrays whose product mod k equals each possible remainder.
- For each ending position, maintain dp[r] = number of subarrays ending here with
  product mod k == r.
- Transition: dp_new[(r * nums[i]) % k] += dp[r]; also dp_new[nums[i] % k] += 1.
- Answer for each x is the total count of subarrays with product % k == x.

Time: O(n * k)  Space: O(k)
---
"""

from typing import List


class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        # answer[x] = count of subarrays with product % k == x
        answer = [0] * k

        # dp[r] = count of subarrays ending at current position with product mod k == r
        dp = [0] * k

        for num in nums:
            new_dp = [0] * k
            v = num % k
            for r in range(k):
                if dp[r] > 0:
                    new_dp[(r * v) % k] += dp[r]
            # Single element subarray
            new_dp[v] += 1
            dp = new_dp

            for r in range(k):
                answer[r] += dp[r]

        return answer


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.resultArray([1, 2, 3, 4, 5], 3) == [9, 2, 4]
    assert sol.resultArray([1, 2, 4, 8, 16, 32], 4) == [18, 1, 2, 0]
    assert sol.resultArray([1], 1) == [1]

    print("Solution: all tests passed")
