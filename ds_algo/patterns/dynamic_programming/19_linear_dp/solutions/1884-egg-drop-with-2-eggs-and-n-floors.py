"""
1884. Egg Drop With 2 Eggs and N Floors
https://leetcode.com/problems/egg-drop-with-2-eggs-and-n-floors/

Pattern: 19 - Linear DP

---
APPROACH 1 (Math): Find the smallest t such that t*(t+1)/2 >= n.
  With t moves we can check at most t+(t-1)+...+1 = t*(t+1)/2 floors
  because: drop first egg from floor t. If it breaks, linearly check
  t-1 floors below with the second egg (t-1 moves). If it survives,
  next drop from t + (t-1), etc.

APPROACH 2 (DP): dp[k] = min moves to determine critical floor for k floors.
  dp[k] = min over j in [1..k] of max(j-1, 1 + dp[k-j])
  where j-1 = linear scan with 1 egg below j, dp[k-j] = recurse above.

We implement the O(1) math solution.

Time:  O(sqrt(n))
Space: O(1)
---
"""

import math


class Solution:
    def twoEggDrop(self, n: int) -> int:
        """Return the minimum number of moves to determine the critical floor."""
        # Find smallest t where t*(t+1)/2 >= n
        t = math.ceil((-1 + math.sqrt(1 + 8 * n)) / 2)
        return t


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.twoEggDrop(2) == 2
    assert sol.twoEggDrop(6) == 3   # 3*4/2 = 6 >= 6
    assert sol.twoEggDrop(100) == 14  # 14*15/2 = 105 >= 100
    assert sol.twoEggDrop(1) == 1
    assert sol.twoEggDrop(10) == 4   # 4*5/2 = 10 >= 10
    assert sol.twoEggDrop(1000) == 45  # 45*46/2 = 1035 >= 1000

    print("all tests passed")
