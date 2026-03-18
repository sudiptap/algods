"""
1155. Number of Dice Rolls With Target Sum (Medium)
https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/

You have n dice, and each die has k faces numbered from 1 to k. Given three
integers n, k, and target, return the number of possible ways (out of k^n
total ways) to roll the dice so the sum of the face-up numbers equals target.
Return the answer modulo 10^9 + 7.

Pattern: Unbounded Knapsack (rolling 1D DP)
- dp[t] = number of ways to reach sum t using the dice rolled so far.
- For each die, update dp by considering all face values 1..k.
- Transition: new_dp[t] = sum(dp[t - face]) for face in 1..k where t - face >= 0.
- Base case: dp[0] = 1 (one way to reach sum 0 with zero dice).

Time:  O(n * target * k)
Space: O(target)
"""

MOD = 10**9 + 7


class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        """Return number of ways to roll n dice (k faces each) to reach target.

        Args:
            n: Number of dice.
            k: Number of faces per die (1..k).
            target: Desired sum.

        Returns:
            Number of ways modulo 10^9 + 7.
        """
        dp = [0] * (target + 1)
        dp[0] = 1

        for _ in range(n):
            new_dp = [0] * (target + 1)
            for t in range(1, target + 1):
                for face in range(1, k + 1):
                    if t - face >= 0:
                        new_dp[t] = (new_dp[t] + dp[t - face]) % MOD
            dp = new_dp

        return dp[target]


# ---------- tests ----------
def test_num_rolls_to_target():
    sol = Solution()

    # Example 1: 1 die, 6 faces, target 3 -> only face=3 -> 1 way
    assert sol.numRollsToTarget(1, 6, 3) == 1

    # Example 2: 2 dice, 6 faces, target 7 -> 6 ways
    assert sol.numRollsToTarget(2, 6, 7) == 6

    # Example 3: 30 dice, 30 faces, target 500 -> 222616187
    assert sol.numRollsToTarget(30, 30, 500) == 222616187

    # Edge: target too small (n dice, min sum = n)
    assert sol.numRollsToTarget(3, 6, 1) == 0

    # Edge: target too large (n dice, max sum = n*k)
    assert sol.numRollsToTarget(2, 6, 13) == 0

    # 2 dice, 2 faces, target 3 -> (1,2) and (2,1) -> 2 ways
    assert sol.numRollsToTarget(2, 2, 3) == 2

    print("All tests passed for 1155. Number of Dice Rolls With Target Sum")


if __name__ == "__main__":
    test_num_rolls_to_target()
