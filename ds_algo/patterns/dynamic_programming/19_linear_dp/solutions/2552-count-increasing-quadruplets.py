"""
2552. Count Increasing Quadruplets
https://leetcode.com/problems/count-increasing-quadruplets/

Pattern: 19 - Linear DP

---
APPROACH: For each (j, k) pair with nums[j] > nums[k], accumulate contributions
- Key insight: iterate k, maintain dp[j] = number of valid i < j with nums[i] < nums[k].
  As k moves right, when we encounter nums[k]:
  - For each j < k where nums[j] > nums[k], add dp[j] * (count of l > k with nums[l] > nums[j]).

  Simpler O(n^2) approach using prefix counting:
  - For each k (3rd element), track dp[k] = sum over j<k where nums[j]>nums[k] of
    (count of i<j with nums[i]<nums[k]).
  - Then for l (4th element), add dp[k] for each k < l with nums[k] < nums[l].

  Cleaner: sweep from left to right. For each new element at position k:
  - dp[j] accumulates count of i < j with nums[i] < nums[k] as k increases.
  - When nums[j] > nums[k], add to answer: dp[j] (already has count of valid i's).

  Actually the standard trick:
  - cnt[j] = as we process positions as k: the cumulative count of valid (i,j) pairs.
  - For position k: for each j < k, if nums[j] > nums[k], ans contributes...

  Let's use the editorial approach:
  - dp[j] = number of 132 patterns (i,j,k) found so far where j is the middle element.
  - Iterate k from left to right:
    - For each j < k with nums[j] > nums[k]: dp[j] += (count of i<j: nums[i]<nums[k])
    - For the 4th element: as l, for each k<l with nums[k]<nums[l]: ans += dp[k]

  But we need to separate the two usages. Let me use:
  - Iterate index as the 4th element (l). Maintain dp[k] = count of (i,j,k) triples.
  - When processing l: ans += sum of dp[k] for k<l with nums[k]<nums[l].
  - After processing l as 4th element, update dp values by considering l as potential k:
    for j < l, if nums[j] > nums[l], dp[l] += (count i<j: nums[i]<nums[l]).

  This still seems O(n^2) per step. Let me just track things incrementally.

Actual O(n^2) approach:
- dp[j] = number of (i, j, k) 132-like triples (nums[i]<nums[k]<nums[j], i<j<k).
- Iterate k from 0 to n-1:
  - less_count = 0 (count of i < k with nums[i] < nums[k])
  - For j from 0 to k-1:
    - if nums[j] < nums[k]: less_count += 1
    - if nums[j] > nums[k]: dp[j] += less_count (new valid i's for this j,k pair...
      but less_count includes j itself!)
  Actually: we need i < j, so iterate j up to k-1 and track less_count of elements
  strictly before j that are less than nums[k]. We need to be careful.

  Fix: iterate j from 0 to k-1. Before checking j, less_count = #{i<j: nums[i]<nums[k]}.
  - if nums[j] > nums[k]: dp[j] += less_count
  - if nums[j] < nums[k]: less_count += 1 (j could be i for future j's)

Then for the 4th element l:
  - ans = sum over k < l where nums[k] < nums[l] of dp[k].
  - As we iterate l, maintain running sum.

Wait, we iterate k as the outer loop and inside update dp[j]. Then we need another
pass for l. Let me combine:

Iterate l from 0 to n-1, treating l as both potential k (for building dp) and
potential 4th element.

For each l:
  1. As 4th element: ans += sum of dp[k] for k<l with nums[k]<nums[l]
     -> maintain this with a running sum as we go
  2. As 3rd element (k=l): update dp[j] for j<l where nums[j]>nums[l]
     -> iterate j from 0..l-1, tracking less_count

This is O(n^2) total.

Time: O(n^2)  Space: O(n)
---
"""

from typing import List


class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n  # dp[j] = count of (i,j,k) triples
        ans = 0

        for k in range(n):
            # Step 1: as 4th element (l=k), collect answer
            # ans += dp[j] for j<k where... wait dp[j] already counts (i,j,prev_k)
            # and we need nums[k] > nums[j]? No.
            # dp[j] = count of valid (i,j,k') triples with k'<k.
            # For 4th element l=k: need nums[l] > nums[j]? No, need nums[l] > nums[j]?
            # The pattern is i<j<k<l, nums[i]<nums[k]<nums[j] (wait no...)
            #
            # Pattern: i<j<k<l, nums[i]<nums[j]<...? No:
            # Count quadruplets where nums[i]<nums[k]<nums[j]<nums[l]? No...
            #
            # Re-read problem: "i<j<k<l and nums[i]<nums[k]<nums[j]<nums[l]"? No.
            # The problem says 42-pattern: nums[i]<nums[k]<nums[j] where i<j<k...
            # Actually the problem: count (i,j,k,l) with i<j<k<l and
            # nums[i]<nums[k]<nums[j]<nums[l]? Let me re-check.
            #
            # Problem 2552: "i<j<k<l such that nums[i]<nums[k]<nums[j]<nums[l]"? No.
            # Actually: i<j<k<l, nums[i] < nums[j] < nums[k] < nums[l]... that's
            # just increasing quadruplets? That seems too simple.
            #
            # Oh wait, let me re-read: "Count Increasing Quadruplets"
            # 2552: Given 0-indexed array, count quadruplets (i,j,k,l) where
            # i<j<k<l and nums[i]<nums[k]<nums[j]<nums[l].
            # Pattern: a < c < b < d where a is at i, b at j, c at k, d at l.
            # So: nums[i] < nums[k] < nums[j] < nums[l]. 1-3-2-4 pattern.
            pass

        # Clean implementation for 1324 pattern:
        # nums[i] < nums[k] < nums[j] < nums[l] where i<j<k<l
        # Equivalently: find i<j<k<l with nums[i]<nums[k] and nums[k]<nums[j] (so j>k
        # impossible since j<k)... wait i<j<k<l but nums[j]>nums[k]. So it IS the
        # 1-3-2-4 pattern looking at values: val_i < val_k < val_j < val_l
        # with positions i<j<k<l.

        # dp[j] = for each j, count of (i, j, k) triples where i<j<k,
        #         nums[i]<nums[k]<nums[j] (i.e., k has a smaller value than j but
        #         bigger than some i before j)
        # Wait this means: for the triple (i,j,k) in positions with i<j<k:
        #   nums[i] < nums[k] < nums[j]
        # Then l>k with nums[l]>nums[j] completes it.

        dp = [0] * n
        ans = 0

        for k in range(n):
            # Use k as potential 4th element (l):
            # For each j < k (acting as j in the quad) where nums[j] < nums[k]:
            #   ... no, nums[l] > nums[j], so we need nums[k] > nums[j_in_triple].
            # But j in the triple has nums[j] > nums[k_in_triple].
            # Let me reindex: in the quadruplet (a,b,c,d)=positions:
            #   nums[a]<nums[c]<nums[b]<nums[d]
            # dp[b] = count of (a,b,c) triples for fixed b.
            # When we add d: need nums[d] > nums[b], so for each b<d with nums[b]<nums[d]:
            #   ans += dp[b]

            # As 4th element d=k:
            for b in range(k):
                if nums[b] < nums[k]:
                    ans += dp[b]

            # Now update dp by considering k as potential c (3rd position):
            # For triple (a,b,c) with c=k: need b<k, nums[b]>nums[k],
            # and a<b, nums[a]<nums[k].
            less_before = 0
            for b in range(k):
                if nums[b] > nums[k]:
                    dp[b] += less_before
                if nums[b] < nums[k]:
                    less_before += 1

        return ans


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.countQuadruplets([1, 3, 2, 4, 5]) == 2
    assert sol.countQuadruplets([1, 2, 3, 4]) == 0
    assert sol.countQuadruplets([4, 3, 2, 1]) == 0

    print("all tests passed")
