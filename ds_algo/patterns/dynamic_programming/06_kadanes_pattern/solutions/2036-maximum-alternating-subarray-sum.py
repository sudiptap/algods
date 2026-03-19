"""
2036. Maximum Alternating Subarray Sum (Medium)
https://leetcode.com/problems/maximum-alternating-subarray-sum/

Find the maximum alternating sum of any subarray. The alternating sum
of a subarray starting at index i is: a[i] - a[i+1] + a[i+2] - ...

Pattern: Kadane's Pattern (Two States)
Approach:
- Two states at each position:
  - add: max alternating sum ending here where current element is added
  - sub: max alternating sum ending here where current element is subtracted
- Transitions:
  - new_add = max(nums[i], sub + nums[i])  (start new or extend from sub state)
  - new_sub = add - nums[i]  (extend from add state)
- Track max of add across all positions.

Time:  O(n)
Space: O(1)
"""

from typing import List


class Solution:
    def maximumAlternatingSubarraySum(self, nums: List[int]) -> int:
        """Return maximum alternating subarray sum.

        Args:
            nums: Array of integers.

        Returns:
            Maximum alternating sum of any subarray.
        """
        ans = float('-inf')
        add = float('-inf')  # best ending with + sign
        sub = float('-inf')  # best ending with - sign

        for x in nums:
            new_add = max(x, sub + x)
            new_sub = add - x
            add, sub = new_add, new_sub
            ans = max(ans, add, sub)

        return ans


# ---------- tests ----------
def test_max_alternating_subarray_sum():
    sol = Solution()

    # [3,-1,1,2]: alternating sums:
    # [3]=3, [3,-1]=4, [3,-1,1]=3+1-(-1)=3-(-1)+1=4... wait
    # alt sum of [3,-1,1,2] = 3-(-1)+1-2 = 3+1+1-2 = 3
    # alt sum of [3,-1] = 3-(-1) = 4
    # [3] = 3
    assert sol.maximumAlternatingSubarraySum([3, -1, 1, 2]) == 5

    # [2,2,2,2,2] -> [2]=2, [2,2]=0, etc. Best=2
    assert sol.maximumAlternatingSubarraySum([2, 2, 2, 2, 2]) == 2

    # [1] -> 1
    assert sol.maximumAlternatingSubarraySum([1]) == 1

    # [-1,-2,-3] -> best = -1 (single element)
    assert sol.maximumAlternatingSubarraySum([-1, -2, -3]) == -1

    # [4,-1,5] -> 4-(-1)+5=10? no: 4-(-1)=5, but [4,-1,5]=4-(-1)+5=10
    assert sol.maximumAlternatingSubarraySum([4, -1, 5]) == 10

    print("All tests passed for 2036. Maximum Alternating Subarray Sum")


if __name__ == "__main__":
    test_max_alternating_subarray_sum()
