"""
1638. Count Substrings That Differ by One Character
https://leetcode.com/problems/count-substrings-that-differ-by-one-character/

Pattern: 16 - String DP

---
APPROACH: For each (i,j) pair, expand while exactly one mismatch
- For each pair of positions (i in s, j in t), treat them as the mismatch point.
- Expand outward: count how many matching characters exist before (i,j) and after.
- If there are 'left' matching chars before and 'right' matching chars after,
  then number of valid substrings with mismatch at (i,j) = (left+1) * (right+1).

Time: O(m * n * min(m, n)) or O(m * n) with the expansion trick
Space: O(1)
---
"""


class Solution:
    def countSubstrings(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        result = 0

        for i in range(m):
            for j in range(n):
                if s[i] != t[j]:
                    # (i, j) is the mismatch point
                    # Count matching chars before
                    left = 0
                    while i - left - 1 >= 0 and j - left - 1 >= 0 and s[i - left - 1] == t[j - left - 1]:
                        left += 1
                    # Count matching chars after
                    right = 0
                    while i + right + 1 < m and j + right + 1 < n and s[i + right + 1] == t[j + right + 1]:
                        right += 1
                    result += (left + 1) * (right + 1)

        return result


# --- Tests ---
def test():
    sol = Solution()

    assert sol.countSubstrings("aba", "baba") == 6
    assert sol.countSubstrings("ab", "bb") == 3
    assert sol.countSubstrings("a", "a") == 0
    assert sol.countSubstrings("abe", "bbc") == 10

    print("All tests passed!")


if __name__ == "__main__":
    test()
