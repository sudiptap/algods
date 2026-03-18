"""
1911. Maximum Alternating Subsequence Sum
https://leetcode.com/problems/maximum-alternating-subsequence-sum/

Pattern: 19 - Linear DP (Two-state greedy DP)

---
APPROACH: Track two states while scanning left to right.
- odd:  best alternating sum if the *next* element we pick is at an ODD
        position (1-indexed) in the subsequence → it gets ADDED.
- even: best alternating sum if the *next* element we pick is at an EVEN
        position → it gets SUBTRACTED.

Transitions for each element x:
  new_odd  = max(odd, even + x)   # skip x, or pick x at an odd position
  new_even = max(even, odd - x)   # skip x, or pick x at an even position

The subsequence must have at least one element, so the answer is
max(odd, even) at the end, but since we always want to end on a "just added"
state for max sum, the answer is `even` (meaning we just finished placing
an odd-position element and are waiting for the next even-position one,
i.e., last action was addition).

Actually simpler: odd starts at 0, even at -inf. Answer = max(odd, even).

Time:  O(n)
Space: O(1)
---
"""

from typing import List


class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        """Return the maximum alternating sum of any subsequence of nums."""
        odd = 0          # max sum when next pick is added (odd position)
        even = 0         # max sum when next pick is subtracted (even position)

        for x in nums:
            # If we pick x at an odd position: we add x to whatever
            # state had the last pick at an even position (or fresh start).
            new_odd = max(odd, even + x)
            new_even = max(even, odd - x)
            odd, even = new_odd, new_even

        return odd  # best is ending with an addition (odd-position pick)


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.maxAlternatingSum([4, 2, 5, 3]) == 7       # 4 - 2 + 5 = 7
    assert sol.maxAlternatingSum([5, 6, 7, 8]) == 8       # just pick 8
    assert sol.maxAlternatingSum([6, 2, 1, 2, 4, 5]) == 10  # 6 - 1 + 5 = 10
    assert sol.maxAlternatingSum([1]) == 1
    assert sol.maxAlternatingSum([100]) == 100

    print("all tests passed")
