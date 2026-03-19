"""
2969. Minimum Number of Coins for Fruits II

Pattern: Linear DP
Approach: Monotonic deque optimization. If you buy fruit at index i (1-indexed),
    you get fruits i+1..2*i for free. dp[i] = min cost to acquire fruits 1..i.
    dp[i] = min(dp[j-1] + prices[j]) for valid j where 2*j >= i.
    Use a monotonic deque to track minimum dp[j-1]+prices[j] over a sliding window.
Time Complexity: O(n)
Space Complexity: O(n)
"""
from collections import deque

def minimumCoins(prices):
    n = len(prices)
    if n == 1:
        return prices[0]

    # dp[i] = min cost to get all fruits 1..i (1-indexed)
    # If we buy fruit j (1-indexed), we pay prices[j-1] and get j+1..2j free
    # So dp[i] = min over j where 2j >= i of (dp[j-1] + prices[j-1])
    # j ranges: j >= ceil(i/2) to j = i
    dp = [float('inf')] * (n + 1)
    dp[0] = 0
    dq = deque()  # stores (j, dp[j-1] + prices[j-1]) in increasing order of value

    j = 1
    for i in range(1, n + 1):
        # Add all j up to i into the deque
        while j <= i:
            val = dp[j - 1] + prices[j - 1]
            while dq and dq[-1][1] >= val:
                dq.pop()
            dq.append((j, val))
            j += 1

        # Remove j's that can't cover fruit i: need 2*j >= i => j >= ceil(i/2)
        while dq and dq[0][0] * 2 < i:
            dq.popleft()

        dp[i] = dq[0][1]

    return dp[n]


def test():
    assert minimumCoins([3, 1, 2]) == 4
    assert minimumCoins([1, 10, 1, 1]) == 2
    assert minimumCoins([26, 18, 6, 12, 49, 7, 45, 45]) == 39
    assert minimumCoins([5]) == 5
    print("All tests passed!")

test()
