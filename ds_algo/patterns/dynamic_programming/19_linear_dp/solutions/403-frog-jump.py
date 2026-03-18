"""
403. Frog Jump (Hard)

A frog crosses a river by jumping on stones. The stones are at sorted
positions given in the array `stones`. The frog starts on stones[0]
(always 0) and its first jump must be 1 unit. If the last jump was k
units, the next jump must be k-1, k, or k+1 units (k-1 >= 1).

Return True if the frog can reach the last stone.

Approach - Hash map of reachable jump sizes per stone:
    Build a dict: stone_position -> set of jump sizes that can land here.
    Initialise stones[0] with jump size 0.
    For each stone in order, for each jump size k in its set, try
    jumps of k-1, k, k+1 from current position. If the landing
    position exists in the dict, add the new jump size to that set.
    Finally check if the last stone's set is non-empty.

    Time : O(n^2) worst case (each stone can accumulate up to n jump sizes)
    Space: O(n^2)

Example:
    stones = [0,1,3,5,6,8,12,17]  -> True
    stones = [0,1,2,3,4,8,9,11]   -> False
"""

from typing import List


class Solution:
    def canCross(self, stones: List[int]) -> bool:
        """Hash-map DP: O(n^2) time and space."""
        if not stones or stones[1] != 1:
            return False

        # Map each stone position to the set of jump sizes that reached it
        reachable = {pos: set() for pos in stones}
        reachable[stones[0]].add(0)

        for pos in stones:
            for k in reachable[pos]:
                for nk in (k - 1, k, k + 1):
                    if nk > 0 and (pos + nk) in reachable:
                        reachable[pos + nk].add(nk)

        return len(reachable[stones[-1]]) > 0


# ---- Tests ----
def test():
    sol = Solution()

    assert sol.canCross([0, 1, 3, 5, 6, 8, 12, 17]) is True
    assert sol.canCross([0, 1, 2, 3, 4, 8, 9, 11]) is False
    assert sol.canCross([0, 1]) is True
    assert sol.canCross([0, 2]) is False  # first jump must be 1
    assert sol.canCross([0, 1, 3]) is True  # 0->1 (k=1), 1->3 (k=2)
    assert sol.canCross([0, 1, 3, 6, 10, 15, 21]) is True
    assert sol.canCross([0, 1, 3, 6, 7]) is False  # from 6 (k=3), can jump 2/3/4 -> 8/9/10, not 7
    # Edge: very large gap early
    assert sol.canCross([0, 1, 100]) is False

    print("All tests passed!")


if __name__ == "__main__":
    test()
