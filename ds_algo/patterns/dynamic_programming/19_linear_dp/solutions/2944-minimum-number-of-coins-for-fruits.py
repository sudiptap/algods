"""
2944. Minimum Number of Coins for Fruits
https://leetcode.com/problems/minimum-number-of-coins-for-fruits/

Pattern: 19 - Linear DP

---
APPROACH: dp[i] = min coins to acquire all fruits from i to n (1-indexed).
- Buying fruit i (cost prices[i]) gives fruits i+1..2i for free.
- So dp[i] = prices[i] + min(dp[i+1..2i+1]), where dp[j] for j > n is 0
  (meaning all fruits already covered).
- Process right to left. Use a monotonic deque (min-deque) over a window
  whose right bound shrinks as i decreases from n to 1.

Time: O(n)  Space: O(n)
---
"""

from typing import List
from collections import deque


class Solution:
    def minimumCoins(self, prices: List[int]) -> int:
        """Return minimum coins to acquire all fruits."""
        n = len(prices)
        if n == 1:
            return prices[0]

        # dp[i] = min cost to acquire fruits i..n (1-indexed)
        # dp[n+1] = 0 (sentinel: nothing left to buy)
        dp = [0] * (n + 2)

        # Build dp right to left
        # For index i, window is [i+1, min(2*i+1, n+1)]
        # As i goes from n down to 1, we add each new dp[i+1] to our structure.
        # The window right bound 2*i+1 decreases as i decreases.

        # Monotonic deque: stores indices with non-decreasing dp values
        # Front of deque = index with minimum dp in current window
        dq = deque()

        for i in range(n, 0, -1):
            # If 2*i >= n, buying fruit i covers all remaining fruits
            if 2 * i >= n:
                dp[i] = prices[i - 1]
            else:
                # Remove from front anything outside window (index > 2*i+1)
                while dq and dq[0] > 2 * i + 1:
                    dq.popleft()
                dp[i] = prices[i - 1] + dp[dq[0]]

            # Add dp[i] to deque (it will be in window for some earlier index)
            while dq and dp[dq[-1]] >= dp[i]:
                dq.pop()
            dq.append(i)

        return dp[1]


# --- Tests ---
def test():
    sol = Solution()

    # Example 1
    assert sol.minimumCoins([3, 1, 2]) == 4

    # Example 2
    assert sol.minimumCoins([1, 10, 1, 1]) == 2

    # Single fruit
    assert sol.minimumCoins([5]) == 5

    # Two fruits — buy first, second is free
    assert sol.minimumCoins([1, 100]) == 1

    # Three fruits — buy fruit 1 (gets fruit 2 free), then must consider fruit 3
    assert sol.minimumCoins([1, 100, 1]) == 2  # buy 1 and 3

    # Cheaper to buy first that covers many
    assert sol.minimumCoins([1, 1, 1, 1, 1]) == 2

    print("All tests passed!")


if __name__ == "__main__":
    test()
