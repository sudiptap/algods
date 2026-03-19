"""
903. Valid Permutations for DI Sequence (Hard)
https://leetcode.com/problems/valid-permutations-for-di-sequence/

Given a string s of 'D' and 'I' characters, count the number of permutations
perm of 0..n (where n = len(s)) such that:
- s[i] == 'D' implies perm[i] > perm[i+1]
- s[i] == 'I' implies perm[i] < perm[i+1]

Pattern: Counting / Combinatorial DP
Approach:
- dp[j] = number of valid permutations of {0..i} where the last element has
  relative rank j (j elements below it among those placed so far).
- Transition using prefix/suffix sums:
  - If s[i] == 'I': dp_new[j] = sum(dp[0..j-1]) — previous rank was lower.
  - If s[i] == 'D': dp_new[j] = sum(dp[j..i]) — previous rank was higher or equal.
- This gives O(n^2) with running sums.

Time:  O(n^2)
Space: O(n)
"""

MOD = 10**9 + 7


class Solution:
    def numPermsDISequence(self, s: str) -> int:
        """Return count of valid permutations for DI sequence mod 10^9+7.

        Args:
            s: String of 'D' and 'I', 1 <= len(s) <= 200.

        Returns:
            Number of valid permutations modulo 10^9+7.
        """
        n = len(s)
        dp = [1]  # i=0: single element, rank 0

        for i in range(n):
            new_dp = [0] * (i + 2)
            if s[i] == 'I':
                # New rank j gets contributions from old ranks 0..j-1
                prefix = 0
                for j in range(i + 2):
                    new_dp[j] = prefix
                    if j <= i:
                        prefix = (prefix + dp[j]) % MOD
            else:  # 'D'
                # New rank j gets contributions from old ranks j..i
                suffix = 0
                for j in range(i, -1, -1):
                    suffix = (suffix + dp[j]) % MOD
                    new_dp[j] = suffix
            dp = new_dp

        return sum(dp) % MOD


# ---------- tests ----------
def test_valid_permutations_di():
    sol = Solution()

    # Example 1: "DID" -> 5
    assert sol.numPermsDISequence("DID") == 5

    # "D" -> [1,0] -> 1
    assert sol.numPermsDISequence("D") == 1

    # "I" -> [0,1] -> 1
    assert sol.numPermsDISequence("I") == 1

    # "DD" -> [2,1,0] -> 1
    assert sol.numPermsDISequence("DD") == 1

    # "II" -> [0,1,2] -> 1
    assert sol.numPermsDISequence("II") == 1

    # "DI" -> [1,0,2], [2,0,1] -> 2
    assert sol.numPermsDISequence("DI") == 2

    # "ID" -> [0,2,1], [1,2,0] -> 2
    assert sol.numPermsDISequence("ID") == 2

    print("All tests passed for 903. Valid Permutations for DI Sequence")


if __name__ == "__main__":
    test_valid_permutations_di()
