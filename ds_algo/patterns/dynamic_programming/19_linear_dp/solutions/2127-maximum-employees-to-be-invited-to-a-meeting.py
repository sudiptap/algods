"""
2127. Maximum Employees to Be Invited to a Meeting (Hard)
https://leetcode.com/problems/maximum-employees-to-be-invited-to-a-meeting/

Each employee has exactly one favorite person. Seat them around a circular
table such that each is next to their favorite. Maximize employees seated.

Pattern: Linear DP (Functional Graph)
Approach:
- This is a functional graph (each node has out-degree 1).
- Every connected component has exactly one cycle.
- Case 1: Large cycles (length >= 3). Each can seat exactly cycle_length people.
- Case 2: Cycles of length 2 (mutual pairs). For each pair, attach the
  longest chain from outside the cycle to each node. Multiple pairs can
  coexist at the same table.
- Answer = max(largest single cycle, sum of all pair-based arrangements).

Time:  O(n)
Space: O(n)
"""

from typing import List
from collections import deque


class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        """Return maximum employees that can be seated.

        Args:
            favorite: favorite[i] = favorite person of employee i.

        Returns:
            Maximum number of employees at the table.
        """
        n = len(favorite)

        # Find all cycles using in-degree peeling (topological sort)
        in_deg = [0] * n
        for f in favorite:
            in_deg[f] += 1

        queue = deque()
        for i in range(n):
            if in_deg[i] == 0:
                queue.append(i)

        # Longest chain ending at each node (from non-cycle nodes)
        depth = [0] * n
        removed = [False] * n

        while queue:
            node = queue.popleft()
            removed[node] = True
            nxt = favorite[node]
            depth[nxt] = max(depth[nxt], depth[node] + 1)
            in_deg[nxt] -= 1
            if in_deg[nxt] == 0:
                queue.append(nxt)

        # Remaining nodes are in cycles
        max_cycle = 0
        pair_total = 0
        visited = [False] * n

        for i in range(n):
            if removed[i] or visited[i]:
                continue
            # Trace the cycle
            cycle = []
            node = i
            while not visited[node]:
                visited[node] = True
                cycle.append(node)
                node = favorite[node]

            cycle_len = len(cycle)
            if cycle_len == 2:
                # Mutual pair: add longest chains from each side
                pair_total += 2 + depth[cycle[0]] + depth[cycle[1]]
            else:
                max_cycle = max(max_cycle, cycle_len)

        return max(max_cycle, pair_total)


# ---------- tests ----------
def test_max_invitations():
    sol = Solution()

    # Example 1: [2,2,1,2] -> cycle 1<->2 (len 2) + chains
    assert sol.maximumInvitations([2, 2, 1, 2]) == 3

    # Example 2: [1,2,0] -> cycle 0->1->2->0 (len 3)
    assert sol.maximumInvitations([1, 2, 0]) == 3

    # Example 3: [3,0,1,4,1] -> 4
    assert sol.maximumInvitations([3, 0, 1, 4, 1]) == 4

    # Mutual pair
    assert sol.maximumInvitations([1, 0]) == 2

    print("All tests passed for 2127. Maximum Employees to Be Invited to a Meeting")


if __name__ == "__main__":
    test_max_invitations()
