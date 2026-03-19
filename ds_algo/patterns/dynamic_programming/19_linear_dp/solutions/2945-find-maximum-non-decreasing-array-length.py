"""
2945. Find Maximum Non-decreasing Array Length

Pattern: Linear DP
Approach: Greedy with prefix sums and binary search. After operations (merging
    consecutive elements), we want the longest non-decreasing result. Use prefix
    sums. dp[i] = max segments ending at i. Track last segment sum to ensure
    non-decreasing. Use binary search to find valid split points.
Time Complexity: O(n log n)
Space Complexity: O(n)
"""
from bisect import bisect_left

def findMaximumLength(nums):
    n = len(nums)
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i + 1] = prefix[i] + nums[i]

    # dp[i] = max number of segments for first i elements
    # last[i] = the sum of the last segment when dp[i] is achieved
    dp = [0] * (n + 1)
    last = [0] * (n + 1)
    # For each position, we want to find the best split point j such that
    # prefix[i] - prefix[j] >= last[j] => prefix[i] >= prefix[j] + last[j]
    # We maintain a monotonic queue of candidates
    from collections import deque
    q = deque([0])  # indices into dp/last/prefix

    for i in range(1, n + 1):
        # Remove candidates that are dominated
        while len(q) > 1 and prefix[q[0]] + last[q[0]] <= prefix[i]:
            # q[0] is valid, but check if q[1] is also valid
            if prefix[q[1]] + last[q[1]] <= prefix[i]:
                q.popleft()
            else:
                break
        j = q[0]
        if prefix[j] + last[j] <= prefix[i]:
            dp[i] = dp[j] + 1
            last[i] = prefix[i] - prefix[j]
        else:
            dp[i] = dp[i - 1]
            last[i] = float('inf')

        # Maintain monotonicity: prefix[i] + last[i] should be increasing in queue
        while q and prefix[q[-1]] + last[q[-1]] >= prefix[i] + last[i]:
            q.pop()
        q.append(i)

    return dp[n]


# Tests
def test():
    assert findMaximumLength([5, 2, 2]) == 1, f"Got {findMaximumLength([5,2,2])}"
    assert findMaximumLength([1, 2, 3, 4]) == 4
    assert findMaximumLength([4, 3, 2, 6]) == 3
    assert findMaximumLength([1, 1, 1]) == 3
    assert findMaximumLength([10]) == 1
    print("All tests passed!")

test()
