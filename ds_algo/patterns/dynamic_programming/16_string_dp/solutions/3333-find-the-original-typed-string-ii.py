"""
3333. Find the Original Typed String II (Hard)

Pattern: 16_string_dp
- A string was typed but keys may have been held causing repeated chars. Given the
  typed string word and integer k, find the number of possible original strings
  of length >= k.

Approach:
- Group consecutive identical chars: groups = [(char, count), ...].
- Each group of count c can produce 1..c chars in original (at least 1).
- Total original strings = product of group counts. We need those with length >= k.
- dp to count strings of length < k, then subtract from total.
- dp[j] = number of ways to have total length j after processing some groups.
- For each group with count c, new_dp[j] += dp[j - t] for t in 1..c.
- Use prefix sums for efficient updates.

Complexity:
- Time:  O(k * number_of_groups) amortized with prefix sums on group sizes
- Space: O(k)
"""

MOD = 10**9 + 7


class Solution:
    def possibleStringCount(self, word: str, k: int) -> int:
        # Build groups
        groups = []
        i = 0
        while i < len(word):
            j = i
            while j < len(word) and word[j] == word[i]:
                j += 1
            groups.append(j - i)
            i = j

        g = len(groups)
        # Total possible strings (any length >= g)
        total = 1
        for c in groups:
            total = total * c % MOD

        # If minimum length (g) >= k, all strings are valid
        if g >= k:
            return total

        # Count strings with length < k using dp
        # dp[j] = ways to form total length j using groups processed so far
        dp = [0] * k
        dp[0] = 1

        for c in groups:
            # For this group, we pick 1..c chars
            # new_dp[j] = sum of dp[j-t] for t=1..c
            # Use prefix sums
            prefix = [0] * (k + 1)
            for j in range(k):
                prefix[j + 1] = (prefix[j] + dp[j]) % MOD

            new_dp = [0] * k
            for j in range(k):
                # sum dp[j-c..j-1] = prefix[j] - prefix[max(0, j-c)]
                lo = max(0, j - c)
                new_dp[j] = (prefix[j] - prefix[lo]) % MOD

            dp = new_dp

        less_than_k = sum(dp) % MOD
        return (total - less_than_k) % MOD


# ---------- Tests ----------
def test():
    sol = Solution()

    # Example 1
    assert sol.possibleStringCount("aabbccdd", 7) == 5

    # Example 2
    assert sol.possibleStringCount("aabbccdd", 8) == 1

    # Example 3
    assert sol.possibleStringCount("aaabbb", 3) == 8

    print("All tests passed!")


if __name__ == "__main__":
    test()
