"""
458. Poor Pigs (Hard)
https://leetcode.com/problems/poor-pigs/

Pattern: Linear DP / Math

Given buckets of liquid, one poisonous, determine the minimum number
of pigs needed to identify the poisonous bucket within the allowed
number of test rounds.

Approach:
    Each pig can be in (T + 1) states where T = minutesToTest // minutesToDie
    (it dies in round 1, round 2, ..., round T, or survives all rounds).
    With p pigs, we can distinguish (T+1)^p outcomes.
    We need (T+1)^p >= buckets, so p = ceil(log(buckets) / log(T+1)).

Time:  O(1)
Space: O(1)
"""

import math


class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        """Return minimum number of pigs to identify the poisonous bucket."""
        if buckets <= 1:
            return 0
        tests = minutesToTest // minutesToDie
        base = tests + 1
        return math.ceil(math.log(buckets) / math.log(base))


# ───────────────────────── tests ─────────────────────────

def test_example1():
    assert Solution().poorPigs(1000, 15, 60) == 5

def test_example2():
    assert Solution().poorPigs(4, 15, 15) == 2

def test_single_bucket():
    assert Solution().poorPigs(1, 1, 1) == 0

def test_two_buckets():
    assert Solution().poorPigs(2, 15, 15) == 1

def test_exact_power():
    # base = 60/15 + 1 = 5, 5^2 = 25
    assert Solution().poorPigs(25, 15, 60) == 2

def test_just_over():
    assert Solution().poorPigs(26, 15, 60) == 3


if __name__ == "__main__":
    import pytest
    pytest.main([__file__, "-v"])
