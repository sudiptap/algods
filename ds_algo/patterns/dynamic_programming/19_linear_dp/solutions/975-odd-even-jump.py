"""
975. Odd Even Jump (Hard)
https://leetcode.com/problems/odd-even-jump/

From index i, odd-numbered jumps go to the smallest value >= arr[i] among
indices j > i (if tie, smallest j). Even-numbered jumps go to the largest
value <= arr[i] among j > i (if tie, smallest j). First jump is odd.
Count starting indices from which you can reach the last index.

Pattern: Linear DP / Monotonic Stack
Approach:
- Process from right to left. For each index, determine:
  odd_next[i]: next index for odd jump (smallest val >= arr[i] to the right).
  even_next[i]: next index for even jump (largest val <= arr[i] to the right).
- Use sorted order + monotonic stack to compute these efficiently.
- dp: odd[i] = can reach end starting with an odd jump from i.
       even[i] = can reach end starting with an even jump from i.
- odd[i] = even[odd_next[i]] (after odd jump, next is even).
  even[i] = odd[even_next[i]].

Time:  O(n log n) — sorting for monotonic stack construction.
Space: O(n)
"""

from typing import List


class Solution:
    def oddEvenJumps(self, arr: List[int]) -> int:
        """Return number of good starting indices.

        Args:
            arr: Integer array, 1 <= len(arr) <= 2*10^4.

        Returns:
            Count of indices from which you can reach the last index.
        """
        n = len(arr)
        if n == 1:
            return 1

        # Find next greater or equal (odd jump): sort by value asc, index asc
        # Find next smaller or equal (even jump): sort by value desc, index asc

        def make_next(sorted_indices):
            """Given indices in some sorted order, find for each index the
            next index to its right using a monotonic stack."""
            result = [None] * n
            stack = []  # decreasing stack of indices
            for i in sorted_indices:
                while stack and stack[-1] < i:
                    result[stack.pop()] = i
                stack.append(i)
            return result

        # Odd jump: smallest value >= arr[i], smallest index if tie
        sorted_inc = sorted(range(n), key=lambda i: (arr[i], i))
        odd_next = make_next(sorted_inc)

        # Even jump: largest value <= arr[i], smallest index if tie
        sorted_dec = sorted(range(n), key=lambda i: (-arr[i], i))
        even_next = make_next(sorted_dec)

        # DP from right to left
        odd_reach = [False] * n   # can reach end starting with odd jump from i
        even_reach = [False] * n  # can reach end starting with even jump from i
        odd_reach[-1] = even_reach[-1] = True

        for i in range(n - 2, -1, -1):
            if odd_next[i] is not None:
                odd_reach[i] = even_reach[odd_next[i]]
            if even_next[i] is not None:
                even_reach[i] = odd_reach[even_next[i]]

        # First jump is odd, so count odd_reach[i] == True
        return sum(odd_reach)


# ---------- tests ----------
def test_odd_even_jumps():
    sol = Solution()

    # Example 1: [10,13,12,14,15] -> 2 (from index 3 and 4)
    assert sol.oddEvenJumps([10, 13, 12, 14, 15]) == 2

    # Example 2: [2,3,1,1,4] -> 3
    assert sol.oddEvenJumps([2, 3, 1, 1, 4]) == 3

    # Example 3: [5,1,3,4,2] -> 3
    assert sol.oddEvenJumps([5, 1, 3, 4, 2]) == 3

    # Single element
    assert sol.oddEvenJumps([1]) == 1

    # Two elements, increasing
    assert sol.oddEvenJumps([1, 2]) == 2

    # Two elements, decreasing -> odd jump from 0 needs >= 2 at index > 0 -> arr[1]=1 < 2, no. So only index 1.
    # Wait: arr=[2,1]. Odd jump from 0: need smallest val >= 2 to right. arr[1]=1 < 2. No jump. So just index 1.
    assert sol.oddEvenJumps([2, 1]) == 1

    print("All tests passed for 975. Odd Even Jump")


if __name__ == "__main__":
    test_odd_even_jumps()
