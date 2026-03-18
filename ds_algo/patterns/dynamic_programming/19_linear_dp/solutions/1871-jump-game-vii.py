"""
1871. Jump Game VII
https://leetcode.com/problems/jump-game-vii/

Pattern: 19 - Linear DP (Sliding Window / Prefix Sum)

---
APPROACH: DP with prefix sum of reachable positions
- dp[i] = True if index i is reachable.
- For each i, we need to know if any index in [i-maxJump, i-minJump] is
  reachable. Checking each one individually is O(n * maxJump).
- Optimization: keep a running count of reachable indices in the window.
  As i advances, add dp[i-minJump] entering the window and subtract
  dp[i-maxJump-1] leaving the window.
- dp[i] = (s[i] == '0') and (window_count > 0).

Time:  O(n)
Space: O(n)
---
"""


class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        """Return True if we can reach the last index starting from index 0."""
        n = len(s)
        if s[-1] == '1':
            return False

        dp = [False] * n
        dp[0] = True
        count = 0  # number of reachable indices in current window

        for i in range(1, n):
            # index (i - minJump) enters the window
            if i - minJump >= 0 and dp[i - minJump]:
                count += 1
            # index (i - maxJump - 1) leaves the window
            if i - maxJump - 1 >= 0 and dp[i - maxJump - 1]:
                count -= 1

            dp[i] = (s[i] == '0') and (count > 0)

        return dp[-1]


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.canReach("011010", 2, 3) == True
    assert sol.canReach("01101110", 2, 3) == False
    assert sol.canReach("0", 1, 1) == True
    assert sol.canReach("00", 1, 1) == True
    assert sol.canReach("01", 1, 1) == False
    # Can jump exactly maxJump to land on last 0
    assert sol.canReach("00000", 2, 4) == True
    # All zeros, large jump range
    assert sol.canReach("0000000", 1, 6) == True

    print("all tests passed")
