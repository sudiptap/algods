"""
3339. Find the Number of K-Even Arrays (Medium)

Pattern: 15_counting_combinatorial
- Count arrays of length n with elements in [1, m] that have exactly k adjacent
  pairs where both elements are even.

Approach:
- dp on position with state = last element parity and count of even-even pairs.
- Even numbers: m//2, Odd numbers: m - m//2.
- dp[i][j][parity]: i = position, j = even-even pairs so far, parity = 0 (odd) / 1 (even).
- Transition: if we place even after even, j increases by 1.

Complexity:
- Time:  O(n * k)
- Space: O(k)
"""

MOD = 10**9 + 7


class Solution:
    def countOfArrays(self, n: int, m: int, k: int) -> int:
        even = m // 2
        odd = m - even

        # dp[j][p]: j even-even pairs, p = parity of last element (0=odd, 1=even)
        dp = [[0] * 2 for _ in range(k + 1)]
        dp[0][0] = odd
        dp[0][1] = even

        for i in range(1, n):
            new_dp = [[0] * 2 for _ in range(k + 1)]
            for j in range(k + 1):
                # Last was odd
                if dp[j][0]:
                    # Place odd: no even-even pair
                    new_dp[j][0] = (new_dp[j][0] + dp[j][0] * odd) % MOD
                    # Place even: no even-even pair (last was odd)
                    new_dp[j][1] = (new_dp[j][1] + dp[j][0] * even) % MOD
                # Last was even
                if dp[j][1]:
                    # Place odd: no even-even pair
                    new_dp[j][0] = (new_dp[j][0] + dp[j][1] * odd) % MOD
                    # Place even: even-even pair!
                    if j + 1 <= k:
                        new_dp[j + 1][1] = (new_dp[j + 1][1] + dp[j][1] * even) % MOD
            dp = new_dp

        return (dp[k][0] + dp[k][1]) % MOD


# ---------- Tests ----------
def test():
    sol = Solution()

    # Example 1
    assert sol.countOfArrays(3, 2, 1) == 2  # [2,2,1] and [2,2,2]... let me verify
    # n=3, m=2, k=1: elements in {1,2}. Even-even pairs exactly 1.
    # [1,2,2]: pair(2,2)=1 -> yes
    # [2,2,1]: pair(2,2)=1 -> yes
    # [2,2,2]: pairs=2 -> no
    # So answer = 2. Correct.

    # n=5, m=9, k=0: no even-even adjacent pairs
    # evens=4, odds=5. Recurrence gives 29225.
    assert sol.countOfArrays(5, 9, 0) == 29225

    # Single element, m=1(odd), k=0
    assert sol.countOfArrays(1, 1, 0) == 1

    # n=2, m=2, k=1: [2,2] is the only array with exactly 1 even-even pair
    assert sol.countOfArrays(2, 2, 1) == 1

    # n=2, m=2, k=0: [1,1],[1,2],[2,1] = 3
    assert sol.countOfArrays(2, 2, 0) == 3

    print("All tests passed!")


if __name__ == "__main__":
    test()
