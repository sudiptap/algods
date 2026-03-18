"""
1220. Count Vowels Permutation (Hard)
https://leetcode.com/problems/count-vowels-permutation/

Given an integer n, count how many strings of length n can be formed under the
following rules:
  - 'a' may only be followed by 'e'
  - 'e' may only be followed by 'a' or 'i'
  - 'i' may NOT be followed by another 'i'
  - 'o' may only be followed by 'i' or 'u'
  - 'u' may only be followed by 'a'
Return the count modulo 10^9 + 7.

Pattern: State Machine DP
- 5 states: a, e, i, o, u.
- Transitions (which vowel can PRECEDE the current one):
    a <- e, i, u     (a follows e; a follows i; a follows u)
    e <- a, i         (e follows a; e follows i)
    i <- e, o         (i follows e; i follows o)
    o <- i            (o follows i)
    u <- i, o         (u follows i; u follows o)
- dp[v] = number of strings of current length ending in vowel v.
- Base: dp[v] = 1 for all v (strings of length 1).

Time:  O(n)
Space: O(1)
"""

MOD = 10**9 + 7


class Solution:
    def countVowelPermutation(self, n: int) -> int:
        """Return the number of valid strings of length n under vowel rules.

        Args:
            n: Length of the string, 1 <= n <= 2 * 10^4.

        Returns:
            Count of valid strings modulo 10^9 + 7.
        """
        # a, e, i, o, u
        a = e = i = o = u = 1

        for _ in range(1, n):
            a2 = (e + i + u) % MOD
            e2 = (a + i) % MOD
            i2 = (e + o) % MOD
            o2 = i % MOD
            u2 = (i + o) % MOD
            a, e, i, o, u = a2, e2, i2, o2, u2

        return (a + e + i + o + u) % MOD


# ---------- tests ----------
def test_count_vowel_permutation():
    sol = Solution()

    # n=1: 5 single-character strings
    assert sol.countVowelPermutation(1) == 5

    # n=2: a->e, e->a, e->i, i->a,e,o,u (4), o->i,u (2), u->a => 10
    assert sol.countVowelPermutation(2) == 10

    # n=5: 68
    assert sol.countVowelPermutation(5) == 68

    # Large n
    result = sol.countVowelPermutation(20000)
    assert 0 <= result < MOD

    # n=3: manually verified = 19
    assert sol.countVowelPermutation(3) == 19

    print("All tests passed for 1220. Count Vowels Permutation")


if __name__ == "__main__":
    test_count_vowel_permutation()
