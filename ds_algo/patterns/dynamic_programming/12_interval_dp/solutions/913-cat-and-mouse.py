"""
913. Cat and Mouse (Hard)
https://leetcode.com/problems/cat-and-mouse/

A game on an undirected graph. Mouse starts at node 1, cat at node 2.
Node 0 is the hole. Players alternate; mouse moves first. Mouse wins by
reaching hole (0). Cat wins by landing on mouse. Draw if state repeats.
Cat cannot enter node 0. Return 1 if mouse wins, 2 if cat wins, 0 if draw.

Pattern: Interval DP / Game DP
Approach:
- State: (mouse_pos, cat_pos, turn) where turn=0 for mouse, 1 for cat.
- BFS backward from terminal states:
  - Mouse at 0 -> mouse wins (1).
  - Mouse == cat -> cat wins (2).
- For each resolved state, propagate to parent states:
  - If a parent can move to a winning state for its player, it wins.
  - If all children of a parent are losing, the parent loses.
  - Otherwise, draw (0).

Time:  O(n^3) — O(n^2) states, each with O(n) edges.
Space: O(n^2)
"""

from collections import deque
from typing import List

MOUSE_TURN, CAT_TURN = 0, 1
DRAW, MOUSE_WIN, CAT_WIN = 0, 1, 2


class Solution:
    def catMouseGame(self, graph: List[List[int]]) -> int:
        """Return game outcome: 0=draw, 1=mouse wins, 2=cat wins.

        Args:
            graph: Adjacency list, n nodes (3 <= n <= 50).

        Returns:
            Outcome of optimal play.
        """
        n = len(graph)
        # result[mouse][cat][turn]
        result = [[[DRAW] * 2 for _ in range(n)] for _ in range(n)]
        # degree[mouse][cat][turn] = number of unresolved children
        degree = [[[0] * 2 for _ in range(n)] for _ in range(n)]

        # Compute degrees
        for m in range(n):
            for c in range(n):
                degree[m][c][MOUSE_TURN] = len(graph[m])
                degree[m][c][CAT_TURN] = len(graph[c])
                # Cat can't go to hole (node 0)
                if 0 in graph[c]:
                    degree[m][c][CAT_TURN] -= 1

        queue = deque()

        # Initialize terminal states
        for c in range(1, n):  # cat can't be at 0
            for t in range(2):
                # Mouse at hole -> mouse wins
                result[0][c][t] = MOUSE_WIN
                queue.append((0, c, t))
            for t in range(2):
                # Mouse and cat at same position -> cat wins
                result[c][c][t] = CAT_WIN
                queue.append((c, c, t))

        while queue:
            m, c, t = queue.popleft()
            res = result[m][c][t]

            # Find parent states that can transition to (m, c, t)
            if t == MOUSE_TURN:
                # Previous turn was cat's turn; cat moved to c
                prev_turn = CAT_TURN
                for prev_c in graph[c]:
                    if prev_c == 0:
                        continue  # cat can't be at hole
                    for prev_m in [m]:  # mouse didn't move
                        if result[prev_m][prev_c][prev_turn] != DRAW:
                            continue
                        if res == CAT_WIN:
                            # Cat (mover) wins -> parent wins
                            result[prev_m][prev_c][prev_turn] = CAT_WIN
                            queue.append((prev_m, prev_c, prev_turn))
                        else:
                            degree[prev_m][prev_c][prev_turn] -= 1
                            if degree[prev_m][prev_c][prev_turn] == 0:
                                result[prev_m][prev_c][prev_turn] = MOUSE_WIN
                                queue.append((prev_m, prev_c, prev_turn))
            else:
                # Previous turn was mouse's turn; mouse moved to m
                prev_turn = MOUSE_TURN
                for prev_m in graph[m]:
                    for prev_c in [c]:  # cat didn't move
                        if result[prev_m][prev_c][prev_turn] != DRAW:
                            continue
                        if res == MOUSE_WIN:
                            # Mouse (mover) wins -> parent wins
                            result[prev_m][prev_c][prev_turn] = MOUSE_WIN
                            queue.append((prev_m, prev_c, prev_turn))
                        else:
                            degree[prev_m][prev_c][prev_turn] -= 1
                            if degree[prev_m][prev_c][prev_turn] == 0:
                                result[prev_m][prev_c][prev_turn] = CAT_WIN
                                queue.append((prev_m, prev_c, prev_turn))

        return result[1][2][MOUSE_TURN]


# ---------- tests ----------
def test_cat_and_mouse():
    sol = Solution()

    # Example 1: graph=[[2,5],[3],[0,4,5],[1,4,5],[2,3],[0,2,3]]
    # Mouse wins
    assert sol.catMouseGame([[2, 5], [3], [0, 4, 5], [1, 4, 5], [2, 3], [0, 2, 3]]) == 0

    # Example 2: graph=[[1,3],[0],[3],[0,2]]
    assert sol.catMouseGame([[1, 3], [0], [3], [0, 2]]) == 1

    # Simple: 0-1-2 (path). Mouse at 1, cat at 2. Mouse goes to 0 directly.
    assert sol.catMouseGame([[1], [0, 2], [1]]) == 1

    # Cat blocks: triangle 0-1-2. Mouse at 1, cat at 2.
    # Mouse can go to 0 directly if 0 in graph[1].
    assert sol.catMouseGame([[1, 2], [0, 2], [0, 1]]) == 1

    print("All tests passed for 913. Cat and Mouse")


if __name__ == "__main__":
    test_cat_and_mouse()
