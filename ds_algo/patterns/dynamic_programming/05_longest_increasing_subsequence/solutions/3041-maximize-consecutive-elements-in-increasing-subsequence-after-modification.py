"""
3041. Maximize Consecutive Elements in Increasing Subsequence After Modification

Pattern: Longest Increasing Subsequence
Approach: Each element can be nums[i] or nums[i]+1. Sort array. dp[v] = max length
    of consecutive sequence ending at value v. For each num, try ending at num or num+1.
Time Complexity: O(n log n)
Space Complexity: O(n)
"""

def maxSelectedElements(nums):
    nums.sort()
    dp = {}  # dp[v] = max consecutive length ending with value v

    for x in nums:
        # Try making it x+1
        dp[x + 1] = dp.get(x, 0) + 1
        # Try keeping it x
        dp[x] = dp.get(x - 1, 0) + 1

    return max(dp.values())


def test():
    assert maxSelectedElements([2, 1, 5, 1, 1]) == 3
    # [1,4,7,10]: each can be val or val+1. No 2+ consecutive possible -> 1
    assert maxSelectedElements([1, 4, 7, 10]) == 1
    print("All tests passed!")

test()
