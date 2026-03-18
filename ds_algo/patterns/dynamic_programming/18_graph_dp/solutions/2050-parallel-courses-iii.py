"""
2050. Parallel Courses III
https://leetcode.com/problems/parallel-courses-iii/

Pattern: 18 - Graph DP (Topological Sort + DP)

---
APPROACH: Kahn's algorithm (BFS topological sort) with DP.
- dp[i] = earliest time course i finishes.
- Initially dp[i] = time[i] for courses with no prerequisites.
- Process nodes in topological order. For each neighbor v of u,
  dp[v] = max(dp[v], dp[u] + time[v]).
- Answer is max(dp).

Time: O(V + E)  Space: O(V + E)
---
"""

from typing import List
from collections import deque


class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        """Return minimum time to finish all courses run in parallel."""
        graph = [[] for _ in range(n)]
        indegree = [0] * n

        for prev, nxt in relations:
            graph[prev - 1].append(nxt - 1)  # 1-indexed to 0-indexed
            indegree[nxt - 1] += 1

        dp = [0] * n
        queue = deque()
        for i in range(n):
            if indegree[i] == 0:
                dp[i] = time[i]
                queue.append(i)

        while queue:
            u = queue.popleft()
            for v in graph[u]:
                dp[v] = max(dp[v], dp[u] + time[v])
                indegree[v] -= 1
                if indegree[v] == 0:
                    queue.append(v)

        return max(dp)


# --- Tests ---
def test():
    sol = Solution()

    # Example 1: 3 courses, chain 1->2->3
    assert sol.minimumTime(3, [[1, 3], [2, 3]], [3, 2, 5]) == 8

    # Example 2: parallel + dependent
    assert sol.minimumTime(
        5, [[1, 5], [2, 5], [3, 5], [3, 4], [4, 5]], [1, 2, 3, 4, 5]
    ) == 12

    # Single course
    assert sol.minimumTime(1, [], [10]) == 10

    # All independent
    assert sol.minimumTime(3, [], [3, 1, 2]) == 3

    print("All tests passed!")


if __name__ == "__main__":
    test()
