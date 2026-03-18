"""
2063. Vowels of All Substrings
https://leetcode.com/problems/vowels-of-all-substrings/

Pattern: 19 - Linear DP (Contribution counting)

---
APPROACH: Count each vowel's contribution across all substrings.
- A character at index i appears in substrings that start at 0..i and
  end at i..n-1.
- Number of substrings containing index i = (i + 1) * (n - i).
- If word[i] is a vowel, add (i + 1) * (n - i) to the answer.

Time: O(n)  Space: O(1)
---
"""


class Solution:
    def countVowels(self, word: str) -> int:
        """Return total number of vowels in all substrings of word."""
        vowels = set("aeiou")
        n = len(word)
        total = 0
        for i, ch in enumerate(word):
            if ch in vowels:
                total += (i + 1) * (n - i)
        return total


# --- Tests ---
def test():
    sol = Solution()

    # Example 1
    assert sol.countVowels("aba") == 6

    # Example 2
    assert sol.countVowels("abc") == 3

    # Example 3
    assert sol.countVowels("ltcd") == 0

    # All vowels: "a"(1v), "ae"(2v), "e"(1v) => 4
    assert sol.countVowels("ae") == 4

    # Single vowel
    assert sol.countVowels("a") == 1

    print("All tests passed!")


if __name__ == "__main__":
    test()
