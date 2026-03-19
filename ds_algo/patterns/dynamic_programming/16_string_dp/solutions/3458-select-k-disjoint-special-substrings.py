"""
3458. Select K Disjoint Special Substrings
https://leetcode.com/problems/select-k-disjoint-special-substrings/

Pattern: 16 - String DP (Greedy interval scheduling)

---
APPROACH: Find all valid "special" intervals, then greedily select max non-overlapping.
- A special substring: all occurrences of every character in it are contained within it,
  and it's not the entire string.
- For each char, find [first_occurrence, last_occurrence].
- Expand intervals: for each starting char, expand [lo, hi] to include all chars within.
- Collect valid intervals, sort by end, greedily pick non-overlapping.
- Return whether we can pick >= k.

Time: O(n * 26)  Space: O(n)
---
"""


class Solution:
    def maxSubstringLength(self, s: str, k: int) -> bool:
        n = len(s)
        if k == 0:
            return True

        # First and last occurrence of each character
        first = {}
        last = {}
        for i, c in enumerate(s):
            if c not in first:
                first[c] = i
            last[c] = i

        # Build valid intervals
        intervals = []
        for c in first:
            lo, hi = first[c], last[c]
            # Expand to include all chars whose occurrences fall within [lo, hi]
            i = lo
            valid = True
            while i <= hi:
                ch = s[i]
                if first[ch] < lo:
                    valid = False
                    break
                if last[ch] > hi:
                    hi = last[ch]
                i += 1
            if valid and not (lo == 0 and hi == n - 1):
                intervals.append((lo, hi))

        # Remove duplicates and sort by end
        intervals = sorted(set(intervals), key=lambda x: x[1])

        # Greedy interval scheduling: pick max non-overlapping
        count = 0
        prev_end = -1
        for lo, hi in intervals:
            if lo > prev_end:
                count += 1
                prev_end = hi

        return count >= k


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.maxSubstringLength("abcdbaefab", 2) == True
    assert sol.maxSubstringLength("ccdaabbdcd", 2) == True
    assert sol.maxSubstringLength("aabbcc", 3) == True
    assert sol.maxSubstringLength("a", 1) == False  # single char = entire string

    print("Solution: all tests passed")
