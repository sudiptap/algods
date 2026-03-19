"""
3229. Minimum Operations to Make Array Equal to Target

Pattern: Linear DP
Approach: Compute diff[i] = target[i] - nums[i]. The problem reduces to making
    diff array all zeros using +1/-1 on subarrays. This equals the sum of positive
    increases plus the sum of negative decreases when scanning left to right.
    Similar to "minimum number of increments on subarrays to form target array".
Time Complexity: O(n)
Space Complexity: O(n)
"""

def minimumOperations(nums, target):
    n = len(nums)
    diff = [target[i] - nums[i] for i in range(n)]

    ops = abs(diff[0])
    for i in range(1, n):
        if diff[i] > diff[i - 1] and diff[i] > 0 and diff[i - 1] >= 0:
            ops += diff[i] - diff[i - 1]
        elif diff[i] < diff[i - 1] and diff[i] < 0 and diff[i - 1] <= 0:
            ops += abs(diff[i]) - abs(diff[i - 1])
        elif diff[i] > 0 and diff[i - 1] <= 0:
            ops += diff[i]
        elif diff[i] < 0 and diff[i - 1] >= 0:
            ops += abs(diff[i])
        # If same sign and magnitude decreasing, no extra ops needed

    return ops


def test():
    assert minimumOperations([3, 5, 1, 2], [4, 6, 2, 4]) == 2
    assert minimumOperations([1, 3, 2], [2, 1, 4]) == 5
    print("All tests passed!")

test()
