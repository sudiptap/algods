"""
3533. Concatenated Divisibility
https://leetcode.com/problems/concatenated-divisibility/

Pattern: 11 - Bitmask DP (dp[mask][remainder])

---
APPROACH: dp[mask][rem] = True if we can form a concatenation of the elements indicated
by mask such that the number formed so far has remainder rem when divided by k.
- When adding number nums[i] with d digits to current number N:
  new_number = N * 10^d + nums[i], so new_rem = (rem * 10^d + nums[i]) % k.
- Track which permutation gives the result for reconstruction.

Time: O(2^n * n * k)  Space: O(2^n * k)
---
"""

from typing import List


class Solution:
    def concatenatedDivisibility(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        # Precompute number of digits for each number
        num_digits = [len(str(x)) for x in nums]
        # Precompute 10^d mod k
        pow10 = [1] * 11
        for d in range(1, 11):
            pow10[d] = pow10[d - 1] * 10 % k

        full = (1 << n) - 1

        # dp[mask][rem] = index of last added element (for reconstruction), or -1 if not reachable
        # Use BFS/DP forward
        dp = [[False] * k for _ in range(1 << n)]
        parent = [[(-1, -1)] * k for _ in range(1 << n)]  # (prev_mask, prev_rem)
        last_elem = [[-1] * k for _ in range(1 << n)]

        dp[0][0] = True

        for mask in range(1 << n):
            for rem in range(k):
                if not dp[mask][rem]:
                    continue
                # Try adding each unused element (in order for lex smallest)
                for i in range(n):
                    if mask & (1 << i):
                        continue
                    new_mask = mask | (1 << i)
                    new_rem = (rem * pow10[num_digits[i]] + nums[i]) % k
                    if not dp[new_mask][new_rem]:
                        dp[new_mask][new_rem] = True
                        parent[new_mask][new_rem] = (mask, rem)
                        last_elem[new_mask][new_rem] = i

        if not dp[full][0]:
            return []

        # Reconstruct: backtrack from (full, 0)
        result = []
        mask, rem = full, 0
        while mask != 0:
            i = last_elem[mask][rem]
            result.append(nums[i])
            prev_mask, prev_rem = parent[mask][rem]
            mask, rem = prev_mask, prev_rem

        result.reverse()
        return result


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    r1 = sol.concatenatedDivisibility([1, 2, 3], 3)
    # Any permutation of [1,2,3] concatenated should be div by 3 since 1+2+3=6
    assert len(r1) == 3
    assert int(''.join(map(str, r1))) % 3 == 0

    r2 = sol.concatenatedDivisibility([1, 2], 7)
    # 12 % 7 = 5, 21 % 7 = 0
    assert r2 == [2, 1]

    print("Solution: all tests passed")
