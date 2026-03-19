"""
3509. Maximum Product of Subsequences With Alternating Sum Equal to K
https://leetcode.com/problems/maximum-product-of-subsequences-with-alternating-sum-equal-to-k/

Pattern: 02 - 0/1 Knapsack (dp[sum][product])

---
APPROACH: DP tracking alternating sum and product.
- Alternating sum of subsequence [a1, a2, a3, ...] = a1 - a2 + a3 - ...
- dp[sum][product] = True/False whether achievable.
- Product can be large; use modular arithmetic for final answer but need exact values for DP.
- Since values are small (0-9), product is bounded by 9^n. Use set-based DP or limit product.

Actually, the problem asks for max product mod 10^9+7 where alternating sum = k.
Since elements are 0-9 and n up to ~200, product values can be huge.
Key insight: any subsequence containing 0 has product 0.
For non-zero subsequences, track log(product) or use modular arithmetic with careful handling.

But we need exact comparison for "maximum". Use the observation that products are
products of digits 1-9, which have limited unique values up to a bound.

Time: varies  Space: varies
---
"""

from typing import List


class Solution:
    def maxProduct(self, nums: List[int], k: int, limit: int) -> int:
        MOD = 10**9 + 7
        n = len(nums)

        # dp[s] = set of achievable products (capped at limit) with alternating sum s
        # and a given subsequence length parity.
        # State: (alternating_sum, product, length_parity)
        # But product can be huge... unless we cap at limit.
        # The problem says products must be <= limit to be valid.
        # So we only track products <= limit.

        # dp[(alt_sum, parity)] = set of products <= limit achievable
        # parity: 0 = even length (next element added), 1 = odd length (next element subtracted)

        # Actually: alternating sum for subseq of length L:
        # a1 - a2 + a3 - a4 + ... = sum with alternating signs starting with +
        # When we add an element at position len+1:
        #   if new length is odd: alt_sum += element
        #   if new length is even: alt_sum -= element

        # dp: dict mapping (alt_sum, parity) -> set of products
        # parity 0 = next add will be +, parity 1 = next add will be -

        # Initial: empty subsequence (not valid for answer)
        # dp = {(0, 0): {1}}  -- empty subseq: alt_sum=0, parity=0 (next is +), product=1 (empty)

        # Use dict of sets. For efficiency, products are bounded by limit.

        # dp[(alt_sum, length_parity)] -> set of products
        from collections import defaultdict

        dp = defaultdict(set)
        dp[(0, 0)].add(1)  # empty subsequence placeholder (product = 1 for multiplicative identity)

        has_answer = False

        for num in nums:
            new_dp = defaultdict(set)
            # Copy existing states (don't take this element)
            for key, prods in dp.items():
                new_dp[key] |= prods

            # Take this element
            for (s, par), prods in dp.items():
                if par == 0:
                    # Next element gets +, so new_s = s + num, new parity = 1
                    new_s = s + num
                    new_par = 1
                else:
                    # Next element gets -, so new_s = s - num, new parity = 0
                    new_s = s - num
                    new_par = 0

                for p in prods:
                    new_p = p * num
                    if new_p <= limit:
                        new_dp[(new_s, new_par)].add(new_p)

            dp = new_dp

        # Find max product with alt_sum = k (any parity, since parity just indicates next action)
        # But we need actual subsequences, not empty. Parity 1 means odd length, parity 0 means even length (>=2).
        ans = -1
        for par in [0, 1]:
            if (k, par) in dp:
                for p in dp[(k, par)]:
                    # Skip the empty subsequence marker
                    if par == 0 and p == 1:
                        # This could be the empty subsequence or a real product of 1
                        # We need to distinguish. Let's handle differently.
                        pass
                    ans = max(ans, p)

        # Handle the empty subseq issue: the (0, 0, product=1) is the empty subseq.
        # If k=0, product=1 from empty subseq shouldn't count.
        # Fix: track whether the subsequence is non-empty.

        # Redo with a flag
        dp2 = defaultdict(set)
        dp2[(0, 0, False)].add(1)  # (alt_sum, parity, started) -> products

        for num in nums:
            new_dp2 = defaultdict(set)
            for key, prods in dp2.items():
                new_dp2[key] |= prods

            for (s, par, started), prods in dp2.items():
                if par == 0:
                    new_s = s + num
                    new_par = 1
                else:
                    new_s = s - num
                    new_par = 0

                for p in prods:
                    if not started:
                        new_p = num  # first element, product = num itself
                    else:
                        new_p = p * num
                    if new_p <= limit:
                        new_dp2[(new_s, new_par, True)].add(new_p)

            dp2 = new_dp2

        ans = -1
        for par in [0, 1]:
            key = (k, par, True)
            if key in dp2:
                for p in dp2[key]:
                    ans = max(ans, p)

        return ans % MOD if ans >= 0 else -1


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.maxProduct([1, 2, 3], 2, 10) == 6
    assert sol.maxProduct([0, 2, 3], -5, 12) == -1
    assert sol.maxProduct([2, 2, 3, 3], 0, 9) == 9

    print("Solution: all tests passed")
