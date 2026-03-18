"""
354. Russian Doll Envelopes (Hard)

You are given a 2D array of integers envelopes where
envelopes[i] = [wi, hi] represents the width and height of an envelope.
One envelope can fit into another if and only if both the width and
height of one envelope are strictly greater than the other envelope.

Return the maximum number of envelopes you can Russian doll
(i.e., put one inside the other).

Approach:
1. Sort envelopes by width ascending. For ties in width, sort by height
   descending. This ensures that when we pick an increasing subsequence
   of heights, we never pick two envelopes with the same width.
2. Extract the heights and find the Longest Increasing Subsequence (LIS)
   using the O(n log n) patience sorting / bisect approach.

Time:  O(n log n)
Space: O(n)
"""

import bisect
from typing import List


class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        """Return the max number of envelopes that can be nested."""
        # Sort by width asc; if width equal, height desc
        envelopes.sort(key=lambda x: (x[0], -x[1]))

        # LIS on heights using O(n log n) with a tails array
        tails: List[int] = []
        for _, h in envelopes:
            pos = bisect.bisect_left(tails, h)
            if pos == len(tails):
                tails.append(h)
            else:
                tails[pos] = h
        return len(tails)


# ---------- Tests ----------

def test_basic():
    sol = Solution()
    assert sol.maxEnvelopes([[5, 4], [6, 4], [6, 7], [2, 3]]) == 3
    # [2,3] -> [5,4] -> [6,7]

def test_same_size():
    sol = Solution()
    assert sol.maxEnvelopes([[1, 1], [1, 1], [1, 1]]) == 1

def test_single():
    sol = Solution()
    assert sol.maxEnvelopes([[1, 2]]) == 1

def test_all_increasing():
    sol = Solution()
    assert sol.maxEnvelopes([[1, 1], [2, 2], [3, 3], [4, 4]]) == 4

def test_same_width_different_height():
    sol = Solution()
    # Same width means they can't nest
    assert sol.maxEnvelopes([[3, 1], [3, 2], [3, 3]]) == 1

def test_reverse_sorted():
    sol = Solution()
    assert sol.maxEnvelopes([[4, 4], [3, 3], [2, 2], [1, 1]]) == 4

def test_complex():
    sol = Solution()
    envelopes = [[2, 100], [3, 200], [4, 300], [5, 500],
                 [5, 400], [5, 250], [6, 370], [6, 360], [7, 380]]
    assert sol.maxEnvelopes(envelopes) == 5
    # e.g. [2,100]->[3,200]->[4,300]->[6,370]->[7,380]


if __name__ == "__main__":
    test_basic()
    test_same_size()
    test_single()
    test_all_increasing()
    test_same_width_different_height()
    test_reverse_sorted()
    test_complex()
    print("All tests passed!")
