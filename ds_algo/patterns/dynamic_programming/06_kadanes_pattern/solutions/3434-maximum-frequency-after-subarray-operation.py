"""
3434. Maximum Frequency After Subarray Operation
https://leetcode.com/problems/maximum-frequency-after-subarray-operation/

Pattern: 06 - Kadane's Pattern

---
APPROACH: Kadane variant per target value.
- Operation: choose subarray, add some value v to each element in it.
- We want to maximize frequency of value k after one operation.
- Existing k's outside the subarray are kept. Inside the subarray, elements equal to
  k-v become k (gain), elements already k might change (but we can choose v freely).
- For each possible source value s (s != k), consider v = k - s.
  In a subarray with this v applied: elements = s become k (+1), elements = k become k+v (lose if v!=0, i.e. s!=k).
  Actually if s == k, v = 0, no change.
- For each s != k: score[i] = +1 if nums[i]==s, -1 if nums[i]==k, 0 otherwise.
  Run Kadane on score to find max subarray sum. Add to base count of k.
- Also: we might not do any operation, so base count of k is a candidate.

Time: O(n * unique_values)  Space: O(n)
---
"""

from typing import List
from collections import Counter


class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        base = nums.count(k)
        best = base  # no operation

        unique_vals = set(nums)
        unique_vals.discard(k)

        for s in unique_vals:
            # Kadane: gain = max subarray sum of score where +1 for s, -1 for k, 0 otherwise
            cur = 0
            max_gain = 0
            for x in nums:
                if x == s:
                    cur += 1
                elif x == k:
                    cur -= 1
                # else: cur += 0
                if cur < 0:
                    cur = 0
                max_gain = max(max_gain, cur)
            best = max(best, base + max_gain)

        return best


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.maxFrequency([1, 4, 2, 3, 1, 4], 1) == 3  # not from LC, custom
    assert sol.maxFrequency([1, 2, 3, 4, 5, 6], 1) == 2
    assert sol.maxFrequency([10, 2, 3, 4, 5, 5, 4, 3, 2, 2], 10) == 4

    print("Solution: all tests passed")
