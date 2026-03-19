"""
3320. Count The Number of Winning Sequences (Hard)

Pattern: 14_state_machine_dp
- Alice plays a string of F/W/E. Bob must choose moves to beat Alice overall.
  Bob cannot make the same move in consecutive rounds. Count Bob's winning sequences.

Approach:
- Scoring: F beats E, E beats W, W beats F (rock-paper-scissors style).
- dp[i][diff][last] = number of ways for Bob after round i with score difference diff
  and last move = last.
- diff ranges from -n to n; offset by n. Bob wins if final diff > 0.
- Moves: 0=F, 1=W, 2=E. Round score for Bob move b vs Alice move a:
  +1 if Bob wins, -1 if Alice wins, 0 if tie.

Complexity:
- Time:  O(n * 2n * 3) = O(n^2)
- Space: O(n * 3) with rolling array
"""

MOD = 10**9 + 7


class Solution:
    def countWinningSequences(self, s: str) -> int:
        n = len(s)
        # Map chars to indices
        char_to_idx = {'F': 0, 'W': 1, 'E': 2}

        # score[bob_move][alice_move]: +1 bob wins, -1 alice wins, 0 tie
        # F beats E, E beats W, W beats F
        score_table = [[0] * 3 for _ in range(3)]
        score_table[0][2] = 1; score_table[0][1] = -1  # F vs E=+1, F vs W=-1
        score_table[1][0] = 1; score_table[1][2] = -1  # W vs F=+1, W vs E=-1
        score_table[2][1] = 1; score_table[2][0] = -1  # E vs W=+1, E vs F=-1

        offset = n  # diff ranges from -n to n, index = diff + offset
        size = 2 * n + 1

        # dp[diff_idx][last_move] = count
        dp = [[0] * 3 for _ in range(size)]

        # First round
        a = char_to_idx[s[0]]
        for b in range(3):
            sc = score_table[b][a]
            dp[sc + offset][b] = 1

        for i in range(1, n):
            a = char_to_idx[s[i]]
            new_dp = [[0] * 3 for _ in range(size)]
            for d in range(size):
                for prev_b in range(3):
                    if dp[d][prev_b] == 0:
                        continue
                    for b in range(3):
                        if b == prev_b:
                            continue
                        sc = score_table[b][a]
                        nd = d + sc
                        if 0 <= nd < size:
                            new_dp[nd][b] = (new_dp[nd][b] + dp[d][prev_b]) % MOD
            dp = new_dp

        # Sum all states with diff > 0
        ans = 0
        for d in range(offset + 1, size):
            for b in range(3):
                ans = (ans + dp[d][b]) % MOD

        return ans


# ---------- Tests ----------
def test():
    sol = Solution()

    # Example 1
    assert sol.countWinningSequences("FFF") == 3

    # Example 2
    assert sol.countWinningSequences("FWEFW") == 18

    # Single round
    assert sol.countWinningSequences("F") == 1  # Only W beats F

    print("All tests passed!")


if __name__ == "__main__":
    test()
