"""
526. Beautiful Arrangement (Medium)
https://leetcode.com/problems/beautiful-arrangement/

Given an integer n, return the number of beautiful arrangements you can
construct. A beautiful arrangement is a permutation perm of 1..n such that
for every position i (1-indexed) either:
  - perm[i] is divisible by i, or
  - i is divisible by perm[i].

Pattern: Bitmask DP
- dp[mask] = number of ways to fill the first popcount(mask) positions
  using exactly the numbers indicated by set bits in mask.
- Let pos = popcount(mask) (the next position to fill, 1-indexed).
- For each bit j set in mask, number (j+1) is placed at position pos.
  Check divisibility condition; if satisfied, dp[mask] += dp[mask ^ (1<<j)].
- Base case: dp[0] = 1 (empty arrangement is valid).
- Answer: dp[(1<<n) - 1].

Time:  O(2^n * n)
Space: O(2^n)
"""


class Solution:
    def countArrangement(self, n: int) -> int:
        """Return the count of beautiful arrangements of 1..n.

        Args:
            n: Number of integers, 1 <= n <= 15.

        Returns:
            Number of valid permutations.
        """
        full = 1 << n
        dp = [0] * full
        dp[0] = 1

        for mask in range(1, full):
            pos = bin(mask).count("1")  # 1-indexed position being filled
            for j in range(n):
                if not (mask & (1 << j)):
                    continue
                num = j + 1  # number represented by bit j
                if num % pos == 0 or pos % num == 0:
                    dp[mask] += dp[mask ^ (1 << j)]

        return dp[full - 1]


# ---------- tests ----------
def test_beautiful_arrangement():
    sol = Solution()

    # n=1: only [1] -> 1
    assert sol.countArrangement(1) == 1

    # n=2: [1,2] and [2,1] both valid -> 2
    assert sol.countArrangement(2) == 2

    # n=3: known result is 3
    assert sol.countArrangement(3) == 3

    # n=4: known result is 8
    assert sol.countArrangement(4) == 8

    # n=5: known result is 10
    assert sol.countArrangement(5) == 10

    # n=15: known result is 24679
    assert sol.countArrangement(15) == 24679

    print("All tests passed for 526. Beautiful Arrangement")


if __name__ == "__main__":
    test_beautiful_arrangement()
