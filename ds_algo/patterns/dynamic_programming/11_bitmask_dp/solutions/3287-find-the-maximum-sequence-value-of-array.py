"""
3287. Find the Maximum Sequence Value of Array (Hard)

Pattern: 11_bitmask_dp
- Pick a subsequence of size 2*k, split into first-k and last-k. Sequence value =
  (OR of first k) XOR (OR of last k). Maximize this.

Approach:
- left[i][j] = set of OR values achievable by choosing j elements from nums[0..i].
- right[i][j] = set of OR values achievable by choosing j elements from nums[i..n-1].
- For each split point, combine left OR values (k elements) with right OR values
  (k elements) and maximize XOR.
- Since OR values are bounded by 2^7 = 128 (values up to 127), use bitsets.

Complexity:
- Time:  O(n * k * 128)
- Space: O(n * k * 128)
"""

from typing import List


class Solution:
    def maxValue(self, nums: List[int], k: int) -> int:
        n = len(nums)

        # left_reach[i] = set of OR values using exactly k elements from nums[0..i]
        # Build incrementally: dp[j] = set of reachable OR values using j elements
        # left_at[i] = reachable OR values using exactly k elements ending at or before i

        # left[i] stores sets for each count j=0..k
        # We want: for each i, the set of OR values achievable with exactly k elements from nums[0..i]
        left_sets = [set() for _ in range(n)]  # left_sets[i] = reachable k-element OR values from [0..i]
        dp = [set() for _ in range(k + 1)]
        dp[0].add(0)
        for i in range(n):
            # Process in reverse to avoid using same element twice
            for j in range(min(i + 1, k), 0, -1):
                for v in dp[j - 1]:
                    dp[j].add(v | nums[i])
            left_sets[i] = set(dp[k])

        right_sets = [set() for _ in range(n)]
        dp2 = [set() for _ in range(k + 1)]
        dp2[0].add(0)
        for i in range(n - 1, -1, -1):
            for j in range(min(n - i, k), 0, -1):
                for v in dp2[j - 1]:
                    dp2[j].add(v | nums[i])
            right_sets[i] = set(dp2[k])

        ans = 0
        # Split: first k from [0..i], last k from [i+1..n-1]
        # Need i >= k-1 and n-1-(i+1)+1 >= k => i <= n-1-k
        for i in range(k - 1, n - k):
            for lv in left_sets[i]:
                for rv in right_sets[i + 1]:
                    ans = max(ans, lv ^ rv)

        return ans


# ---------- Tests ----------
def test():
    sol = Solution()

    # Example 1
    assert sol.maxValue([2, 6, 7], 1) == 5

    # Example 2
    assert sol.maxValue([4, 2, 5, 6, 7], 2) == 2

    # Minimal
    assert sol.maxValue([1, 2], 1) == 3

    print("All tests passed!")


if __name__ == "__main__":
    test()
