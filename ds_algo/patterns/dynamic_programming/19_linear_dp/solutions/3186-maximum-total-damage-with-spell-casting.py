"""
3186. Maximum Total Damage With Spell Casting

Pattern: Linear DP (House Robber variant)
Approach: Group spells by power value. Sort unique values. For each unique value,
    you can't use values within +/-2. This is like house robber but with gaps.
    Use DP with pointer to last valid group (binary search).
Time Complexity: O(n log n)
Space Complexity: O(n)
"""
from collections import Counter
from bisect import bisect_left

def maximumTotalDamage(power):
    freq = Counter(power)
    vals = sorted(freq.keys())
    n = len(vals)

    # dp[i] = max damage using values from vals[0..i]
    dp = [0] * (n + 1)

    for i in range(n):
        val = vals[i]
        total = val * freq[val]

        # Find last index j where vals[j] < val - 2
        j = bisect_left(vals, val - 2) - 1
        take = total + (dp[j + 1] if j >= 0 else 0)
        dp[i + 1] = max(dp[i], take)

    return dp[n]


def test():
    assert maximumTotalDamage([1, 1, 3, 4]) == 6
    assert maximumTotalDamage([7, 1, 6, 6]) == 13
    assert maximumTotalDamage([5, 5, 5]) == 15
    print("All tests passed!")

test()
