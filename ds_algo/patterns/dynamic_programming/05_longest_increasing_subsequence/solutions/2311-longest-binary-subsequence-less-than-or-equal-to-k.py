"""
2311. Longest Binary Subsequence <= K
https://leetcode.com/problems/longest-binary-subsequence-less-than-or-equal-to-k/

Pattern: 05 - Longest Increasing Subsequence

---
APPROACH: Greedy - keep all 0s, add 1s from right if value <= k
- All '0's can always be included (they don't increase value).
- For '1's, process from right to left. Each '1' at position p from the right
  contributes 2^p to the value. Add it if total stays <= k.
- Count zeros first, then greedily add 1s from the right.

Time: O(n)  Space: O(1)
---
"""


class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        n = len(s)
        zeros = s.count('0')
        result = zeros
        val = 0
        power = 0

        # Process from right to left
        for i in range(n - 1, -1, -1):
            if s[i] == '1':
                if power < 30 and val + (1 << power) <= k:
                    val += (1 << power)
                    result += 1
                elif power >= 30:
                    break
            power += 1

        return result


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.longestSubsequence("1001010", 5) == 5
    assert sol.longestSubsequence("00101001", 1) == 6
    assert sol.longestSubsequence("0", 0) == 1
    assert sol.longestSubsequence("1", 1) == 1
    assert sol.longestSubsequence("1", 0) == 0

    print("all tests passed")
