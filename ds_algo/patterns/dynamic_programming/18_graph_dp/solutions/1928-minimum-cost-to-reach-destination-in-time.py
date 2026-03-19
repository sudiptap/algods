"""
1928. Minimum Cost to Reach Destination in Time (Hard)
https://leetcode.com/problems/minimum-cost-to-reach-destination-in-time/

Given a graph with n cities, edges with travel times, passing fees per city,
and maxTime, find the minimum cost path from city 0 to city n-1 within maxTime.

Pattern: Graph DP / Modified Dijkstra
Approach:
- dp[time][city] = min cost to reach city using exactly 'time' time.
- Use Dijkstra-like approach: priority queue on (cost, time, city).
- For each state, expand to neighbors if time + edge_time <= maxTime.
- Track best known time to reach each city at each cost level, or
  simply track min cost at each (city, time) pair.

Time:  O(maxTime * E * log(maxTime * V)) with Dijkstra
Space: O(maxTime * V)
"""

from typing import List
import heapq


class Solution:
    def minCost(self, maxTime: int, edges: List[List[int]], passingFees: List[int]) -> int:
        """Return min cost to travel from city 0 to n-1 within maxTime.

        Args:
            maxTime: Maximum allowed travel time.
            edges: List of [u, v, time] edges.
            passingFees: Fee for passing through each city.

        Returns:
            Minimum cost, or -1 if impossible.
        """
        n = len(passingFees)
        # Build adjacency list
        graph = [[] for _ in range(n)]
        for u, v, t in edges:
            graph[u].append((v, t))
            graph[v].append((u, t))

        # min_time[city] = minimum time we've reached this city with
        # (to prune states that arrive later with higher cost)
        min_time = [float('inf')] * n

        # Dijkstra: (cost, time_spent, city)
        pq = [(passingFees[0], 0, 0)]
        min_time[0] = 0

        while pq:
            cost, time, city = heapq.heappop(pq)

            if city == n - 1:
                return cost

            if time > min_time[city]:
                continue

            for neighbor, travel_time in graph[city]:
                new_time = time + travel_time
                if new_time > maxTime:
                    continue
                new_cost = cost + passingFees[neighbor]
                if new_time < min_time[neighbor]:
                    min_time[neighbor] = new_time
                    heapq.heappush(pq, (new_cost, new_time, neighbor))

        return -1


# ---------- tests ----------
def test_min_cost():
    sol = Solution()

    # Example 1
    assert sol.minCost(30, [[0,1,10],[1,2,10],[2,5,10],[0,3,1],[3,4,10],[4,5,15]], [5,1,2,20,20,3]) == 11

    # Example 2
    assert sol.minCost(29, [[0,1,10],[1,2,10],[2,5,10],[0,3,1],[3,4,10],[4,5,15]], [5,1,2,20,20,3]) == 48

    # Example 3: impossible
    assert sol.minCost(25, [[0,1,10],[1,2,10],[2,5,10],[0,3,1],[3,4,10],[4,5,15]], [5,1,2,20,20,3]) == -1

    print("All tests passed for 1928. Minimum Cost to Reach Destination in Time")


if __name__ == "__main__":
    test_min_cost()
