"""
276. Paint Fence (Medium)

Pattern: 01_fibonacci_pattern
    Fibonacci-style recurrence: each state depends on the previous two states.

Approach:
    For each post, count ways where it's the SAME color as previous vs
    DIFFERENT color.
    - same  = diff_prev * 1       (must differ from the one before previous)
    - diff  = total_prev * (k-1)  (any of k-1 other colors)
    - total = same + diff
    Base: post 1 has k ways (all different, 0 same).

Complexity:
    Time:  O(n) - single pass through posts.
    Space: O(1) - only track same and diff.
"""


class Solution:
    def numWays(self, n: int, k: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return k

        # Post 1: same=0, diff=k
        same, diff = 0, k

        for _ in range(2, n + 1):
            new_same = diff  # same color as prev => prev must have been diff
            new_diff = (same + diff) * (k - 1)
            same, diff = new_same, new_diff

        return same + diff


# ---------- Tests ----------
def test():
    sol = Solution()

    # n=1, k=1 => 1
    assert sol.numWays(1, 1) == 1

    # n=3, k=2 => 6
    assert sol.numWays(3, 2) == 6

    # n=2, k=2 => 4 (all combos: 2*2)
    assert sol.numWays(2, 2) == 4

    # n=0 => 0
    assert sol.numWays(0, 5) == 0

    # n=1, k=5 => 5
    assert sol.numWays(1, 5) == 5

    # n=2, k=1 => 1 (same color twice is allowed for 2 consecutive)
    assert sol.numWays(2, 1) == 1

    # n=3, k=1 => 0 (can't have 3 consecutive same)
    assert sol.numWays(3, 1) == 0

    # n=7, k=2 => 42
    assert sol.numWays(7, 2) == 42

    print("All tests passed!")


if __name__ == "__main__":
    test()
