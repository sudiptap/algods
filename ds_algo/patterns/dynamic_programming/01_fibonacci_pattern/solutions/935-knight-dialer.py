"""
935. Knight Dialer
https://leetcode.com/problems/knight-dialer/

Pattern: 01 - Fibonacci Pattern

---
APPROACH: DP with transition map
- Map each digit to the digits reachable by a knight move.
- dp[digit] = number of distinct numbers ending at that digit.
- For each step, new_dp[digit] = sum(dp[prev] for prev in moves_to[digit]).
- Answer = sum(dp[digit] for all digits) after n-1 steps.

Time: O(10 * n)  Space: O(1) — only 10 states
---
"""

MOD = 10**9 + 7

# moves_to[d] = list of digits from which a knight can jump TO d
MOVES = {
    0: [4, 6],
    1: [6, 8],
    2: [7, 9],
    3: [4, 8],
    4: [0, 3, 9],
    5: [],
    6: [0, 1, 7],
    7: [2, 6],
    8: [1, 3],
    9: [2, 4],
}


class Solution:
    def knightDialer(self, n: int) -> int:
        """Return the number of distinct phone numbers of length n a knight can dial."""
        dp = [1] * 10  # length 1: each digit is one number

        for _ in range(n - 1):
            new_dp = [0] * 10
            for digit in range(10):
                for prev in MOVES[digit]:
                    new_dp[digit] = (new_dp[digit] + dp[prev]) % MOD
            dp = new_dp

        return sum(dp) % MOD


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.knightDialer(1) == 10
    assert sol.knightDialer(2) == 20
    assert sol.knightDialer(3131) == 136006598
    assert sol.knightDialer(3) == 46
    assert sol.knightDialer(4) == 104

    print("all tests passed")
