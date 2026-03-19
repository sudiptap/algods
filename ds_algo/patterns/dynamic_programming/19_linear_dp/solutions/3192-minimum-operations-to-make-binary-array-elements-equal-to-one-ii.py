"""
3192. Minimum Operations to Make Binary Array Elements Equal to One II

Pattern: Linear DP
Approach: Each operation flips all elements from index i to end. Track flip parity.
    Scan left to right: if current effective value is 0, flip (increment ops, toggle parity).
Time Complexity: O(n)
Space Complexity: O(1)
"""

def minOperations(nums):
    ops = 0
    flip = 0  # 0 or 1, tracks cumulative flip parity
    for x in nums:
        cur = x ^ flip
        if cur == 0:
            ops += 1
            flip ^= 1
    return ops


def test():
    assert minOperations([0, 1, 1, 0, 1]) == 4
    assert minOperations([1, 0, 0, 0]) == 1
    assert minOperations([1, 1, 1]) == 0
    print("All tests passed!")

test()
