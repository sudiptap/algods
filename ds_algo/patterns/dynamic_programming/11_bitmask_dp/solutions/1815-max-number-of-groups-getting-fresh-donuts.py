"""
1815. Maximum Number of Groups Getting Fresh Donuts (Hard)
https://leetcode.com/problems/maximum-number-of-groups-getting-fresh-donuts/

Given batchSize and an array groups where groups[i] is the number of
customers in the i-th group, return the maximum number of happy groups.
A group is happy if the first customer gets a fresh batch (i.e., the
total donuts served before this group is divisible by batchSize).

Pattern: Bitmask DP (on remainder distribution)
Approach:
- Only the remainder of each group size mod batchSize matters.
- Groups with remainder 0 are always happy; count them directly.
- Represent the state as a tuple of counts of each remainder (1..batchSize-1).
- dp(state, leftover) = max happy groups from remaining state given
  current leftover donuts.
- Memoize on (state, leftover). Try each remainder class that has
  count > 0, update leftover, recurse.

Time:  O(product of counts * batchSize) — bounded by distinct states
Space: O(distinct states)
"""

from typing import List
from functools import lru_cache


class Solution:
    def maxHappyGroups(self, batchSize: int, groups: List[int]) -> int:
        """Return max number of groups that get fresh donuts first.

        Args:
            batchSize: Number of donuts per batch.
            groups: List of group sizes.

        Returns:
            Maximum number of happy groups.
        """
        # Count remainders
        remainder_count = [0] * batchSize
        for g in groups:
            remainder_count[g % batchSize] += 1

        # Groups with remainder 0 are always happy
        result = remainder_count[0]
        remainder_count[0] = 0

        state = tuple(remainder_count[1:])

        @lru_cache(maxsize=None)
        def dp(state, leftover):
            best = 0
            for i in range(len(state)):
                if state[i] == 0:
                    continue
                r = i + 1  # actual remainder value
                new_state = list(state)
                new_state[i] -= 1
                new_state = tuple(new_state)
                happy = 1 if leftover == 0 else 0
                new_leftover = (leftover + r) % batchSize
                val = happy + dp(new_state, new_leftover)
                best = max(best, val)
            return best

        return result + dp(state, 0)


# ---------- tests ----------
def test_max_happy_groups():
    sol = Solution()

    # Example 1
    assert sol.maxHappyGroups(3, [1, 2, 3, 4, 5, 6]) == 4

    # Example 2
    assert sol.maxHappyGroups(4, [1, 3, 2, 5, 2, 2, 1, 6]) == 4

    # Single group divisible by batch
    assert sol.maxHappyGroups(5, [5]) == 1

    # Single group not divisible
    assert sol.maxHappyGroups(5, [3]) == 1  # first group always happy

    # All same remainder
    assert sol.maxHappyGroups(3, [1, 1, 1]) == 1

    # Two groups: [1, 2]. First group always happy. Second: leftover = 1%3=1, not fresh.
    # Or [2, 1]: first happy. leftover = 2%3=2, 1 not fresh.
    # Only 1 group is happy regardless of order.
    # Wait: [2,1]: first group (2) happy (leftover=0). leftover becomes 2.
    # Second group (1): leftover 2 != 0, not fresh.
    # [1,2]: first (1) happy. leftover=1. second (2): leftover 1!=0, not fresh.
    # So answer = 1.
    assert sol.maxHappyGroups(3, [1, 2]) == 1

    print("All tests passed for 1815. Max Number of Groups Getting Fresh Donuts")


if __name__ == "__main__":
    test_max_happy_groups()
