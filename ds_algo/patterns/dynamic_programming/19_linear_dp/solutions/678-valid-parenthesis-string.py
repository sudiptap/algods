"""
678. Valid Parenthesis String (Medium)

Given a string s containing only three types of characters: '(', ')' and '*',
return true if s is valid. '*' can be treated as '(', ')' or empty string.

Pattern: Linear DP (Greedy with range tracking)
- Track lo and hi representing the range of possible open parenthesis counts.
- '(' : lo++, hi++
- ')' : lo--, hi--
- '*' : lo-- (treat as ')'), hi++ (treat as '(')
- Clamp lo to 0 (can't have negative open count by choosing '*' as empty).
- If hi < 0 at any point, too many ')' even treating all '*' as '(' -> invalid.
- Valid if lo == 0 at end (there exists a valid assignment).

Time: O(n)
Space: O(1)
"""


class Solution:
    def checkValidString(self, s: str) -> bool:
        """Return True if s is a valid parenthesis string considering '*' wildcards."""
        lo = 0  # minimum possible open parens
        hi = 0  # maximum possible open parens

        for c in s:
            if c == '(':
                lo += 1
                hi += 1
            elif c == ')':
                lo -= 1
                hi -= 1
            else:  # '*'
                lo -= 1  # treat as ')'
                hi += 1  # treat as '('

            if hi < 0:
                # Too many ')' even if all '*' are '('
                return False
            lo = max(lo, 0)  # lo can't go below 0

        return lo == 0


def run_tests():
    sol = Solution()

    # Example 1
    assert sol.checkValidString("()") is True

    # Example 2
    assert sol.checkValidString("(*)") is True

    # Example 3
    assert sol.checkValidString("(*))") is True

    # Empty string is valid
    assert sol.checkValidString("") is True

    # Just stars
    assert sol.checkValidString("***") is True

    # Unmatched open
    assert sol.checkValidString("(((") is False

    # Unmatched close
    assert sol.checkValidString(")))") is False

    # Star can be empty
    assert sol.checkValidString("*") is True

    # Complex valid case
    assert sol.checkValidString("(*)(*)") is True

    # Invalid: close before open with no star help
    assert sol.checkValidString(")(") is False

    # Star used as open and close
    assert sol.checkValidString("*(") is False

    print("All tests passed for 678. Valid Parenthesis String!")


if __name__ == "__main__":
    run_tests()
