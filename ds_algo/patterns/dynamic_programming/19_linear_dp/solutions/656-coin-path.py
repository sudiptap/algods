"""
656. Coin Path
https://leetcode.com/problems/coin-path/

Pattern: 19 - Linear DP

---
APPROACH: DP from right to left for min cost, reconstruct lexicographically smallest path
- dp[i] = minimum cost to reach index n-1 from index i.
- Transition: dp[i] = A[i] + min(dp[j]) for j in [i+1, i+B], A[j] != -1.
- Process right to left. Track next[i] for path reconstruction.
- For lexicographically smallest: when costs tie, pick largest j (rightmost)
  when iterating j from i+B down to i+1, update on <=.
  Actually, iterate j from i+B down to i+1 and use <= so we keep the
  smallest next index (last update wins with <=, but we want smallest j,
  so iterate from large to small and use <=).
  Wait: we want lex smallest path. At each position, we want the smallest
  next index among ties. Iterate j from i+B downto i+1, keep track of
  best with <=, so the last update (smallest j) wins.

Time: O(n * B)  Space: O(n)
---
"""

from typing import List


class Solution:
    def cheapestJump(self, coins: List[int], maxJump: int) -> List[int]:
        n = len(coins)
        if n == 0 or coins[0] == -1 or coins[-1] == -1:
            return []

        INF = float('inf')
        dp = [INF] * n
        nxt = [-1] * n
        dp[n - 1] = coins[n - 1]

        for i in range(n - 2, -1, -1):
            if coins[i] == -1:
                continue
            # Iterate from largest j to smallest j; use <= to prefer smallest j on tie
            for j in range(min(i + maxJump, n - 1), i, -1):
                if dp[j] == INF:
                    continue
                cost = coins[i] + dp[j]
                if cost <= dp[i]:
                    dp[i] = cost
                    nxt[i] = j

        if dp[0] == INF:
            return []

        # Reconstruct path
        path = []
        idx = 0
        while idx != -1:
            path.append(idx + 1)  # 1-indexed
            idx = nxt[idx]

        return path


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.cheapestJump([1, 2, 4, -1, 2], 2) == [1, 3, 5]
    assert sol.cheapestJump([1, 2, 4, -1, 2], 1) == []  # blocked by -1
    assert sol.cheapestJump([1], 1) == [1]
    assert sol.cheapestJump([1, 2], 1) == [1, 2]
    assert sol.cheapestJump([1, 2, 3], 2) == [1, 3]  # skip index 2 for cheaper path
    assert sol.cheapestJump([-1], 1) == []

    print("all tests passed")
