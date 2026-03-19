"""
2002. Maximum Product of the Length of Two Palindromic Subsequences (Medium)
https://leetcode.com/problems/maximum-product-of-the-length-of-two-palindromic-subsequences/

Given string s (len <= 12), find two disjoint palindromic subsequences
and maximize the product of their lengths.

Pattern: Palindromic Subsequence (Bitmask Enumeration)
Approach:
- Enumerate all 2^n subsets. For each subset, check if it forms a
  palindrome.
- Store all palindromic masks with their lengths.
- For each pair of palindromic masks, check if they are disjoint
  (mask1 & mask2 == 0). Track max product.
- Optimization: iterate over palindromic masks and their complements.

Time:  O(3^n) or O(2^n * n) for checking + O(4^n) worst case for pairs
Space: O(2^n)
"""


class Solution:
    def maxProduct(self, s: str) -> int:
        """Return max product of lengths of two disjoint palindromic subsequences.

        Args:
            s: Input string (length <= 12).

        Returns:
            Maximum product.
        """
        n = len(s)

        # For each mask, check if the subsequence is a palindrome
        palindrome_len = {}
        for mask in range(1, 1 << n):
            # Extract subsequence
            subseq = []
            for i in range(n):
                if mask & (1 << i):
                    subseq.append(s[i])
            # Check palindrome
            if subseq == subseq[::-1]:
                palindrome_len[mask] = len(subseq)

        # Find max product of disjoint palindromic masks
        best = 0
        pal_masks = list(palindrome_len.keys())
        for i in range(len(pal_masks)):
            m1 = pal_masks[i]
            l1 = palindrome_len[m1]
            for j in range(i + 1, len(pal_masks)):
                m2 = pal_masks[j]
                if m1 & m2 == 0:
                    best = max(best, l1 * palindrome_len[m2])

        return best


# ---------- tests ----------
def test_max_product():
    sol = Solution()

    # Example 1: "leetcodecom" -> "ee" and "cdc" -> 2*3=6? Actually 2*5=10?
    # "ete" (len 3) and "coc" (len 3) -> 9? Let's trust LeetCode: answer = 9
    assert sol.maxProduct("leetcodecom") == 9

    # Example 2: "bb" -> "b" and "b" -> 1
    assert sol.maxProduct("bb") == 1

    # Example 3: "accbcaxxcxx" -> answer = 25
    assert sol.maxProduct("accbcaxxcxx") == 25

    # Single char repeated
    assert sol.maxProduct("ab") == 1

    print("All tests passed for 2002. Maximum Product of Two Palindromic Subsequences")


if __name__ == "__main__":
    test_max_product()
