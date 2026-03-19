"""
1977. Number of Ways to Separate Numbers (Hard)
https://leetcode.com/problems/number-of-ways-to-separate-numbers/

Given a digit string num, count the number of ways to split it into
non-empty parts where each part has no leading zeros and each part is
>= the previous part (as an integer). Return answer mod 10^9+7.

Pattern: String DP
Approach:
- dp[i][j] = number of ways to partition num[0..i-1] where the last
  number starts at index j (0-indexed) and ends at index i-1.
- The last number is num[j..i-1] with length (i-j).
- Previous number must have length <= (i-j), or same length and be <=.
- Use prefix sums of dp for efficient computation.
- LCP (Longest Common Prefix) array to quickly compare numbers of same length.

Time:  O(n^2)
Space: O(n^2)
"""


class Solution:
    def numberOfCombinations(self, num: str) -> int:
        """Return number of ways to split num into non-decreasing parts.

        Args:
            num: Digit string without leading zeros in parts.

        Returns:
            Count of valid splits mod 10^9 + 7.
        """
        if num[0] == '0':
            return 0

        MOD = 10**9 + 7
        n = len(num)

        # LCP[i][j] = length of longest common prefix of num[i:] and num[j:]
        lcp = [[0] * (n + 1) for _ in range(n + 1)]
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if num[i] == num[j]:
                    lcp[i][j] = lcp[i + 1][j + 1] + 1
                else:
                    lcp[i][j] = 0

        def le(i, j, length):
            """Check if num[i:i+length] <= num[j:j+length]."""
            l = lcp[i][j]
            if l >= length:
                return True
            return num[i + l] <= num[j + l]

        # dp[i][j] = ways where last number is num[j:i+1] (0-indexed, inclusive)
        # Use prefix sums: sdp[i][j] = sum of dp[i][0..j]
        # Actually, let's define:
        # dp[i][l] = ways to split num[0:i] where last number has length l
        # Last number = num[i-l:i]

        # dp[i][l]: last number is num[i-l .. i-1] (length l), i is 1-indexed end
        # Previous number ends at i-l, has length <= l.
        # If prev length < l: sum of dp[i-l][1..l-1]
        # If prev length == l: dp[i-l][l] only if num[i-2l..i-l-1] <= num[i-l..i-1]

        dp = [[0] * (n + 1) for _ in range(n + 1)]
        # prefix[i][l] = sum(dp[i][1], dp[i][2], ..., dp[i][l])
        prefix = [[0] * (n + 1) for _ in range(n + 1)]

        # Base: dp[l][l] = 1 if num[0:l] has no leading zero (num[0] != '0', already checked)
        for l in range(1, n + 1):
            dp[l][l] = 1

        # Fill dp for i from 1 to n
        for i in range(1, n + 1):
            for l in range(1, i + 1):
                # Last number is num[i-l:i], must not have leading zero
                if num[i - l] == '0':
                    dp[i][l] = 0
                    continue

                if l == i:
                    # Already set as base case (the whole prefix is one number)
                    pass
                else:
                    # Previous number ends at position i-l, length <= l
                    # Sum of dp[i-l][1..l-1]
                    dp[i][l] = prefix[i - l][min(l - 1, i - l)] if l - 1 >= 1 else 0
                    dp[i][l] %= MOD

                    # Plus dp[i-l][l] if prev number (same length) <= current
                    if l <= i - l:  # previous number of length l exists
                        if le(i - 2 * l, i - l, l):
                            dp[i][l] = (dp[i][l] + dp[i - l][l]) % MOD

            # Build prefix sums for row i
            for l in range(1, n + 1):
                prefix[i][l] = (prefix[i][l - 1] + dp[i][l]) % MOD

        return prefix[n][n]


# ---------- tests ----------
def test_number_of_combinations():
    sol = Solution()

    # Example 1: "327" -> [3,27], [32,7] invalid (32>7), [327] -> 2
    assert sol.numberOfCombinations("327") == 2

    # Example 2: "094" -> starts with 0, no valid split for "09..." leading zeros
    assert sol.numberOfCombinations("094") == 0

    # Example 3: "0" -> leading zero issue
    assert sol.numberOfCombinations("0") == 0

    # "9999999999999" -> many ways
    assert sol.numberOfCombinations("9999999999999") == 101

    # Single digit
    assert sol.numberOfCombinations("1") == 1

    # Two digits
    assert sol.numberOfCombinations("12") == 2  # [1,2] and [12]

    print("All tests passed for 1977. Number of Ways to Separate Numbers")


if __name__ == "__main__":
    test_number_of_combinations()
