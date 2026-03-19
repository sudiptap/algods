"""
3717. Minimum Operations to Make the Array Beautiful
https://leetcode.com/problems/minimum-operations-to-make-the-array-beautiful/

Pattern: 19 - Linear DP

---
APPROACH: DP tracking possible previous values
- Array is beautiful if nums[i] % nums[i-1] == 0 for all i > 0.
- Operation: increment any element by 1.
- dp[v] = min operations to make prefix ending with value v at current position.
- For each position, enumerate previous values and find smallest multiple >= nums[i].
- Values bounded by constraints (1 <= nums[i] <= 50, so multiples up to 100).

Time: O(n * V^2)  Space: O(V)
where V = max possible value (100)
---
"""

from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        MAX_VAL = 100
        # dp[v] = min cost so far if previous element's value is v
        dp = {}
        # First element: can be nums[0] with 0 cost, or higher with some cost
        # But we only need to consider nums[0] as-is (incrementing first element
        # never helps since it only makes divisibility harder for next elements).
        # Actually incrementing first element could help if next element is large.
        # We should consider all possible values for first element.
        # But optimal: first element should stay as nums[0] or we pick a value
        # that makes future elements easier. With values up to 50, multiples up to 100.
        for v in range(nums[0], MAX_VAL + 1):
            cost = v - nums[0]
            if v not in dp or cost < dp[v]:
                dp[v] = cost

        for i in range(1, len(nums)):
            new_dp = {}
            for prev, prev_cost in dp.items():
                # Current element must be a multiple of prev, and >= nums[i]
                # Find smallest multiple of prev >= nums[i]
                if prev == 0:
                    continue
                mul = ((nums[i] + prev - 1) // prev) * prev
                # Try this and next few multiples
                while mul <= MAX_VAL:
                    cost = prev_cost + (mul - nums[i])
                    if mul not in new_dp or cost < new_dp[mul]:
                        new_dp[mul] = cost
                    mul += prev
            dp = new_dp

        return min(dp.values()) if dp else 0


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.minOperations([3, 7, 9]) == 2    # [3,9,9]
    assert sol.minOperations([1, 1, 1]) == 0
    assert sol.minOperations([4]) == 0
    # [1,2,3]: 2%1=0 ok, 3%2=1 not ok. Need 3->4, cost 1.
    assert sol.minOperations([1, 2, 3]) == 1
    assert sol.minOperations([2, 3]) == 1         # 3->4, cost 1

    print("all tests passed")
