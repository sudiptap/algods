"""
3177. Find the Maximum Length of a Good Subsequence II

Pattern: Longest Increasing Subsequence (Optimized)
Approach: Same as 3176 but optimized for large k. Use dp_val[v][j] = max length
    ending with value v using j differences. Track global best[j] = max over all v
    of dp_val[v][j]. Process in reverse j order to avoid conflicts.
Time Complexity: O(n * k)
Space Complexity: O(n * k) but practically much less with hash maps
"""

def maximumLength(nums, k):
    dp_val = {}
    best = [0] * (k + 1)

    for x in nums:
        if x not in dp_val:
            dp_val[x] = [0] * (k + 1)
        cur = dp_val[x]
        for j in range(k, -1, -1):
            cur[j] += 1
            if j > 0:
                cur[j] = max(cur[j], best[j - 1] + 1)
        for j in range(k + 1):
            best[j] = max(best[j], cur[j])

    return best[k]


def test():
    assert maximumLength([1, 2, 1, 1, 3], 2) == 4
    assert maximumLength([1, 2, 3, 4, 5, 1], 0) == 2
    assert maximumLength([1, 1, 1], 0) == 3
    print("All tests passed!")

test()
