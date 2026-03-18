"""
473. Matchsticks to Square (Medium)

Pattern: 11_bitmask_dp
- Backtracking with pruning to partition matchsticks into 4 groups of equal sum.

Approach:
- Compute total sum; if not divisible by 4, return False immediately.
- Target side length = total // 4. If any single matchstick exceeds this, return False.
- Sort matchsticks in descending order for early pruning (larger sticks fail faster).
- Use backtracking: try to place each matchstick into one of the 4 sides.
  Pruning rules:
    1. Skip a side if adding the current matchstick would exceed the target.
    2. Skip duplicate sides (if sides[j] == sides[j-1] and we failed with j-1, skip j).
    3. If a side is 0, only try the first empty side (all empty sides are equivalent).

Complexity:
- Time:  O(4^n) worst case, but pruning makes it much faster in practice
- Space: O(n) recursion depth
"""

from typing import List


class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total = sum(matchsticks)
        if total == 0 or total % 4 != 0:
            return False

        target = total // 4
        if max(matchsticks) > target:
            return False

        matchsticks.sort(reverse=True)
        sides = [0] * 4

        def backtrack(idx: int) -> bool:
            if idx == len(matchsticks):
                return sides[0] == sides[1] == sides[2] == target

            seen = set()
            for j in range(4):
                if sides[j] + matchsticks[idx] > target:
                    continue
                if sides[j] in seen:
                    continue
                seen.add(sides[j])

                sides[j] += matchsticks[idx]
                if backtrack(idx + 1):
                    return True
                sides[j] -= matchsticks[idx]

            return False

        return backtrack(0)


# ---------- Tests ----------
def test():
    sol = Solution()

    # Example 1: [1,1,2,2,2] -> side=2, possible
    assert sol.makesquare([1, 1, 2, 2, 2]) is True

    # Example 2: [3,3,3,3,4] -> sum=16, side=4, but 3+3=6>4 can't fit
    assert sol.makesquare([3, 3, 3, 3, 4]) is False

    # All equal
    assert sol.makesquare([5, 5, 5, 5]) is True

    # Sum not divisible by 4
    assert sol.makesquare([1, 2, 3]) is False

    # Single matchstick too large
    assert sol.makesquare([10, 1, 1, 1, 1]) is False

    # Larger valid case
    assert sol.makesquare([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) is True  # side=3

    # Edge: empty
    assert sol.makesquare([]) is False

    print("All tests passed!")


if __name__ == "__main__":
    test()
