"""
2851. String Transformation
https://leetcode.com/problems/string-transformation/

Pattern: 16 - String DP (KMP + Matrix Exponentiation)

---
APPROACH: Concatenate s+s and use KMP to count how many rotations of s equal t.
Let cnt = number of matching rotations. The transition matrix for k steps:
from matching rotation we can go to another matching (cnt-1 ways) or non-matching
(n-cnt ways), and vice versa. Use matrix exponentiation to compute k-step result.

Time: O(n + log k)  Space: O(n)
---
"""

MOD = 10**9 + 7


class Solution:
    def numberOfWays(self, s: str, t: str, k: int) -> int:
        n = len(s)

        # Count rotations of s that equal t using KMP on t in (s+s)[:-1]
        def kmp_count(text, pattern):
            m = len(pattern)
            # Build failure function
            fail = [0] * m
            j = 0
            for i in range(1, m):
                while j > 0 and pattern[i] != pattern[j]:
                    j = fail[j - 1]
                if pattern[i] == pattern[j]:
                    j += 1
                fail[i] = j

            count = 0
            j = 0
            for i in range(len(text)):
                while j > 0 and text[i] != pattern[j]:
                    j = fail[j - 1]
                if text[i] == pattern[j]:
                    j += 1
                if j == m:
                    count += 1
                    j = fail[j - 1]
            return count

        doubled = (s + s)[1:]  # rotations at positions 1..n-1, plus position 0 check
        cnt_nonzero = kmp_count(doubled, t)
        # Check rotation 0 (s itself == t)
        is_zero = 1 if s == t else 0
        # cnt_nonzero counts matches in positions 0..n-2 of doubled = s[1:]+s
        # which corresponds to rotations 1..n-1
        # Total matching rotations:
        cnt = cnt_nonzero + is_zero  # but we need to be careful
        # Actually let me redo: rotations of s are s[i:]+s[:i] for i=0..n-1
        # We want to count how many equal t.
        # s+s contains all rotations as substrings at positions 0..n-1
        # So search t in (s+s)[0:2n-1]
        cnt = kmp_count((s + s)[:2 * n - 1], t)

        # Matrix exponentiation
        # State: currently matching (M) or not matching (N)
        # From M: cnt-1 ways to stay M, n-cnt ways to go N
        # From N: cnt ways to go M, n-cnt-1 ways to stay N
        # We start at state M if s==t, else N
        # After k steps, we want count of ways to be at M

        def mat_mult(A, B):
            return [
                [(A[0][0] * B[0][0] + A[0][1] * B[1][0]) % MOD,
                 (A[0][0] * B[0][1] + A[0][1] * B[1][1]) % MOD],
                [(A[1][0] * B[0][0] + A[1][1] * B[1][0]) % MOD,
                 (A[1][0] * B[0][1] + A[1][1] * B[1][1]) % MOD]
            ]

        def mat_pow(M, p):
            result = [[1, 0], [0, 1]]  # identity
            while p:
                if p & 1:
                    result = mat_mult(result, M)
                M = mat_mult(M, M)
                p >>= 1
            return result

        # Transition matrix: [M->M, N->M; M->N, N->N]
        # but we want column-based: next = T * current
        # T = [[cnt-1, cnt], [n-cnt, n-cnt-1]]
        T = [
            [(cnt - 1) % MOD, cnt % MOD],
            [(n - cnt) % MOD, (n - cnt - 1) % MOD]
        ]

        Tk = mat_pow(T, k)

        # Initial state: [1, 0] if s==t (start at M), else [0, 1] (start at N)
        if s == t:
            return Tk[0][0]
        else:
            return Tk[0][1]


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.numberOfWays("abcd", "cdab", 2) == 2
    assert sol.numberOfWays("ababab", "ababab", 1) == 2

    print("All tests passed!")
