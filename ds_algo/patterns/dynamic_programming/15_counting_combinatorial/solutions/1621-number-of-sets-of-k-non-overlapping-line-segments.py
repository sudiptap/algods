"""
1621. Number of Sets of K Non-Overlapping Line Segments
https://leetcode.com/problems/number-of-sets-of-k-non-overlapping-line-segments/

Pattern: 15 - Counting / Combinatorial DP

---
APPROACH: Combinatorics (Stars and Bars)
- Equivalent to choosing 2k points from n+k-1 points (with transformation).
- Formula: C(n + k - 1, 2 * k)
- Intuition: segments can share endpoints. By adding k-1 extra "gap" points,
  we transform into choosing 2k distinct points from n+k-1 points.

Time: O(k) for computing the combination
Space: O(1)
---
"""

MOD = 10**9 + 7


class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        # C(n + k - 1, 2k) mod p
        # Use modular inverse for combination
        top = n + k - 1
        bot = 2 * k
        # Compute C(top, bot) mod MOD
        if bot > top:
            return 0
        num = 1
        den = 1
        for i in range(bot):
            num = num * (top - i) % MOD
            den = den * (i + 1) % MOD
        return num * pow(den, MOD - 2, MOD) % MOD


# --- Tests ---
def test():
    sol = Solution()

    assert sol.numberOfSets(4, 2) == 5
    assert sol.numberOfSets(3, 1) == 3
    assert sol.numberOfSets(30, 7) == 796297179
    assert sol.numberOfSets(2, 1) == 1
    assert sol.numberOfSets(5, 3) == 7

    print("All tests passed!")


if __name__ == "__main__":
    test()
