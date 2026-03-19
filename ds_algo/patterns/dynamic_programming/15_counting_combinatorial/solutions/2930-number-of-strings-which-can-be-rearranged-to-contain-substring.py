"""
2930. Number of Strings Which Can Be Rearranged to Contain Substring
https://leetcode.com/problems/number-of-strings-which-can-be-rearranged-to-contain-substring/

Pattern: 15 - Counting / Combinatorial (Inclusion-exclusion or DP with 4 states)

---
APPROACH: Use DP with states tracking how many 'l's we've seen (0,1,2+),
whether we've seen 'e', and whether we've seen 't'. We need >= 1 'l', >= 1 'e',
>= 1 'e' (wait: need "leet" substring after rearrangement = at least one 'l',
one 'e', one 'e', one 't' = at least 2 'e's, 1 'l', 1 't').
State: (count_l: 0/1/2+, count_e: 0/1/2+, has_t: 0/1). Use matrix exponentiation.

Time: O(log n)  Space: O(1)
---
"""

MOD = 10**9 + 7


class Solution:
    def stringCount(self, n: int) -> int:
        # Inclusion-exclusion: total - (missing at least one requirement)
        # Requirements: >= 1 'l', >= 2 'e', >= 1 't'
        # Total = 26^n
        # A = no 'l', B = < 2 'e's (0 or 1 'e'), C = no 't'
        # |A| = 25^n (no 'l')
        # |B| = 25^n + n * 25^(n-1) ... wait, strings with <2 'e's:
        #   0 'e's: 25^n, 1 'e': n * 25^(n-1) -> but these use other 25 chars
        # Actually for strings of length n with exactly k 'e's:
        # C(n,k) * 25^(n-k). So |B| = 25^n + n*25^(n-1)
        # |C| = 25^n

        # |A∩B| = strings with no 'l' and < 2 'e's
        #   0 'e': 24^n (no l, no e), 1 'e': n*24^(n-1)
        # |A∩C| = no 'l', no 't' = 24^n
        # |B∩C| = < 2 'e's, no 't'
        #   0 'e': 24^n, 1 'e': n*24^(n-1)
        # |A∩B∩C| = no 'l', < 2 'e's, no 't'
        #   0 'e': 23^n, 1 'e': n*23^(n-1)

        # By inclusion-exclusion: answer = total - |A| - |B| - |C| + |A∩B| + |A∩C| + |B∩C| - |A∩B∩C|

        p = pow
        ans = (p(26, n, MOD)
               - p(25, n, MOD)  # no l
               - (p(25, n, MOD) + n * p(25, n - 1, MOD))  # < 2 e
               - p(25, n, MOD)  # no t
               + (p(24, n, MOD) + n * p(24, n - 1, MOD))  # no l, < 2 e
               + p(24, n, MOD)  # no l, no t
               + (p(24, n, MOD) + n * p(24, n - 1, MOD))  # < 2 e, no t
               - (p(23, n, MOD) + n * p(23, n - 1, MOD))  # no l, < 2 e, no t
               - p(23, n, MOD)  # no l, no t... wait I already counted that
               ) % MOD

        # Let me redo more carefully:
        # A = missing 'l' (0 l's): use 25 other chars -> 25^n
        # B = missing enough 'e' (< 2 e's): C(n,0)*25^n + C(n,1)*1*25^(n-1) = 25^n + n*25^(n-1)
        # C = missing 't' (0 t's): 25^n

        # A∩B = no l, <2 e: 0 e: 24^n, 1 e: n*24^(n-1) -> 24^n + n*24^(n-1)
        # A∩C = no l, no t: 24^n
        # B∩C = <2 e, no t: 0 e: 24^n, 1 e: n*24^(n-1) -> 24^n + n*24^(n-1)

        # A∩B∩C = no l, <2 e, no t: 0 e: 23^n, 1 e: n*23^(n-1) -> 23^n + n*23^(n-1)

        total = p(26, n, MOD)
        A = p(25, n, MOD)
        B = (p(25, n, MOD) + n * p(25, max(n-1,0), MOD)) % MOD
        C = p(25, n, MOD)
        AB = (p(24, n, MOD) + n * p(24, max(n-1,0), MOD)) % MOD
        AC = p(24, n, MOD)
        BC = (p(24, n, MOD) + n * p(24, max(n-1,0), MOD)) % MOD
        ABC = (p(23, n, MOD) + n * p(23, max(n-1,0), MOD)) % MOD

        return (total - A - B - C + AB + AC + BC - ABC) % MOD


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.stringCount(4) == 12
    assert sol.stringCount(10) == 83943898

    print("All tests passed!")
