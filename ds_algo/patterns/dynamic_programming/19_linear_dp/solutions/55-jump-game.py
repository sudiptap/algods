"""
55. Jump Game
https://leetcode.com/problems/jump-game/

Pattern: 19 - Linear DP (greedy — simpler sibling of #45 Jump Game II)

---
APPROACH: Greedy (track farthest reachable)
- Maintain `farthest` = max index we can reach so far
- Scan left to right: if i > farthest, we're stuck → return False
- Update farthest = max(farthest, i + nums[i])
- If farthest >= n-1, return True

Time: O(n)  Space: O(1)

Why greedy works: if we can reach index i, we can reach everything
in [0, i+nums[i]]. No need for DP table — just track the frontier.
---
"""

from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farthest = 0

        for i in range(len(nums)):
            if i > farthest:
                return False
            farthest = max(farthest, i + nums[i])

        return True


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.canJump([2, 3, 1, 1, 4]) == True
    assert sol.canJump([3, 2, 1, 0, 4]) == False
    assert sol.canJump([0]) == True
    assert sol.canJump([1, 0]) == True
    assert sol.canJump([0, 1]) == False
    assert sol.canJump([2, 0, 0]) == True

    print("all tests passed")
