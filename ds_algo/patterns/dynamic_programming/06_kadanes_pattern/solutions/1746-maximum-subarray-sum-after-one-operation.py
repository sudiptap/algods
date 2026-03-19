"""
1746. Maximum Subarray Sum After One Operation
https://leetcode.com/problems/maximum-subarray-sum-after-one-operation/

Pattern: 06 - Kadane's Pattern

---
APPROACH: Kadane's with two states
- Track two values at each position:
  - no_op: max subarray sum ending here with no squaring done yet
  - one_op: max subarray sum ending here with exactly one squaring done
- Transitions:
  - no_op = max(nums[i], no_op + nums[i])
  - one_op = max(nums[i]^2, no_op + nums[i]^2, one_op + nums[i])
- Answer: max of all one_op values (must use exactly one operation).

Time: O(n)
Space: O(1)
---
"""

from typing import List


class Solution:
    def maxSumAfterOperation(self, nums: List[int]) -> int:
        no_op = 0
        one_op = 0
        result = float('-inf')

        for x in nums:
            sq = x * x
            one_op = max(sq, no_op + sq, one_op + x)
            no_op = max(x, no_op + x)
            result = max(result, one_op)

        return result


# --- Tests ---
def test():
    sol = Solution()

    assert sol.maxSumAfterOperation([2, -1, -4, -3]) == 17  # square -4: [2,-1,16,-3], subarray [16]=16? or [2,-1,16]=17
    assert sol.maxSumAfterOperation([1, -1, 1, 1, -1, -1, 1]) == 4
    assert sol.maxSumAfterOperation([-1, -1, -1]) == 1  # square any -1 -> 1

    # Single element
    assert sol.maxSumAfterOperation([5]) == 25
    assert sol.maxSumAfterOperation([-3]) == 9

    print("All tests passed!")


if __name__ == "__main__":
    test()
