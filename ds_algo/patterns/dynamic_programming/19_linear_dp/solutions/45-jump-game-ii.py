"""
45. Jump Game II
https://leetcode.com/problems/jump-game-ii/

Pattern: 19 - Linear DP (greedy optimal)

---
APPROACH 1: Greedy (BFS-like, optimal for interviews)
- Think of it as BFS by levels: each "level" = one jump
- Track the farthest we can reach in current jump window [start, end]
- When we pass current end, we must take another jump
- Variables: jumps, current_end, farthest

Time: O(n)  Space: O(1)

APPROACH 2: DP
- dp[i] = min jumps to reach index i
- For each i, update all reachable j: dp[j] = min(dp[j], dp[i] + 1)
- Correct but O(n^2) — not ideal for interviews

Time: O(n^2)  Space: O(n)
---
"""

from typing import List


# ---------- Approach 1: Greedy (BFS levels) ----------
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0

        jumps = 0
        current_end = 0   # end of current jump's reach
        farthest = 0      # farthest we can reach from positions seen so far

        for i in range(n - 1):  # don't need to jump FROM last index
            farthest = max(farthest, i + nums[i])

            if i == current_end:
                # must take a jump — extend to farthest reachable
                jumps += 1
                current_end = farthest
                if current_end >= n - 1:
                    break

        return jumps


# ---------- Approach 2: DP ----------
class SolutionDP:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [float('inf')] * n
        dp[0] = 0

        for i in range(n):
            for j in range(i + 1, min(i + nums[i] + 1, n)):
                dp[j] = min(dp[j], dp[i] + 1)

        return dp[n - 1]


# ---------- Tests ----------
if __name__ == "__main__":
    for Sol in [Solution, SolutionDP]:
        sol = Sol()

        assert sol.jump([2, 3, 1, 1, 4]) == 2
        assert sol.jump([2, 3, 0, 1, 4]) == 2
        assert sol.jump([1]) == 0
        assert sol.jump([1, 2]) == 1
        assert sol.jump([1, 1, 1, 1]) == 3
        assert sol.jump([10, 1, 1, 1, 1]) == 1

        print(f"{Sol.__name__}: all tests passed")
