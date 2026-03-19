"""
773. Sliding Puzzle
https://leetcode.com/problems/sliding-puzzle/

Pattern: 19 - Linear DP (BFS on states)

---
APPROACH: BFS on board states
- Flatten the 2x3 board to a string. Target = "123450".
- Neighbors of each position in the flattened board:
  0:[1,3], 1:[0,2,4], 2:[1,5], 3:[0,4], 4:[1,3,5], 5:[2,4]
- BFS from initial state, swapping '0' with each neighbor.
- Return number of moves (BFS level) when target is reached, or -1.

Time: O(6! * 6) = O(4320) - at most 720 states  Space: O(6!)
---
"""

from typing import List
from collections import deque


class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        start = "".join(str(x) for row in board for x in row)
        target = "123450"

        if start == target:
            return 0

        neighbors = {
            0: [1, 3], 1: [0, 2, 4], 2: [1, 5],
            3: [0, 4], 4: [1, 3, 5], 5: [2, 4]
        }

        queue = deque([(start, 0)])
        visited = {start}

        while queue:
            state, moves = queue.popleft()
            zero = state.index('0')

            for nei in neighbors[zero]:
                lst = list(state)
                lst[zero], lst[nei] = lst[nei], lst[zero]
                new_state = "".join(lst)

                if new_state == target:
                    return moves + 1

                if new_state not in visited:
                    visited.add(new_state)
                    queue.append((new_state, moves + 1))

        return -1


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.slidingPuzzle([[1, 2, 3], [4, 0, 5]]) == 1
    assert sol.slidingPuzzle([[1, 2, 3], [5, 4, 0]]) == -1
    assert sol.slidingPuzzle([[4, 1, 2], [5, 0, 3]]) == 5
    assert sol.slidingPuzzle([[3, 2, 4], [1, 5, 0]]) == 14
    assert sol.slidingPuzzle([[1, 2, 3], [4, 5, 0]]) == 0

    print("all tests passed")
