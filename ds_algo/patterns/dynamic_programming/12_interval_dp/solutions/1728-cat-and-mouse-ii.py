"""
1728. Cat and Mouse II
https://leetcode.com/problems/cat-and-mouse-ii/

Pattern: 12 - Interval DP / Game DP

---
APPROACH: Game DP on grid with positions and turns
- State: (mouse_pos, cat_pos, turn) where turn indicates whose move it is.
- Mouse wins if it reaches food. Cat wins if it reaches food or catches mouse.
- Draw if game exceeds threshold moves (use ~128 as upper bound since grid <= 8x8).
- Mouse moves up to mouseJump cells, cat up to catJump cells (in 4 directions).
- Mouse moves first (turn 0 = mouse, turn 1 = cat).
- Memoized game: mouse tries to find any winning move, cat tries to prevent it.

Time: O(rows^2 * cols^2 * turns * max_jump) ~ O(64 * 64 * 128 * 8)
Space: O(rows^2 * cols^2 * turns)
---
"""

from typing import List
from functools import lru_cache


class Solution:
    def canMouseWin(self, grid: List[str], catJump: int, mouseJump: int) -> bool:
        rows, cols = len(grid), len(grid[0])

        # Find positions
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 'C':
                    cat_start = (r, c)
                elif grid[r][c] == 'M':
                    mouse_start = (r, c)
                elif grid[r][c] == 'F':
                    food = (r, c)

        MAX_TURNS = rows * cols * 2  # Upper bound for draw detection

        @lru_cache(maxsize=None)
        def dp(mouse, cat, turn):
            # turn: 0 = mouse's turn, 1 = cat's turn
            if turn >= MAX_TURNS:
                return False  # Draw = cat wins
            if mouse == cat:
                return False  # Cat catches mouse
            if cat == food:
                return False  # Cat wins
            if mouse == food:
                return True   # Mouse wins

            dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

            if turn % 2 == 0:  # Mouse's turn - mouse wants True
                jump = mouseJump
                for dr, dc in dirs:
                    for step in range(1, jump + 1):
                        nr, nc = mouse[0] + dr * step, mouse[1] + dc * step
                        if not (0 <= nr < rows and 0 <= nc < cols) or grid[nr][nc] == '#':
                            break
                        if dp((nr, nc), cat, turn + 1):
                            return True
                # Mouse can also stay
                return dp(mouse, cat, turn + 1)
            else:  # Cat's turn - cat wants False
                jump = catJump
                for dr, dc in dirs:
                    for step in range(1, jump + 1):
                        nr, nc = cat[0] + dr * step, cat[1] + dc * step
                        if not (0 <= nr < rows and 0 <= nc < cols) or grid[nr][nc] == '#':
                            break
                        if not dp(mouse, (nr, nc), turn + 1):
                            return False
                # Cat can also stay
                return dp(mouse, cat, turn + 1)

        return dp(mouse_start, cat_start, 0)


# --- Tests ---
def test():
    sol = Solution()

    assert sol.canMouseWin(["####F", "#C...", "M...."], 1, 2) == True
    assert sol.canMouseWin(["M.C...F"], 1, 4) == True
    assert sol.canMouseWin(["M.C...F"], 1, 1) == False
    assert sol.canMouseWin(["C...#", "...#F", "....#", "M...."], 2, 5) == False

    print("All tests passed!")


if __name__ == "__main__":
    test()
