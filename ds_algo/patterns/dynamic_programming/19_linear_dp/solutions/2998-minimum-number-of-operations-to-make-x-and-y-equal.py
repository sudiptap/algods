"""
2998. Minimum Number of Operations to Make X and Y Equal

Pattern: Linear DP
Approach: BFS from x to y. At each state, try: +1, -1, divide by 11 (if divisible),
    divide by 5 (if divisible). If x <= y, answer is y - x. Otherwise BFS explores
    states efficiently. We also consider adjusting to nearest multiple of 5 or 11.
Time Complexity: O(x) worst case
Space Complexity: O(x)
"""
from functools import lru_cache

def minimumOperationsToMakeEqual(x, y):
    if x <= y:
        return y - x

    @lru_cache(maxsize=None)
    def solve(val):
        if val <= y:
            return y - val
        res = val - y  # just decrement
        # Try dividing by 11: go to nearest multiple >= val or <= val
        r = val % 11
        res = min(res, r + 1 + solve(val // 11))           # round down
        res = min(res, (11 - r) + 1 + solve(val // 11 + 1)) # round up
        # Try dividing by 5
        r = val % 5
        res = min(res, r + 1 + solve(val // 5))
        res = min(res, (5 - r) + 1 + solve(val // 5 + 1))
        return res

    return solve(x)


def test():
    assert minimumOperationsToMakeEqual(26, 1) == 3
    assert minimumOperationsToMakeEqual(54, 2) == 4
    assert minimumOperationsToMakeEqual(25, 30) == 5
    assert minimumOperationsToMakeEqual(1, 1) == 0
    # 4 -> 3 -> 2 -> 1 = 3 ops, or 4 -> 5 -> /5 = 1 -> 2 ops? 5/5=1, that's +1, /5 = 2 ops
    # Actually: 4 -1 -> 3 -1 -> 2 -1 -> 1 = 3 ops. But 4+1=5, 5/5=1 = 2 ops!
    assert minimumOperationsToMakeEqual(4, 1) == 2
    print("All tests passed!")

test()
