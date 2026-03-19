"""
2172. Maximum AND Sum of Array (Hard)
https://leetcode.com/problems/maximum-and-sum-of-array/

Given array nums and numSlots slots (each slot can hold at most 2 numbers),
maximize sum of (nums[i] AND slot_number) for all assignments.

Pattern: Bitmask DP (Ternary)
Approach:
- Each slot can hold 0, 1, or 2 numbers -> ternary state.
- dp[state] = max AND sum where state encodes how many numbers each
  slot has received (base 3).
- Total numbers placed = sum of digits of state in base 3.
- For each state, the next number to place is nums[total_placed].
- Try each slot that has room (digit < 2), add (nums[idx] AND slot).

Time:  O(3^numSlots * numSlots)
Space: O(3^numSlots)
"""

from typing import List


class Solution:
    def maximumANDSum(self, nums: List[int], numSlots: int) -> int:
        """Return maximum AND sum assigning nums to slots.

        Args:
            nums: Array of integers.
            numSlots: Number of slots (each holds at most 2).

        Returns:
            Maximum AND sum.
        """
        # Pad nums to 2*numSlots with 0s
        while len(nums) < 2 * numSlots:
            nums.append(0)

        total_states = 3 ** numSlots
        dp = [-1] * total_states
        dp[0] = 0

        # Precompute powers of 3
        pow3 = [1] * (numSlots + 1)
        for i in range(1, numSlots + 1):
            pow3[i] = pow3[i - 1] * 3

        def get_digit(state, slot):
            return (state // pow3[slot]) % 3

        def count_placed(state):
            total = 0
            s = state
            for _ in range(numSlots):
                total += s % 3
                s //= 3
            return total

        ans = 0
        for state in range(total_states):
            if dp[state] == -1:
                continue
            idx = count_placed(state)
            if idx >= len(nums):
                ans = max(ans, dp[state])
                continue

            for slot in range(numSlots):
                if get_digit(state, slot) < 2:
                    new_state = state + pow3[slot]
                    val = dp[state] + (nums[idx] & (slot + 1))
                    if val > dp[new_state]:
                        dp[new_state] = val
                        ans = max(ans, val)

        return ans


# ---------- tests ----------
def test_max_and_sum():
    sol = Solution()

    # Example 1: [1,2,3,4,5,6], numSlots=3
    assert sol.maximumANDSum([1, 2, 3, 4, 5, 6], 3) == 9

    # Example 2: [1,3,10,4,7,1], numSlots=9
    assert sol.maximumANDSum([1, 3, 10, 4, 7, 1], 9) == 24

    # Simple
    assert sol.maximumANDSum([1], 1) == 1

    print("All tests passed for 2172. Maximum AND Sum of Array")


if __name__ == "__main__":
    test_max_and_sum()
