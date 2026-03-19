"""
2746. Decremental String Concatenation
https://leetcode.com/problems/decremental-string-concatenation/

Pattern: 16 - String DP (dp[i][first][last] tracking endpoints)

---
APPROACH: When concatenating s1+s2, we can overlap if last char of s1 == first
char of s2 (saving overlap). Track dp[i][first_char][last_char] = min length
after processing first i+1 words. Only first and last chars matter for overlap.

Time: O(n * 26 * 26)  Space: O(26 * 26)
---
"""

from typing import List


class Solution:
    def minimizeConcatenatedLength(self, words: List[str]) -> int:
        n = len(words)
        # State: (first_char, last_char) -> min length
        dp = {}
        w0 = words[0]
        dp[(w0[0], w0[-1])] = len(w0)

        for i in range(1, n):
            w = words[i]
            wf, wl, wlen = w[0], w[-1], len(w)
            new_dp = {}
            for (f, l), length in dp.items():
                # Option 1: current_string + w  (overlap if l == wf)
                new_len1 = length + wlen - (1 if l == wf else 0)
                key1 = (f, wl)
                if key1 not in new_dp or new_dp[key1] > new_len1:
                    new_dp[key1] = new_len1

                # Option 2: w + current_string  (overlap if wl == f)
                new_len2 = length + wlen - (1 if wl == f else 0)
                key2 = (wf, l)
                if key2 not in new_dp or new_dp[key2] > new_len2:
                    new_dp[key2] = new_len2
            dp = new_dp

        return min(dp.values())


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.minimizeConcatenatedLength(["aa", "ab", "bc"]) == 4
    assert sol.minimizeConcatenatedLength(["ab", "b"]) == 2
    assert sol.minimizeConcatenatedLength(["aaa", "c", "aba"]) == 6

    print("All tests passed!")
