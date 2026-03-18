"""
1025. Divisor Game
https://leetcode.com/problems/divisor-game/

Pattern: 01 - Fibonacci Pattern

---
APPROACH 1: Math observation
- Alice wins if and only if n is even.
- Proof sketch: if n is odd, every divisor x of n is also odd, so n - x is even
  (opponent gets even). If n is even, Alice picks x = 1, giving opponent odd.
  By induction, even = win for the player whose turn it is, odd = loss.

Time:  O(1)
Space: O(1)

APPROACH 2: Bottom-up DP
- dp[i] = True if the player whose turn it is wins with number i.
- dp[1] = False (no valid move).
- dp[i] = any(not dp[i - x] for x in 1..i-1 if i % x == 0)

Time:  O(n * sqrt(n))  Space: O(n)
---
"""


# ---------- Approach 1: Math ----------
class Solution:
    def divisorGame(self, n: int) -> bool:
        """Alice wins iff n is even."""
        return n % 2 == 0


# ---------- Approach 2: DP ----------
class SolutionDP:
    def divisorGame(self, n: int) -> bool:
        """Bottom-up DP: dp[i] = can current player win with value i."""
        if n == 1:
            return False
        dp = [False] * (n + 1)
        # dp[1] = False already
        for i in range(2, n + 1):
            for x in range(1, i):
                if i % x == 0 and not dp[i - x]:
                    dp[i] = True
                    break
        return dp[n]


# ---------- Tests ----------
if __name__ == "__main__":
    for Sol in [Solution, SolutionDP]:
        sol = Sol()

        assert sol.divisorGame(2) is True   # Alice picks 1, Bob gets 1, Bob loses
        assert sol.divisorGame(3) is False  # Alice picks 1, Bob gets 2, Bob wins
        assert sol.divisorGame(1) is False
        assert sol.divisorGame(4) is True
        assert sol.divisorGame(100) is True
        assert sol.divisorGame(7) is False

        print(f"{Sol.__name__}: all tests passed")
