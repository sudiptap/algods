"""
664. Strange Printer (Hard)

A strange printer has two special properties:
- It can only print a sequence of the same character each time.
- At each turn, it can start and stop printing at any position, and will
  overwrite the existing characters.

Given a string s, return the minimum number of turns the printer needs to
print it.

Pattern: Interval DP
- dp[i][j] = minimum turns to print s[i..j].
- Base case: dp[i][i] = 1 (single character needs 1 turn).
- If s[i] == s[j], dp[i][j] = dp[i][j-1] because we can extend the print
  of s[i] to cover position j for free.
- Otherwise, dp[i][j] = min(dp[i][k] + dp[k+1][j]) for all k in [i, j-1].

Time: O(n^3)
Space: O(n^2)
"""


class Solution:
    def strangePrinter(self, s: str) -> int:
        """Return the minimum number of turns to print string s."""
        if not s:
            return 0

        # Remove consecutive duplicates since they don't affect the answer
        filtered = [s[0]]
        for c in s[1:]:
            if c != filtered[-1]:
                filtered.append(c)
        s = filtered
        n = len(s)

        # dp[i][j] = min turns to print s[i..j]
        dp = [[0] * n for _ in range(n)]

        for i in range(n):
            dp[i][i] = 1

        # Fill by increasing interval length
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                # Worst case: print s[j] separately
                dp[i][j] = dp[i][j - 1] + 1
                # Try merging: if s[k] == s[j] for some k in [i, j-1],
                # we can extend the print at k to cover j
                for k in range(i, j):
                    if s[k] == s[j]:
                        cost = dp[i][k] + (dp[k + 1][j - 1] if k + 1 <= j - 1 else 0)
                        dp[i][j] = min(dp[i][j], cost)

        return dp[0][n - 1]


def run_tests():
    sol = Solution()

    # Example 1: "aaabbb" -> 2 turns (print "aaa", then "bbb")
    assert sol.strangePrinter("aaabbb") == 2, f"Expected 2, got {sol.strangePrinter('aaabbb')}"

    # Example 2: "aba" -> 2 turns (print "aaa", then overwrite middle with "b")
    assert sol.strangePrinter("aba") == 2, f"Expected 2, got {sol.strangePrinter('aba')}"

    # Single character
    assert sol.strangePrinter("a") == 1, f"Expected 1, got {sol.strangePrinter('a')}"

    # All same characters
    assert sol.strangePrinter("aaaa") == 1, f"Expected 1, got {sol.strangePrinter('aaaa')}"

    # Empty string
    assert sol.strangePrinter("") == 0, f"Expected 0, got {sol.strangePrinter('')}"

    # "abcabc" -> 5 turns
    assert sol.strangePrinter("abcabc") == 5, f"Expected 5, got {sol.strangePrinter('abcabc')}"

    # "abab" -> 3 turns
    assert sol.strangePrinter("abab") == 3, f"Expected 3, got {sol.strangePrinter('abab')}"

    print("All tests passed for 664. Strange Printer!")


if __name__ == "__main__":
    run_tests()
