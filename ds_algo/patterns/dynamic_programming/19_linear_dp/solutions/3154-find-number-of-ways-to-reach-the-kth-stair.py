"""
3154. Find Number of Ways to Reach the K-th Stair

Pattern: Linear DP
Approach: Memoized DFS. From stair i with jump power j, you can:
    1) Go down to i-1 (if not done consecutively and i > 0)
    2) Jump up to i + 2^j (then j becomes j+1)
    Count ways to reach stair k. State = (current_stair, jump_power, last_was_down).
Time Complexity: O(k * log(k)) states
Space Complexity: O(k * log(k))
"""
from functools import lru_cache

def waysToReachStair(k):
    @lru_cache(maxsize=None)
    def dfs(i, j, last_down):
        if i > k + 1:  # Can't come back (only go down by 1)
            return 0
        count = 1 if i == k else 0

        # Option 1: go up by 2^j
        count += dfs(i + (1 << j), j + 1, False)

        # Option 2: go down by 1 (if not last move and i > 0)
        if not last_down and i > 0:
            count += dfs(i - 1, j, True)

        return count

    return dfs(1, 0, False)


def test():
    assert waysToReachStair(0) == 2
    assert waysToReachStair(1) == 4
    r = waysToReachStair(2)
    assert r > 0, f"Got {r}"
    print("All tests passed!")

test()
