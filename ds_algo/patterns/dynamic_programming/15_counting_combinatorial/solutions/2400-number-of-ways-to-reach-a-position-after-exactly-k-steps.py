"""
2400. Number of Ways to Reach a Position After Exactly k Steps
https://leetcode.com/problems/number-of-ways-to-reach-a-position-after-exactly-k-steps/

Pattern: 15 - Counting/Combinatorial

---
APPROACH: C(k, (k + endPos - startPos) / 2)
- Need to reach endPos from startPos in exactly k steps (+1 or -1).
- Let r = number of right steps, l = number of left steps.
- r + l = k, r - l = endPos - startPos = d
- r = (k + d) / 2. Must be integer and 0 <= r <= k.
- Answer: C(k, r) mod 10^9+7

Time: O(k) for computing combination  Space: O(1)
---
"""

from math import comb


class Solution:
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        MOD = 10**9 + 7
        d = abs(endPos - startPos)

        if (k + d) % 2 != 0 or d > k:
            return 0

        r = (k + d) // 2
        return comb(k, r) % MOD


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.numberOfWays(1, 2, 3) == 3
    assert sol.numberOfWays(2, 5, 10) == 0
    assert sol.numberOfWays(0, 0, 2) == 1
    assert sol.numberOfWays(0, 0, 0) == 1

    print("all tests passed")
