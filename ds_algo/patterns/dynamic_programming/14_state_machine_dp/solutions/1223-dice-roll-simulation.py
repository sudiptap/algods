"""
1223. Dice Roll Simulation (Hard)

Pattern: 14_state_machine_dp
- Count sequences of n dice rolls where face j doesn't appear more than rollMax[j] consecutive times.

Approach:
- dp[i][j][k] = number of sequences of length i, ending with face j appearing
  k consecutive times at the end.
- Base: dp[1][j][1] = 1 for all j in [0..5].
- Transition for roll i:
  - Extend same face: dp[i][j][k] = dp[i-1][j][k-1] if k > 1 and k <= rollMax[j].
  - Start new face: dp[i][j][1] = sum of dp[i-1][j'][k'] for all j' != j, all valid k'.
- Optimize: precompute sum for each i-1, then dp[i][j][1] = total_sum - sum_over_k(dp[i-1][j][k]).

Complexity:
- Time:  O(n * 6 * max_roll), with max_roll up to 15
- Space: O(6 * max_roll) with rolling array
"""

from typing import List

MOD = 10**9 + 7


class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        # dp[j][k] = ways ending with face j, k consecutive
        # k ranges from 1 to rollMax[j]
        max_k = max(rollMax)
        dp = [[0] * (max_k + 1) for _ in range(6)]

        # Base: first roll
        for j in range(6):
            dp[j][1] = 1

        for i in range(2, n + 1):
            new_dp = [[0] * (max_k + 1) for _ in range(6)]
            total = 0
            for j in range(6):
                for k in range(1, rollMax[j] + 1):
                    total = (total + dp[j][k]) % MOD

            for j in range(6):
                # Start new streak of face j: sum of all dp except face j
                face_sum = 0
                for k in range(1, rollMax[j] + 1):
                    face_sum = (face_sum + dp[j][k]) % MOD
                new_dp[j][1] = (total - face_sum) % MOD

                # Extend streak of face j
                for k in range(2, rollMax[j] + 1):
                    new_dp[j][k] = dp[j][k - 1]

            dp = new_dp

        result = 0
        for j in range(6):
            for k in range(1, rollMax[j] + 1):
                result = (result + dp[j][k]) % MOD
        return result


# ---------- Tests ----------
def test():
    sol = Solution()

    # Example 1: n=2, rollMax=[1,1,2,2,2,3] -> 34
    assert sol.dieSimulator(2, [1, 1, 2, 2, 2, 3]) == 34

    # Example 2: n=2, rollMax=[1,1,1,1,1,1] -> 30
    assert sol.dieSimulator(2, [1, 1, 1, 1, 1, 1]) == 30

    # Example 3: n=3, rollMax=[1,1,1,2,2,3] -> 181
    assert sol.dieSimulator(3, [1, 1, 1, 2, 2, 3]) == 181

    # n=1: always 6
    assert sol.dieSimulator(1, [1, 1, 1, 1, 1, 1]) == 6

    print("All tests passed!")


if __name__ == "__main__":
    test()
