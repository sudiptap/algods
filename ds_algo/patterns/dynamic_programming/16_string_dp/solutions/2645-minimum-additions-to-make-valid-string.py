"""
2645. Minimum Additions to Make Valid String
https://leetcode.com/problems/minimum-additions-to-make-valid-string/

Pattern: 16 - String DP (Greedy matching against "abc")

---
APPROACH: Greedily match characters of word against repeated "abc" pattern.
For each group of "abc", track which letters we actually have and count
the missing ones.

Time: O(n)  Space: O(1)
---
"""


class Solution:
    def addMinimum(self, word: str) -> int:
        adds = 0
        i = 0
        n = len(word)
        while i < n:
            # Try to match a, b, c in order
            if word[i] == 'a':
                i += 1
                if i < n and word[i] == 'b':
                    i += 1
                    if i < n and word[i] == 'c':
                        i += 1  # full "abc"
                    else:
                        adds += 1  # missing c
                else:
                    if i < n and word[i] == 'c':
                        i += 1
                        adds += 1  # missing b
                    else:
                        adds += 2  # missing b, c
            elif word[i] == 'b':
                adds += 1  # missing a
                i += 1
                if i < n and word[i] == 'c':
                    i += 1
                else:
                    adds += 1  # missing c
            else:  # word[i] == 'c'
                adds += 2  # missing a, b
                i += 1
        return adds


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.addMinimum("b") == 2
    assert sol.addMinimum("aaa") == 6
    assert sol.addMinimum("abc") == 0
    assert sol.addMinimum("abcabc") == 0
    assert sol.addMinimum("abcb") == 2

    print("All tests passed!")
