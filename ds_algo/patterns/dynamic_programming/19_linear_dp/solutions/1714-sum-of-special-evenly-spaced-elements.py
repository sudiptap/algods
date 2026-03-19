"""
1714. Sum Of Special Evenly-Spaced Elements
https://leetcode.com/problems/sum-of-special-evenly-spaced-elements-in-array/

Pattern: 19 - Linear DP

---
APPROACH: Precompute suffix sums with stride
- For small strides (y <= sqrt(n)), precompute suffix sums for each stride.
  suffix[y][i] = sum of nums[i], nums[i+y], nums[i+2y], ...
- For large strides (y > sqrt(n)), directly compute the sum (few elements).
- Threshold: sqrt(n).

Time: O(n * sqrt(n)) for precomputation, O(sqrt(n)) per query
Space: O(n * sqrt(n))
---
"""

from typing import List
import math

MOD = 10**9 + 7


class Solution:
    def solve(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums)
        threshold = int(math.isqrt(n)) + 1

        # Precompute suffix sums for small strides
        # suffix[y][i] = nums[i] + nums[i+y] + nums[i+2y] + ... (mod MOD)
        suffix = {}
        for y in range(1, threshold + 1):
            suf = [0] * (n + 1)
            for i in range(n - 1, -1, -1):
                suf[i] = nums[i]
                if i + y < n:
                    suf[i] = (suf[i] + suf[i + y]) % MOD
            suffix[y] = suf

        result = []
        for x, y in queries:
            if y <= threshold:
                result.append(suffix[y][x])
            else:
                # Large stride: just iterate
                total = 0
                i = x
                while i < n:
                    total = (total + nums[i]) % MOD
                    i += y
                result.append(total)

        return result


# --- Tests ---
def test():
    sol = Solution()

    # Basic test
    nums = [0, 1, 2, 3, 4, 5, 6, 7]
    queries = [[0, 2], [0, 1], [4, 3]]
    result = sol.solve(nums, queries)
    # [0,2] -> 0+2+4+6 = 12
    # [0,1] -> 0+1+2+3+4+5+6+7 = 28
    # [4,3] -> 4+7 = 11
    assert result == [12, 28, 11]

    # Single element
    assert sol.solve([5], [[0, 1]]) == [5]

    # Large stride
    assert sol.solve([1, 2, 3, 4, 5], [[0, 5]]) == [1]
    assert sol.solve([1, 2, 3, 4, 5], [[0, 3]]) == [1 + 4]

    print("All tests passed!")


if __name__ == "__main__":
    test()
