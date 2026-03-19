"""
1031. Maximum Sum of Two Non-Overlapping Subarrays (Medium)

Pattern: 20_prefix_suffix_dp
- Prefix sums + tracking best L-length subarray before each M-length subarray and vice versa.

Approach:
- Compute prefix sums for O(1) range sum queries.
- Scan left to right. At each position i (end of an M-length window):
  - Track the maximum L-length subarray sum ending at or before the start of M-window.
  - Update answer with best_L + current_M_sum.
- Do the same swapping L and M roles.
- Return the maximum of both passes.

Complexity:
- Time:  O(n)
- Space: O(n) for prefix sums
"""

from typing import List


class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        n = len(nums)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        def range_sum(l, r):
            """Sum of nums[l..r] inclusive."""
            return prefix[r + 1] - prefix[l]

        def solve(L, M):
            # L-window comes before M-window
            best_l = 0
            ans = 0
            for i in range(L + M - 1, n):
                # M-window ends at i, starts at i - M + 1
                # L-window must end at i - M at latest, starts at i - M - L + 1
                m_start = i - M + 1
                l_end = m_start - 1
                l_start = l_end - L + 1
                if l_start >= 0:
                    best_l = max(best_l, range_sum(l_start, l_end))
                m_sum = range_sum(m_start, i)
                if best_l > 0:
                    ans = max(ans, best_l + m_sum)
            return ans

        return max(solve(firstLen, secondLen), solve(secondLen, firstLen))


# ---------- Tests ----------
def test():
    sol = Solution()

    # Example 1
    assert sol.maxSumTwoNoOverlap([0, 6, 5, 2, 2, 5, 1, 9, 4], 1, 2) == 20

    # Example 2
    assert sol.maxSumTwoNoOverlap([3, 8, 1, 3, 2, 1, 8, 9, 0], 3, 2) == 29

    # Example 3
    assert sol.maxSumTwoNoOverlap([2, 1, 5, 6, 0, 9, 5, 0, 3, 8], 4, 3) == 31

    # Minimal case
    assert sol.maxSumTwoNoOverlap([1, 2, 3], 1, 2) == 6

    print("All tests passed!")


if __name__ == "__main__":
    test()
