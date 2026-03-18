"""
1653. Minimum Deletions to Make String Balanced (Medium)
https://leetcode.com/problems/minimum-deletions-to-make-string-balanced/

Given a string s consisting only of 'a' and 'b', return the minimum number
of deletions needed to make s balanced. A string is balanced if there is no
pair (i, j) with i < j where s[i] = 'b' and s[j] = 'a'.

In other words, all 'a's must come before all 'b's.

Approach - Linear scan (like #926):
    Track b_count (number of 'b's seen so far) and deletions.
    - If current char is 'b': increment b_count, no deletion needed.
    - If current char is 'a' after some 'b's: either delete this 'a'
      (deletions + 1) or delete all preceding 'b's (b_count).
      deletions = min(deletions + 1, b_count).

Time:  O(n)
Space: O(1)
"""


class Solution:
    def minimumDeletions(self, s: str) -> int:
        """Return minimum deletions to make s balanced (all a's before b's).

        Single pass tracking b_count and running deletion count.

        Args:
            s: String of 'a' and 'b' characters, 1 <= len(s) <= 10^5.

        Returns:
            Minimum number of character deletions.
        """
        b_count = 0
        deletions = 0

        for ch in s:
            if ch == 'b':
                b_count += 1
            else:  # ch == 'a'
                deletions = min(deletions + 1, b_count)

        return deletions


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    # Example 1
    assert sol.minimumDeletions("aababbab") == 2

    # Example 2
    assert sol.minimumDeletions("bbaaaaabb") == 2

    # Already balanced
    assert sol.minimumDeletions("aaabbb") == 0

    # All a's
    assert sol.minimumDeletions("aaaa") == 0

    # All b's
    assert sol.minimumDeletions("bbbb") == 0

    # Reverse order
    assert sol.minimumDeletions("ba") == 1

    # Single character
    assert sol.minimumDeletions("a") == 0

    # Alternating
    assert sol.minimumDeletions("bababab") == 3

    print("All tests passed!")
