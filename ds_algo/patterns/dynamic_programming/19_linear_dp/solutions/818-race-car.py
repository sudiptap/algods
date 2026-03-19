"""
818. Race Car
https://leetcode.com/problems/race-car/

Pattern: 19 - Linear DP

---
APPROACH: BFS on (position, speed) states
- Start at position 0, speed 1.
- Accelerate: position += speed, speed *= 2.
- Reverse: speed = -1 if speed > 0, else 1.
- BFS to find minimum instructions to reach target.
- Pruning: skip states where position < 0 or position > 2*target
  (going too far is never optimal beyond a bound).

Time: O(target * log(target))  Space: O(target * log(target))
---
"""

from collections import deque


class Solution:
    def racecar(self, target: int) -> int:
        queue = deque([(0, 1, 0)])  # (position, speed, moves)
        visited = {(0, 1)}

        while queue:
            pos, speed, moves = queue.popleft()

            # Accelerate
            new_pos = pos + speed
            new_speed = speed * 2
            if new_pos == target:
                return moves + 1
            if (new_pos, new_speed) not in visited and 0 < new_pos < 2 * target:
                visited.add((new_pos, new_speed))
                queue.append((new_pos, new_speed, moves + 1))

            # Reverse
            new_speed = -1 if speed > 0 else 1
            if (pos, new_speed) not in visited and 0 < pos < 2 * target:
                visited.add((pos, new_speed))
                queue.append((pos, new_speed, moves + 1))

        return -1  # should not reach here for valid input


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.racecar(3) == 2     # AA -> pos=3
    assert sol.racecar(6) == 5     # AAARA -> pos=7, R, A -> 6
    assert sol.racecar(1) == 1
    assert sol.racecar(4) == 5
    assert sol.racecar(5) == 7
    assert sol.racecar(2) == 4     # AARA

    print("all tests passed")
