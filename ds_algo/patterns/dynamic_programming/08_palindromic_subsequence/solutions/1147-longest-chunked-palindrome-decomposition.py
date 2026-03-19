"""
1147. Longest Chunked Palindrome Decomposition (Hard)

Pattern: 08_palindromic_subsequence
- Decompose string into maximum k chunks such that the i-th chunk equals the (k-i+1)-th chunk.

Approach:
- Greedy two-pointer: try to match the shortest prefix of the remaining string
  with the shortest suffix.
- Use left pointer l and right pointer r. Grow prefix from l and suffix from r.
  When prefix == suffix, count 2 chunks and reset the prefix/suffix.
- If there's a middle portion left, count 1 more chunk.
- Greedy works because matching shorter chunks leaves more room for further matches,
  maximizing the total count.

Complexity:
- Time:  O(n^2) due to string comparison; O(n) with rolling hash
- Space: O(n) for substring storage
"""


class Solution:
    def longestDecomposition(self, text: str) -> int:
        n = len(text)
        count = 0
        l, r = 0, n - 1
        prefix = ""
        suffix = ""

        while l < r:
            prefix += text[l]
            suffix = text[r] + suffix
            if prefix == suffix:
                count += 2
                prefix = ""
                suffix = ""
            l += 1
            r -= 1

        # If there's leftover (middle char or unmatched middle section)
        if l == r or prefix:
            count += 1

        return count


# ---------- Tests ----------
def test():
    sol = Solution()

    # Example 1: "ghiabcdefhelloghjabcdefhellog" -> 7
    # g | hiabcdefhello | ghj | abcdefhello | g => wait, let's verify
    # Actually greedy: g matches g(end) -> 2, then hiabcdefhello vs hjabcdefhello
    # h matches h -> 2 more, iabcdefhello vs jabcdefhello -> no single match
    # ia vs lo? no... "iabcdefhello" vs "jabcdefhello" -> full match? no (i!=j)
    # So: g|h|iabcdefhelloghjabcdefhello -> not 7. Use verified test cases only.
    assert sol.longestDecomposition("volvo") == 3  # "vo" + "l" + "vo"
    assert sol.longestDecomposition("aaa") == 3

    # Example 2: "merchant" -> 1
    assert sol.longestDecomposition("merchant") == 1

    # Example 3: "antaprezatepzapreanta" -> 11
    assert sol.longestDecomposition("antaprezatepzapreanta") == 11

    # Single char
    assert sol.longestDecomposition("a") == 1

    # All same chars
    assert sol.longestDecomposition("aaaa") == 4

    # Palindrome: a|b|c|b|a = 5
    assert sol.longestDecomposition("abcba") == 5

    # Two halves equal: ab|ab = 2
    assert sol.longestDecomposition("abab") == 2

    print("All tests passed!")


if __name__ == "__main__":
    test()
