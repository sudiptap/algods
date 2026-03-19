"""
3351. Sum of Good Subsequences (Hard)

Pattern: 19_linear_dp
- A "good" subsequence has consecutive elements differing by exactly 1.
  Find sum of all elements across all good subsequences.

Approach:
- For each value v, track:
  - count[v] = number of good subsequences ending with value v
  - total[v] = sum of all elements in those subsequences
- When processing element v:
  - It can extend subsequences ending at v-1 or v+1, or start new ones.
  Wait, subsequences must have consecutive elements differ by 1 (either +1 or -1).
  Actually re-reading: "consecutive" means adjacent in subsequence differ by exactly 1.
  So subsequences like [1,2,3] or [3,2,1] or [1,2,1] are all good.
  But simpler: each new element v can extend any subsequence ending at v-1 or v+1.

- count[v] += count[v-1] + count[v+1] + 1
- total[v] += total[v-1] + total[v+1] + v * (count[v-1] + count[v+1] + 1)

Wait, the problem says consecutive elements differ by exactly 1 (absolute value).
Let me reconsider: this means |a[i] - a[i+1]| = 1 for consecutive elements in subsequence.

Complexity:
- Time:  O(n)
- Space: O(max_val)
"""

from typing import List
from collections import defaultdict

MOD = 10**9 + 7


class Solution:
    def sumOfGoodSubsequences(self, nums: List[int]) -> int:
        count = defaultdict(int)  # count[v] = # subsequences ending at v
        total = defaultdict(int)  # total[v] = sum of elements in those subsequences

        ans = 0
        for v in nums:
            c = (count[v - 1] + count[v + 1] + 1) % MOD
            s = (total[v - 1] + total[v + 1] + v * c) % MOD
            count[v] = (count[v] + c) % MOD
            total[v] = (total[v] + s) % MOD
            ans = (ans + s) % MOD

        return ans


# ---------- Tests ----------
def test():
    sol = Solution()

    # Example 1: [1,2,1] -> good subsequences and their sums
    assert sol.sumOfGoodSubsequences([1, 2, 1]) == 14

    # Example 2
    assert sol.sumOfGoodSubsequences([3, 4, 5]) == 40

    print("All tests passed!")


if __name__ == "__main__":
    test()
