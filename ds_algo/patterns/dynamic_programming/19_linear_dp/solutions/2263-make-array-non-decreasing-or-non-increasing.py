"""
2263. Make Array Non-decreasing or Non-increasing
https://leetcode.com/problems/make-array-non-decreasing-or-non-increasing/

Pattern: 19 - Linear DP

---
APPROACH: LIS-based with coordinate compression (min operations = n - LIS/LDS)
- To make array non-decreasing with minimum operations (each op changes element by 1):
  Use DP with a heap approach. For non-decreasing: process left to right, use max-heap
  to track medians. For non-increasing: reverse array and do the same.
- This is the "minimum cost to make array non-decreasing" problem solved with
  slope trick / priority queue approach.
- Cost of making non-decreasing: for each element, if it's less than the current
  max in heap, pop max, add cost, push current element twice.
- Answer: min(cost_nondecreasing, cost_nonincreasing)

Time: O(n log n)  Space: O(n)
---
"""

from typing import List
import heapq


class Solution:
    def convertArray(self, nums: List[int]) -> int:
        def min_cost_nondecreasing(arr):
            """Slope trick: min cost to make arr non-decreasing, cost = |change|."""
            heap = []  # max-heap (negate values)
            cost = 0
            for x in arr:
                if heap and -heap[0] > x:
                    top = -heapq.heappop(heap)
                    cost += top - x
                    heapq.heappush(heap, -x)
                heapq.heappush(heap, -x)
            return cost

        cost1 = min_cost_nondecreasing(nums)
        cost2 = min_cost_nondecreasing(nums[::-1])  # non-increasing = reverse non-decreasing
        return min(cost1, cost2)


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.convertArray([3, 2, 4, 5, 0]) == 4
    assert sol.convertArray([2, 2, 3, 4]) == 0
    assert sol.convertArray([0]) == 0
    assert sol.convertArray([5, 4, 3, 2, 1]) == 0
    assert sol.convertArray([1, 2, 3, 4, 5]) == 0

    print("all tests passed")
