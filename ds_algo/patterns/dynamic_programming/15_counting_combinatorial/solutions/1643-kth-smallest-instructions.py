"""
1643. Kth Smallest Instructions
https://leetcode.com/problems/kth-smallest-instructions/

Pattern: 15 - Counting / Combinatorial DP

---
APPROACH: Combinatorial counting to greedily build result
- Need to reach destination[0] rows down, destination[1] cols right.
- Total moves = r + c, with r 'V' and c 'H'. String must be k-th lex smallest.
- At each position, decide H or V:
  - If we place 'H', there are C(remaining_moves - 1, remaining_V) strings.
  - If this count >= k, place 'H'. Otherwise subtract count and place 'V'.

Time: O((r + c)^2) or O(r + c) with precomputed combinations
Space: O(r + c)
---
"""

from typing import List
from math import comb


class Solution:
    def kthSmallestPath(self, destination: List[int], k: int) -> str:
        r, c = destination  # rows down, cols right
        total = r + c
        result = []
        v_remaining = r
        h_remaining = c

        for i in range(total):
            if v_remaining == 0:
                result.append('H')
                h_remaining -= 1
            elif h_remaining == 0:
                result.append('V')
                v_remaining -= 1
            else:
                # Remaining positions after this one
                remaining = total - 1 - i
                # Count of strings starting with 'H'
                count = comb(remaining, v_remaining)
                if k <= count:
                    result.append('H')
                    h_remaining -= 1
                else:
                    result.append('V')
                    k -= count
                    v_remaining -= 1

        return ''.join(result)


# --- Tests ---
def test():
    sol = Solution()

    assert sol.kthSmallestPath([2, 3], 1) == "HHHVV"
    assert sol.kthSmallestPath([2, 3], 2) == "HHVHV"
    assert sol.kthSmallestPath([2, 3], 3) == "HHVVH"
    assert sol.kthSmallestPath([2, 3], 9) == "VHVHH"
    assert sol.kthSmallestPath([2, 3], 10) == "VVHHH"

    # Simple cases
    assert sol.kthSmallestPath([1, 1], 1) == "HV"
    assert sol.kthSmallestPath([1, 1], 2) == "VH"

    print("All tests passed!")


if __name__ == "__main__":
    test()
