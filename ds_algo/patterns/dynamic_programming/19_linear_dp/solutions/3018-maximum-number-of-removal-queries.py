"""
3018. Maximum Number of Removal Queries That Can Be Answered

Pattern: Linear DP
Approach: dp[i][j] represents the max queries answered using nums[i..j].
    For each query [l, r], we greedily try to match from both ends.
    Actually: dp[i][j] = max number of queries answerable if the remaining
    subarray is nums[i..j]. Process queries and use 2D DP on endpoints.
Time Complexity: O(n^2) for the DP
Space Complexity: O(n^2)

Note: This is a hard problem. We use dp where dp[i][j] = max queries we can
answer if we've removed elements outside [i,j]. For query [l,r], we need i<=l, j>=r.
We iterate queries sorted and use interval DP.
"""

def maximumProcessableQueries(nums, queries):
    n = len(nums)
    m = len(queries)
    # dp[i][j] = max queries answerable considering subarray nums[i..j]
    # Start with full array [0, n-1], process queries in order
    # At each step we can remove from left or right
    # Actually: dp[i][j] = max queries answered from query index dp[i][j] onwards
    # if current available subarray is [i..j]

    # For each query q = [l, r], it's answerable if i <= l and j >= r
    # We process queries 0..m-1. dp[i][j] = max queries answered starting
    # from some query index, given subarray [i, j].

    # Let dp[i][j] = the earliest query index we can reach having answered
    # all queries up to that point, with subarray shrunk to [i..j].
    # Actually let's define dp[i][j] = max number of queries answerable
    # if the remaining (unremoved) subarray is exactly [i..j].

    # Simpler: dp[i][j] = max queries answered when left pointer is i
    # and right pointer is j. We try all queries in order.
    # dp[i][j] starts at query 0. For query k=[l,r]:
    #   if i<=l and j>=r: answer it, move to k+1
    #   skip it

    # This is O(n^2 * m) which is too slow for large inputs.
    # Optimized: dp[i][j] = how many queries from 0..m-1 can be answered
    # with subarray [i..j]. We build dp bottom-up.

    # dp[i][j] = max(dp[i][j] without answering current, ...)
    # Let's define dp[i][j] = max queries answered with available range [i,j]
    # Transition: dp[i][j] = max queries we get. We check query dp[i][j]-th
    # To answer query k: need i <= queries[k][0] and j >= queries[k][1]

    # Redefine: dp[i][j] = max index k such that queries 0..k-1 are all answerable
    # with nums reduced to [i..j] or wider. No, queries are independent.

    # Final approach: dp[i][j] = max queries answerable with subarray [i, j]
    # Transition from [0, n-1]: shrink from left or right
    # dp[i][j] = max(dp[i+1][j], dp[i][j-1]) + (1 if query dp[i][j] answerable)

    # Let's use: dp[i][j] = number of queries answerable from the first dp[i][j]
    # queries, when available subarray is [i..j].
    # Process: dp[i][j] = dp_val. Check query dp_val: if answerable, dp[i][j] = dp_val+1
    # Then dp[i+1][j] = max(dp[i+1][j], dp[i][j])
    # and dp[i][j-1] = max(dp[i][j-1], dp[i][j])

    dp = [[0] * n for _ in range(n)]

    # Start from [0, n-1] and expand dp
    # Check if query 0 is answerable with [0, n-1]
    k = 0
    while k < m and 0 <= queries[k][0] and n - 1 >= queries[k][1]:
        k += 1
    dp[0][n - 1] = k

    ans = dp[0][n - 1]

    for i in range(n):
        for j in range(n - 1, i - 1, -1):
            # Current dp[i][j] = number of queries answered
            cur = dp[i][j]
            ans = max(ans, cur)
            # Try shrinking left: remove nums[i]
            if i + 1 <= j:
                nxt = dp[i + 1][j]
                if nxt < cur:
                    nxt = cur
                # From nxt, try answering more queries
                while nxt < m and i + 1 <= queries[nxt][0] and j >= queries[nxt][1]:
                    nxt += 1
                if dp[i + 1][j] < nxt:
                    dp[i + 1][j] = nxt
            # Try shrinking right
            if j - 1 >= i:
                nxt = dp[i][j - 1]
                if nxt < cur:
                    nxt = cur
                while nxt < m and i <= queries[nxt][0] and j - 1 >= queries[nxt][1]:
                    nxt += 1
                if dp[i][j - 1] < nxt:
                    dp[i][j - 1] = nxt

    return ans


def test():
    assert maximumProcessableQueries([1, 2, 3, 4, 5], [[1, 2], [0, 3]]) == 2
    assert maximumProcessableQueries([1, 2], [[0, 1]]) == 1
    assert maximumProcessableQueries([1], [[0, 0]]) == 1
    print("All tests passed!")

test()
