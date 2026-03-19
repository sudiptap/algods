"""
3196. Maximize Total Cost of Alternating Subarrays

Pattern: Linear DP
Approach: Split array into subarrays. Cost of subarray starting at index i:
    nums[i] - nums[i+1] + nums[i+2] - ... (alternating signs).
    dp with two states: add (must add current) or subtract (can subtract or start new).
    add[i] = max total using nums[0..i] where nums[i] is added.
    sub[i] = max total where nums[i] is subtracted.
Time Complexity: O(n)
Space Complexity: O(1)
"""

def maximumTotalCost(nums):
    n = len(nums)
    # State: at position i, the sign applied to nums[i]
    # If we add nums[i]: next can be subtracted (continue) or added (new subarray)
    # If we subtract nums[i]: next must be added (continue) or added (new subarray)
    add = nums[0]  # first element is always added
    sub = float('-inf')

    for i in range(1, n):
        new_add = max(add, sub) + nums[i]  # start new subarray or continue from sub
        new_sub = add - nums[i]  # continue from add (alternate sign)
        add, sub = new_add, new_sub

    return max(add, sub)


def test():
    assert maximumTotalCost([1, -2, 3, 4]) == 10
    assert maximumTotalCost([1, -1, 1, -1]) == 4
    assert maximumTotalCost([0]) == 0
    assert maximumTotalCost([1, -1]) == 2
    print("All tests passed!")

test()
