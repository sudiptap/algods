"""
838. Push Dominoes
https://leetcode.com/problems/push-dominoes/

Pattern: 19 - Linear DP

---
APPROACH: Two-pass force simulation
- Left-to-right pass: track force from 'R'. Assign decreasing force
  values moving right from each 'R'. Reset on 'L'.
- Right-to-left pass: track force from 'L'. Assign decreasing force
  values moving left from each 'L'. Reset on 'R'.
- Compare forces: if right_force > left_force -> 'R', if less -> 'L',
  if equal -> '.' (forces cancel).

Time: O(n)  Space: O(n)
---
"""


class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        n = len(dominoes)
        forces = [0] * n

        # Left to right: R pushes right with decreasing force
        force = 0
        for i in range(n):
            if dominoes[i] == 'R':
                force = n  # max force
            elif dominoes[i] == 'L':
                force = 0
            else:
                force = max(force - 1, 0)
            forces[i] += force

        # Right to left: L pushes left with decreasing force
        force = 0
        for i in range(n - 1, -1, -1):
            if dominoes[i] == 'L':
                force = n
            elif dominoes[i] == 'R':
                force = 0
            else:
                force = max(force - 1, 0)
            forces[i] -= force

        result = []
        for f in forces:
            if f > 0:
                result.append('R')
            elif f < 0:
                result.append('L')
            else:
                result.append('.')

        return ''.join(result)


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.pushDominoes("RR.L") == "RR.L"
    assert sol.pushDominoes(".L.R...LR..L..") == "LL.RR.LLRRLL.."
    assert sol.pushDominoes("R.") == "RR"
    assert sol.pushDominoes(".L") == "LL"
    assert sol.pushDominoes("...") == "..."
    assert sol.pushDominoes("R...L") == "RR.LL"
    assert sol.pushDominoes("R..L") == "RRLL"

    print("all tests passed")
