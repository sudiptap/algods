"""
3181. Maximum Total Reward Using Operations II

Pattern: Linear DP
Approach: Same bitset DP as 3180 but optimized for large inputs. Sort and deduplicate.
    Use Python's arbitrary precision integers as bitsets for O(max_val/word_size) per op.
    dp |= (dp & ((1 << v) - 1)) << v for each reward v.
Time Complexity: O(n * max_val / 64)
Space Complexity: O(max_val / 64)
"""

def maxTotalReward(rewardValues):
    rewardValues = sorted(set(rewardValues))
    dp = 1  # bit 0 = achievable total of 0

    for v in rewardValues:
        mask = (1 << v) - 1
        dp |= (dp & mask) << v

    return dp.bit_length() - 1


def test():
    assert maxTotalReward([1, 1, 3, 3]) == 4
    assert maxTotalReward([1, 6, 4, 3, 2]) == 11
    assert maxTotalReward([1, 2]) == 3
    print("All tests passed!")

test()
