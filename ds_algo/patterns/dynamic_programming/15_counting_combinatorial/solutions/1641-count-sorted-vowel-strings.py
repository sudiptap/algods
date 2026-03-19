"""
1641. Count Sorted Vowel Strings
https://leetcode.com/problems/count-sorted-vowel-strings/

Pattern: 15 - Counting / Combinatorial DP

---
APPROACH: Stars and Bars
- We need strings of length n using 5 vowels in non-decreasing order.
- This is equivalent to: distribute n items into 5 bins (multiset coefficient).
- Formula: C(n + 4, 4) = C(n+4, 4)

Time: O(1)
Space: O(1)
---
"""

from math import comb


class Solution:
    def countVowelStrings(self, n: int) -> int:
        return comb(n + 4, 4)


# --- Tests ---
def test():
    sol = Solution()

    assert sol.countVowelStrings(1) == 5
    assert sol.countVowelStrings(2) == 15
    assert sol.countVowelStrings(33) == 66045
    assert sol.countVowelStrings(3) == 35

    print("All tests passed!")


if __name__ == "__main__":
    test()
