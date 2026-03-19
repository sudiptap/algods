"""
3557. Find Maximum Number of Non Intersecting Substrings
https://leetcode.com/problems/find-maximum-number-of-non-intersecting-substrings/

Pattern: 16 - String DP

---
APPROACH: DP with first/last occurrence
- For each character c, compute first[c] and last[c].
- A valid substring s[i..j] must satisfy: for every character c in s[i..j],
  first[c] >= i and last[c] <= j. This means s[i..j] "contains" all
  occurrences of every character it touches.
- Greedily expand intervals: start at some position i, try to find the
  smallest j such that s[i..j] is valid. Expand j whenever we encounter a
  char whose last occurrence is beyond j.
- Use DP: dp[i] = max non-intersecting substrings in s[0..i-1].
- For each position, either skip it or end a valid substring at it.

Time: O(n * 26)  Space: O(n)
---
"""


class Solution:
    def maxSubstrings(self, word: str) -> int:
        n = len(word)
        first = {}
        last = {}
        for i, c in enumerate(word):
            if c not in first:
                first[c] = i
            last[c] = i

        # For each starting position, find the minimal valid interval
        # A valid interval [i, j]: for all chars in word[i..j], their
        # first and last occurrences are within [i, j].
        # We want to greedily pick as many non-overlapping such intervals.

        # Greedy: scan left to right, for each position try to start an interval
        # and expand minimally, pick it if valid, then jump past it.

        count = 0
        i = 0
        while i < n:
            # Try to form a minimal valid interval starting at first occurrence positions
            # Actually, we should try starting at each i and see if we can close quickly
            j = last[word[i]]
            # Expand: check all chars in word[i..j]
            k = i
            valid = True
            while k <= j:
                c = word[k]
                if first[c] < i:
                    # This char appears before i, so starting at i won't work
                    valid = False
                    break
                if last[c] > j:
                    j = last[c]
                k += 1
            if valid and j < n:
                count += 1
                i = j + 1
            else:
                i += 1
        return count


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.maxSubstrings("abcdba") == 1
    assert sol.maxSubstrings("abcdeafg") == 3
    assert sol.maxSubstrings("abacdda") == 1

    print("All tests passed!")
