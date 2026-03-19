"""
3428. Maximum and Minimum Sums of at Most Size K Subsequences
https://leetcode.com/problems/maximum-and-minimum-sums-of-at-most-size-k-subsequences/

Pattern: 19 - Linear DP (Combinatorial contribution)

---
APPROACH: Sort the array. For each element, count its contribution as min and max.
- Sort ascending. Element at index i is the minimum of all subsequences where it's the
  smallest element: choose up to k-1 elements from indices i+1..n-1.
- Similarly, element at index i is the maximum of subsequences where it's the largest:
  choose up to k-1 from indices 0..i-1.
- Contribution as min: nums[i] * sum(C(n-1-i, j) for j=0..min(k-1, n-1-i))
- Contribution as max: nums[i] * sum(C(i, j) for j=0..min(k-1, i))

Time: O(n log n + n * k)  Space: O(n)
---
"""

from typing import List
from math import comb


class Solution:
    def minMaxSums(self, nums: List[int], k: int) -> int:
        MOD = 10**9 + 7
        nums.sort()
        n = len(nums)

        # Precompute prefix sums of binomial coefficients for efficiency
        # For contribution as min: for index i, multiply by sum(C(n-1-i, j), j=0..min(k-1, n-1-i))
        # For contribution as max: for index i, multiply by sum(C(i, j), j=0..min(k-1, i))

        # Precompute factorials and inverse factorials for comb
        fact = [1] * (n + 1)
        for i in range(1, n + 1):
            fact[i] = fact[i - 1] * i % MOD
        inv_fact = [1] * (n + 1)
        inv_fact[n] = pow(fact[n], MOD - 2, MOD)
        for i in range(n - 1, -1, -1):
            inv_fact[i] = inv_fact[i + 1] * (i + 1) % MOD

        def C(n, r):
            if r < 0 or r > n:
                return 0
            return fact[n] * inv_fact[r] % MOD * inv_fact[n - r] % MOD

        ans = 0

        # We can compute running sums of C(i, 0..min(k-1,i)) as i increases
        # sum_max[i] = sum(C(i, j) for j in 0..min(k-1, i))
        # sum_max[0] = 1 (C(0,0))
        # sum_max[i] = sum_max[i-1] + C(i-1, k-1)  -- by hockey stick / Pascal relation
        # Actually: sum(C(i,j), j=0..t) = sum(C(i-1,j), j=0..t) + sum(C(i-1,j), j=0..t-1)
        # That's not simpler. Let's just compute directly with running sum.

        # Running approach: maintain running_sum = sum(C(i, j), j=0..min(k-1,i))
        # When going from i to i+1:
        # sum(C(i+1, j)) = sum(C(i,j) + C(i,j-1)) = sum(C(i,j)) + sum(C(i,j-1))
        # = running_sum + (running_sum - C(i, min(k-1,i)) ... ) hmm complicated.

        # Simpler: just iterate. O(n*k) but k could be large.
        # Actually we can use the identity: sum_{j=0}^{t} C(m, j) can be maintained.
        # Let S_i = sum_{j=0}^{min(k-1, i)} C(i, j)
        # S_0 = 1
        # S_i = 2 * S_{i-1} - C(i-1, min(k-1, i-1))  if i > k-1
        # S_i = 2 * S_{i-1} if i <= k-1  (since all 2^i terms are included)
        # Because sum_{j=0}^{t} C(i,j) = 2*sum_{j=0}^{t} C(i-1,j) - C(i-1,t)

        # Proof: C(i,j) = C(i-1,j) + C(i-1,j-1)
        # sum_{j=0}^t C(i,j) = sum C(i-1,j) + sum C(i-1,j-1) = S_{i-1,t} + S_{i-1,t} - C(i-1,t)
        # Wait: sum_{j=0}^t C(i-1,j-1) = sum_{j=0}^{t-1} C(i-1,j) = S_{i-1,t-1}
        # Hmm not quite 2*S. Let me just use direct computation.

        # For n up to 10^5 and k up to n, O(n) approach:
        # S[i] = sum_{j=0}^{min(k-1,i)} C(i, j)
        # S[0] = 1
        # If k-1 >= i: S[i] = 2^i (all terms)
        # If k-1 < i: S[i] = S[i-1]*2 - C(i-1, k-1)  [standard identity for partial sum of binomials]

        # max contribution
        s = 1  # S[0]
        for i in range(n):
            if i == 0:
                s = 1
            else:
                if k - 1 >= i:
                    s = pow(2, i, MOD)
                else:
                    s = (2 * s - C(i - 1, k - 1)) % MOD

            ans = (ans + nums[i] * s) % MOD

        # min contribution: nums[i] as min, choose from n-1-i elements to the right
        # sum(C(n-1-i, j), j=0..min(k-1, n-1-i))
        # Reuse same logic but iterate from right
        for i in range(n - 1, -1, -1):
            m = n - 1 - i  # number of elements to the right
            if m == 0:
                s = 1
            else:
                if k - 1 >= m:
                    s = pow(2, m, MOD)
                else:
                    s = (2 * s - C(m - 1, k - 1)) % MOD

            ans = (ans + nums[i] * s) % MOD

        return ans % MOD


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.minMaxSums([1, 2, 3], 2) == 24
    assert sol.minMaxSums([5, 0, 6], 1) == 22
    assert sol.minMaxSums([1, 1, 1], 2) == 12

    print("Solution: all tests passed")
