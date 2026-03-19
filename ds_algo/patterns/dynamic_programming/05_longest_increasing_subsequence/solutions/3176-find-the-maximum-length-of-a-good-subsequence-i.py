"""
3176. Find the Maximum Length of a Good Subsequence I

Pattern: Longest Increasing Subsequence
Approach: dp[j][k] = max length of subsequence ending with value j having at most
    k positions where adjacent elements differ. For each element, either extend
    a subsequence ending with same value (no cost) or different value (cost 1).
Time Complexity: O(n * k)
Space Complexity: O(n * k)
"""

def maximumLength(nums, k):
    n = len(nums)
    # dp_val[v][j] = max length subsequence ending with value v, using j "differences"
    # For each num, for each j from k down to 0:
    #   dp_val[num][j] = max(dp_val[num][j] + 1,  # extend same value, free
    #                        best[j-1] + 1)         # extend any value, cost 1
    # best[j] = max over all v of dp_val[v][j]

    dp_val = {}  # dp_val[v] = list of length k+1
    best = [0] * (k + 1)

    for x in nums:
        if x not in dp_val:
            dp_val[x] = [0] * (k + 1)
        cur = dp_val[x]
        for j in range(k, -1, -1):
            cur[j] += 1  # extend same value subsequence
            if j > 0:
                cur[j] = max(cur[j], best[j - 1] + 1)
        # Update best
        for j in range(k + 1):
            best[j] = max(best[j], cur[j])

    return best[k]


def test():
    assert maximumLength([1, 2, 1, 1, 3], 2) == 4
    assert maximumLength([1, 2, 3, 4, 5, 1], 0) == 2
    assert maximumLength([1, 1, 1], 0) == 3
    print("All tests passed!")

test()
