"""
3180. Maximum Total Reward Using Operations I

Pattern: Linear DP
Approach: Sort rewardValues. Use bitset DP: dp is a bitmask where bit i is set
    if total reward i is achievable. For each reward v, if current total < v,
    we can add v. This means bits 0..v-1 can transition to bits v..2v-1.
    dp |= (dp & ((1 << v) - 1)) << v.
Time Complexity: O(n * max_val)
Space Complexity: O(max_val)
"""

def maxTotalReward(rewardValues):
    rewardValues = sorted(set(rewardValues))
    # dp as bitset: bit i set means total i is achievable
    dp = 1  # bit 0 set: total 0 is achievable

    for v in rewardValues:
        # Extract bits 0..v-1 (totals less than v)
        mask = (1 << v) - 1
        valid = dp & mask
        dp |= valid << v

    return dp.bit_length() - 1


def test():
    assert maxTotalReward([1, 1, 3, 3]) == 4
    assert maxTotalReward([1, 6, 4, 3, 2]) == 11
    assert maxTotalReward([1, 2]) == 3
    print("All tests passed!")

test()
