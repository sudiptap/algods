"""
787. Cheapest Flights Within K Stops
https://leetcode.com/problems/cheapest-flights-within-k-stops/

Pattern: 18 - Graph DP (Bellman-Ford variant)

---
APPROACH: Bellman-Ford limited to k+1 relaxation rounds.
- k stops means at most k+1 edges.
- dp[i] = cheapest price to reach city i.
- Run k+1 iterations of edge relaxation.
- CRITICAL: copy the dp array at the start of each iteration so we
  don't use prices computed in the same round (which would allow
  more edges than permitted).

Time: O(k * E) where E = number of flights  Space: O(n)
---
"""

from typing import List


class Solution:
    def findCheapestPrice(
        self, n: int, flights: List[List[int]], src: int, dst: int, k: int
    ) -> int:
        """Return cheapest price from src to dst with at most k stops, or -1."""
        INF = float("inf")
        dp = [INF] * n
        dp[src] = 0

        for _ in range(k + 1):
            prev = dp[:]  # snapshot to prevent using too many edges
            for u, v, w in flights:
                if prev[u] + w < dp[v]:
                    dp[v] = prev[u] + w

        return dp[dst] if dp[dst] != INF else -1


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    # Example 1
    assert sol.findCheapestPrice(
        4, [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]],
        0, 3, 1
    ) == 700

    # Example 2
    assert sol.findCheapestPrice(
        3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]],
        0, 2, 1
    ) == 200

    # Example 3: no route within k stops
    assert sol.findCheapestPrice(
        3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]],
        0, 2, 0
    ) == 500

    # Unreachable
    assert sol.findCheapestPrice(
        3, [[0, 1, 100]],
        0, 2, 1
    ) == -1

    # Direct flight
    assert sol.findCheapestPrice(
        2, [[0, 1, 50]],
        0, 1, 0
    ) == 50

    print("all tests passed")
