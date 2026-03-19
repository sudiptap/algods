"""
3376. Minimum Time to Break Locks I (Medium)

Pattern: 11_bitmask_dp
- n locks with strength[i]. Sword starts at energy X=1, increases by 1 after each lock.
  Time to break lock i with energy X = ceil(strength[i]/X). Find min total time
  over all orderings.

Approach:
- dp[mask] = min time to break the locks indicated by mask, where popcount(mask) locks
  have been broken (so current energy = popcount(mask) + 1... wait, energy starts at 1
  and increases by 1 after each lock, but the problem says energy factor X which might
  increase differently).
  Actually: K starts at 1. After breaking a lock, K increases by 1. So after breaking
  popcount(mask) locks, K = popcount(mask) + 1... no, K = 1 initially, after first lock
  K = 2, etc. So when breaking the (j+1)-th lock, K = j+1. Wait: K starts at 1, used for
  first lock, then K becomes 2 for second, etc.
  So when we've broken popcount(mask) locks, next lock uses K = popcount(mask) + 1.

Complexity:
- Time:  O(2^n * n)
- Space: O(2^n)
"""

from typing import List
from math import ceil


class Solution:
    def findMinimumTime(self, strength: List[int], K: int) -> int:
        n = len(strength)
        INF = float('inf')
        dp = [INF] * (1 << n)
        dp[0] = 0

        for mask in range(1 << n):
            if dp[mask] == INF:
                continue
            cnt = bin(mask).count('1')
            energy = 1 + cnt * K  # After cnt locks broken, energy = 1 + cnt * K

            for i in range(n):
                if mask & (1 << i):
                    continue
                time = ceil(strength[i] / energy)
                new_mask = mask | (1 << i)
                dp[new_mask] = min(dp[new_mask], dp[mask] + time)

        return dp[(1 << n) - 1]


# ---------- Tests ----------
def test():
    sol = Solution()

    # Example 1
    assert sol.findMinimumTime([3, 4, 1], 1) == 4

    # Example 2
    assert sol.findMinimumTime([2, 5, 4], 2) == 5

    print("All tests passed!")


if __name__ == "__main__":
    test()
