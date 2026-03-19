"""
2484. Count Palindromic Subsequences
https://leetcode.com/problems/count-palindromic-subsequences/

Pattern: 08 - Palindromic Subsequence

---
APPROACH: Count 5-length palindromic subsequences with fixed outer/inner digits
- A palindrome of length 5: d1 d2 x d2 d1
- For each pair (d1, d2), count ways = (prefix pairs ending at i) * (suffix pairs starting after i) for middle char.
- Precompute: for each position, prefix count of subsequences (d1, d2) and suffix count.
- prefix[i][(d1,d2)] = number of subsequences of length 2 = (d1,d2) in s[:i]
- suffix[i][(d1,d2)] = number of subsequences of length 2 = (d1,d2) in s[i+1:]
- For each middle position i, answer += sum over (d1,d2) of prefix[i][(d1,d2)] * suffix[i][(d2,d1)]
  Wait: palindrome is d1 d2 x d2 d1, so suffix needs (d2, d1).

Time: O(n * 100)  Space: O(n * 100)
---
"""


class Solution:
    def countPalindromes(self, s: str) -> int:
        MOD = 10**9 + 7
        n = len(s)

        # prefix[i][d1][d2] = count of 2-char subsequences (d1,d2) in s[:i]
        prefix = [[[0] * 10 for _ in range(10)] for _ in range(n + 1)]
        # count1[d] = count of digit d seen so far
        count1 = [0] * 10

        for i in range(n):
            d = int(s[i])
            # Copy previous
            for a in range(10):
                for b in range(10):
                    prefix[i + 1][a][b] = prefix[i][a][b]
            # New pairs: (a, d) for all a seen before
            for a in range(10):
                prefix[i + 1][a][d] = (prefix[i + 1][a][d] + count1[a]) % MOD
            count1[d] += 1

        # suffix[i][d1][d2] = count of 2-char subsequences (d1,d2) in s[i+1:]
        suffix = [[[0] * 10 for _ in range(10)] for _ in range(n + 1)]
        count1 = [0] * 10

        for i in range(n - 1, -1, -1):
            d = int(s[i])
            for a in range(10):
                for b in range(10):
                    suffix[i][a][b] = suffix[i + 1][a][b]
            # New pairs: (d, a) for all a seen after (to the right)
            for a in range(10):
                suffix[i][d][a] = (suffix[i][d][a] + count1[a]) % MOD
            count1[d] += 1

        ans = 0
        for i in range(2, n - 2):
            for d1 in range(10):
                for d2 in range(10):
                    # palindrome: d1 d2 s[i] d2 d1
                    # prefix needs (d1, d2) in s[:i], suffix needs (d2, d1) in s[i+1:]
                    ans = (ans + prefix[i][d1][d2] * suffix[i + 1][d2][d1]) % MOD

        return ans


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.countPalindromes("103301") == 2
    assert sol.countPalindromes("0000000") == 21
    assert sol.countPalindromes("9999900000") == 2

    print("all tests passed")
