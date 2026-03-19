"""
3077. Maximum Strength of K Disjoint Subarrays

Pattern: Kadane's Pattern
Approach: dp[i][j][0/1] where i=position, j=subarrays used, 0=not in subarray,
    1=in subarray. The j-th subarray has weight (k-j+1) * (-1)^(j+1).
    Transition: extend current subarray or start/end subarrays.
Time Complexity: O(n * k)
Space Complexity: O(n * k)
"""

def maximumStrength(nums, k):
    n = len(nums)
    INF = float('-inf')

    # Weight of j-th subarray (1-indexed): sign * (k - j + 1)
    # sign: odd j -> positive, even j -> negative
    weights = []
    for j in range(1, k + 1):
        w = (k - j + 1) * (1 if j % 2 == 1 else -1)
        weights.append(w)

    # dp_in[j] = max strength when currently inside j-th subarray (0-indexed)
    # dp_out[j] = max strength when j subarrays completed and not inside any
    dp_in = [INF] * k
    dp_out = [INF] * (k + 1)
    dp_out[0] = 0

    for i in range(n):
        new_in = [INF] * k
        new_out = [INF] * (k + 1)
        new_out[0] = 0

        for j in range(k):
            w = weights[j]
            # Start new j-th subarray at i
            if dp_out[j] != INF:
                new_in[j] = max(new_in[j], dp_out[j] + w * nums[i])
            # Extend j-th subarray
            if dp_in[j] != INF:
                new_in[j] = max(new_in[j], dp_in[j] + w * nums[i])

        for j in range(k):
            # End j-th subarray (was inside, now outside)
            if dp_in[j] != INF:
                new_out[j + 1] = max(new_out[j + 1], dp_in[j])
            if new_in[j] != INF:
                new_out[j + 1] = max(new_out[j + 1], new_in[j])

        # Carry forward out states
        for j in range(k + 1):
            new_out[j] = max(new_out[j], dp_out[j])

        dp_in = new_in
        dp_out = new_out

    return dp_out[k]


def test():
    assert maximumStrength([1, 2, 3, -1, 2], 3) == 22
    assert maximumStrength([-1, -2, -3], 1) == -1
    print("All tests passed!")

test()
