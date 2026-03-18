"""
396. Rotate Function (Medium)

Given an integer array nums of length n, define:
    F(k) = sum( i * nums[(i + k) % n] )  for i in 0..n-1

Return the maximum value of F(0), F(1), ..., F(n-1).

Key insight (O(n) math):
    totalSum = sum(nums)
    F(0) = 0*nums[0] + 1*nums[1] + ... + (n-1)*nums[n-1]

    F(k) - F(k-1)
      = totalSum - n * nums[n - k]

    So we can compute F(0) directly, then iterate:
        F(k) = F(k-1) + totalSum - n * nums[n - k]

    Time : O(n)
    Space: O(1)

Example:
    nums = [4,3,2,6]
    F(0) = 0*4 + 1*3 + 2*2 + 3*6 = 25
    F(1) = 0*6 + 1*4 + 2*3 + 3*2 = 16
    F(2) = 0*2 + 1*6 + 2*4 + 3*3 = 23
    F(3) = 0*3 + 1*2 + 2*6 + 3*4 = 26
    Answer = 26
"""

from typing import List


class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        """O(n) time, O(1) space using the recurrence F(k)=F(k-1)+S-n*nums[n-k]."""
        n = len(nums)
        if n == 0:
            return 0

        total_sum = sum(nums)
        f = sum(i * nums[i] for i in range(n))  # F(0)
        best = f

        for k in range(1, n):
            f = f + total_sum - n * nums[n - k]
            best = max(best, f)

        return best


# ---- Tests ----
def test():
    sol = Solution()

    assert sol.maxRotateFunction([4, 3, 2, 6]) == 26
    assert sol.maxRotateFunction([100]) == 0
    assert sol.maxRotateFunction([1, 2]) == 2  # F(0)=2, F(1)=1
    assert sol.maxRotateFunction([0, 0, 0]) == 0
    # Cross-check negative array with brute force
    nums = [-1, -2, -3]
    bf = max(
        sum(i * nums[(i + k) % 3] for i in range(3))
        for k in range(3)
    )
    assert sol.maxRotateFunction(nums) == bf

    # Larger brute-force cross-check
    import random
    random.seed(42)
    for _ in range(50):
        n = random.randint(1, 20)
        nums = [random.randint(-100, 100) for _ in range(n)]
        expected = max(
            sum(i * nums[(i + k) % n] for i in range(n))
            for k in range(n)
        )
        assert sol.maxRotateFunction(nums) == expected

    print("All tests passed!")


if __name__ == "__main__":
    test()
