"""
3700. Number of ZigZag Arrays II
https://leetcode.com/problems/number-of-zigzag-arrays-ii/

Pattern: 15 - Counting / Combinatorial DP

---
APPROACH: Optimized zigzag counting
- Same as ZigZag Arrays I but with larger constraints requiring O(n) or
  O(n log n) approach.
- Use the recurrence for Euler/tangent numbers with rolling array.
- A(n) can be computed iteratively in O(n) space using the tangent number
  recurrence.

Time: O(n^2) with optimization  Space: O(n)
---
"""

MOD = 10**9 + 7


class Solution:
    def numberOfZigZagArrays(self, n: int, k: int) -> int:
        if n <= 0:
            return 0
        if n == 1:
            return 1

        # Use rolling Entringer number computation
        # E[k] represents E(current_n, k)
        E = [0] * (n + 1)
        E[0] = 1  # E(0,0) = 1

        for i in range(1, n + 1):
            # Compute E(i, 0..i) from E(i-1, 0..i-1)
            new_E = [0] * (n + 1)
            new_E[0] = 0
            for j in range(1, i + 1):
                new_E[j] = (new_E[j - 1] + E[i - j]) % MOD
            E = new_E

        return E[n] % MOD


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.numberOfZigZagArrays(1, 0) == 1
    assert sol.numberOfZigZagArrays(2, 0) == 1
    assert sol.numberOfZigZagArrays(3, 0) == 2
    assert sol.numberOfZigZagArrays(4, 0) == 5
    assert sol.numberOfZigZagArrays(5, 0) == 16

    print("All tests passed!")
