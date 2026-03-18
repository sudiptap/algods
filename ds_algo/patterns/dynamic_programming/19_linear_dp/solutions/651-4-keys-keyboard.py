"""
651. 4 Keys Keyboard (Medium)

Imagine you have a special keyboard with the following keys:
- Key 1: (A) - Print one 'A' on screen.
- Key 2: (Ctrl-A) - Select the whole screen.
- Key 3: (Ctrl-C) - Copy selection to buffer.
- Key 4: (Ctrl-V) - Print buffer on screen (appending after what's already there).

Given n keystrokes, find the maximum number of 'A's you can print.

Pattern: Linear DP
- dp[i] = maximum number of A's printable with exactly i keystrokes.
- For each i, we either just type A (dp[i] = dp[i-1] + 1),
  or we try every breakpoint j where we do Ctrl-A, Ctrl-C at step j,
  then paste (i - j - 1) times, multiplying dp[j] by (i - j - 1).

Time: O(n^2)
Space: O(n)
"""


class Solution:
    def maxA(self, n: int) -> int:
        """Return the maximum number of 'A's printable with n keystrokes."""
        if n <= 0:
            return 0

        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            # Option 1: just press 'A'
            dp[i] = dp[i - 1] + 1
            # Option 2: try Ctrl-A + Ctrl-C at step j, then paste (i-j-1) times
            # j ranges from 1..i-3 (need at least 3 keys for select, copy, paste)
            for j in range(1, i - 2):
                pastes = i - j - 1  # number of Ctrl-V presses (subtract 2 for Ctrl-A + Ctrl-C)
                dp[i] = max(dp[i], dp[j] * pastes)

        return dp[n]


def run_tests():
    sol = Solution()

    # Basic cases
    assert sol.maxA(1) == 1, f"Expected 1, got {sol.maxA(1)}"
    assert sol.maxA(2) == 2, f"Expected 2, got {sol.maxA(2)}"
    assert sol.maxA(3) == 3, f"Expected 3, got {sol.maxA(3)}"

    # n=4: AAAA (4 A's) or A,Ctrl-A,Ctrl-C,Ctrl-V = 2 -> best is 4
    assert sol.maxA(4) == 4, f"Expected 4, got {sol.maxA(4)}"

    # n=7: A,A,A,Ctrl-A,Ctrl-C,Ctrl-V,Ctrl-V = 3*3 = 9
    assert sol.maxA(7) == 9, f"Expected 9, got {sol.maxA(7)}"

    # n=0 edge case
    assert sol.maxA(0) == 0, f"Expected 0, got {sol.maxA(0)}"

    # n=10: AAAA, Ctrl-A, Ctrl-C, Ctrl-V x4 = 4*5 = 20
    assert sol.maxA(10) == 20, f"Expected 20, got {sol.maxA(10)}"

    print("All tests passed for 651. 4 Keys Keyboard!")


if __name__ == "__main__":
    run_tests()
