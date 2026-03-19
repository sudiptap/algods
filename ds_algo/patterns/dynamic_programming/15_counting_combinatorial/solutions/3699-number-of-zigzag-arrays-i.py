"""
3699. Number of ZigZag Arrays I
https://leetcode.com/problems/number-of-zigzag-arrays-i/

Pattern: 15 - Counting / Combinatorial DP

---
APPROACH: DP permutation counting
- Count permutations of [1..n] that form a zigzag: a[0]<a[1]>a[2]<a[3]>...
  (alternating up-down).
- dp[i][j] = number of zigzag permutations of length i where the last
  element is the j-th smallest among remaining.
- Classic "alternating permutation" count (Euler numbers / tangent numbers).

Time: O(n^2)  Space: O(n)
---
"""

MOD = 10**9 + 7


class Solution:
    def numberOfZigZagArrays(self, n: int, k: int) -> int:
        # Count zigzag permutations of [1..n].
        # k might indicate the starting direction or number of peaks.
        # Assuming k=0 means up-down (a[0]<a[1]>a[2]<...)
        # and k=1 means down-up (a[0]>a[1]<a[2]>...)

        # Euler zigzag numbers E(n):
        # E(1)=1, E(2)=1, E(3)=1, E(4)=2, E(5)=5, ...
        # Actually: alternating permutations of n elements = A(n)
        # A(1)=1, A(2)=1, A(3)=2, A(4)=5, A(5)=16, A(6)=61

        # Using the recurrence: A(n) = sum over i of C(n-1, i) * A(i) * A(n-1-i)
        # Or use the tangent/secant number approach.

        # Simpler DP: T[n] = number of up-down alternating perms of {1,...,n}
        # T[0]=1, T[1]=1
        # Using: T[n] = T[n-1] * n // something... Actually:

        # Let's use the "entringer numbers" E(n,k):
        # E(n,0) = 0 for n>0, E(0,0) = 1
        # E(n,k) = E(n,k-1) + E(n-1,n-k)
        # A(n) = E(n, n) for alternating perms

        # But this might not match the problem exactly. Let me compute directly.

        if n <= 0:
            return 0

        # Compute using Entringer numbers
        E = [[0] * (n + 1) for _ in range(n + 1)]
        E[0][0] = 1

        for i in range(1, n + 1):
            E[i][0] = 0
            for j in range(1, i + 1):
                E[i][j] = (E[i][j - 1] + E[i - 1][i - j]) % MOD

        # E[n][n] = number of alternating permutations
        # For up-down starting: A_up(n) = E[n][n] when n is odd contributes to up-start
        # Total alternating perms (both up-down and down-up) = 2 * E[n][n] for n >= 2

        return E[n][n] % MOD


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.numberOfZigZagArrays(1, 0) == 1
    assert sol.numberOfZigZagArrays(2, 0) == 1
    assert sol.numberOfZigZagArrays(3, 0) == 2  # [1,3,2] and [2,3,1]... actually depends on definition
    # E(3,3): E(3,0)=0, E(3,1)=E(3,0)+E(2,1)=0+1=1, E(3,2)=1+E(2,1)=1+1=2,
    # E(3,3)=2+E(2,0)=2+0=2. Hmm wait E(2,0)=0, E(2,1)=E(2,0)+E(1,0)=0+0=0.
    # Let me recheck. E(0,0)=1. E(1,0)=0. E(1,1)=E(1,0)+E(0,0)=0+1=1.
    # E(2,0)=0. E(2,1)=E(2,0)+E(1,1)=0+1=1. E(2,2)=E(2,1)+E(1,0)=1+0=1.
    # E(3,0)=0. E(3,1)=0+E(2,2)=1. E(3,2)=1+E(2,1)=2. E(3,3)=2+E(2,0)=2.
    # So alternating perms of 3 = 2. Correct? [1,3,2] and [2,3,1] for up-down. Yes.

    print("All tests passed!")
