"""
920. Number of Music Playlists (Hard)
https://leetcode.com/problems/number-of-music-playlists/

Given n unique songs, create a playlist of goal songs such that every song is
played at least once, and a song can only be replayed if at least k other songs
have been played since its last play. Return count modulo 10^9+7.

Pattern: Counting / Combinatorial DP
Approach:
- dp[i][j] = number of playlists of length i using exactly j unique songs.
- Transition:
  - Add a new song: dp[i][j] = dp[i-1][j-1] * (n - (j-1)) — pick from unused songs.
  - Replay an old song: dp[i][j] += dp[i-1][j] * max(j - k, 0) — replay any of
    j songs except the last k played.
- Answer: dp[goal][n].

Time:  O(goal * n)
Space: O(goal * n), optimizable to O(n).
"""

MOD = 10**9 + 7


class Solution:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        """Return number of valid playlists of length goal with n songs.

        Args:
            n: Number of unique songs.
            goal: Playlist length.
            k: Minimum gap before replaying a song.

        Returns:
            Count modulo 10^9+7.
        """
        # dp[j] = playlists of current length using exactly j unique songs
        dp = [0] * (n + 1)
        dp[0] = 1

        for i in range(1, goal + 1):
            # Update in reverse to avoid using updated values
            new_dp = [0] * (n + 1)
            for j in range(1, n + 1):
                # Add new song
                new_dp[j] = dp[j - 1] * (n - j + 1) % MOD
                # Replay old song
                if j > k:
                    new_dp[j] = (new_dp[j] + dp[j] * (j - k)) % MOD
            dp = new_dp

        return dp[n]


# ---------- tests ----------
def test_num_music_playlists():
    sol = Solution()

    # Example 1: n=3, goal=3, k=1 -> 6 (all permutations of 3 songs)
    assert sol.numMusicPlaylists(3, 3, 1) == 6

    # Example 2: n=2, goal=3, k=0 -> 6
    # Playlists: [1,1,2],[1,2,1],[1,2,2],[2,1,1],[2,1,2],[2,2,1]
    assert sol.numMusicPlaylists(2, 3, 0) == 6

    # Example 3: n=2, goal=3, k=1 -> 2
    # [1,2,1] and [2,1,2]
    assert sol.numMusicPlaylists(2, 3, 1) == 2

    # n=1, goal=1, k=0 -> 1
    assert sol.numMusicPlaylists(1, 1, 0) == 1

    # n=1, goal=3, k=0 -> 1 (play same song 3 times)
    assert sol.numMusicPlaylists(1, 3, 0) == 1

    print("All tests passed for 920. Number of Music Playlists")


if __name__ == "__main__":
    test_num_music_playlists()
