"""
1987. Number of Unique Good Subsequences (Hard)
https://leetcode.com/problems/number-of-unique-good-subsequences/

Given binary string, return number of unique good subsequences.
A good subsequence is non-empty and has no leading zeros (except "0" itself).

Pattern: String DP
Approach:
- Track dp ending in 0 (a) and ending in 1 (b).
- For char '0': new_a = a + b (append 0 to all seqs ending in 0 or 1).
  But "0" alone is special — handle separately.
- For char '1': new_b = a + b + 1 (append 1 to all, or start new "1").
- The "+1" for '1' accounts for starting a new subsequence with "1".
- Add 1 at the end if "0" exists in the string (for the subsequence "0").

Time:  O(n)
Space: O(1)
"""


class Solution:
    def numberOfUniqueGoodSubsequences(self, binary: str) -> int:
        """Return number of unique good subsequences of binary string.

        Args:
            binary: Binary string.

        Returns:
            Count of unique good subsequences mod 10^9 + 7.
        """
        MOD = 10**9 + 7
        # a = count of unique subsequences ending with '0' (excluding bare "0")
        # b = count of unique subsequences ending with '1'
        a = 0
        b = 0
        has_zero = 0

        for ch in binary:
            if ch == '0':
                a = (a + b) % MOD
                has_zero = 1
            else:
                b = (a + b + 1) % MOD

        return (a + b + has_zero) % MOD


# ---------- tests ----------
def test_unique_good_subsequences():
    sol = Solution()

    # Example 1: "001" -> "0", "1", "01" -> 3? Actually "0","1","01" = 3... wait
    # Unique good: "0", "0" (dup), "1", "01" -> "0","1","01" = 3? Let me check.
    # "001": subsequences without leading zeros: "0", "01", "1", "001"->leading zero
    # Actually "001" as subsequence has leading zero. Good ones: "0","1","01" = 3? No...
    # Wait: "0" is allowed. "1" is allowed. "01" has leading zero -> not good (except "0").
    # Hmm, "01" starts with 0 -> leading zero -> not good.
    # So: "0", "1" = 2? Let me recheck.
    # Actually subsequences: from "001": "0"(x2), "0"(x1 from second), "1", "00", "01"(x2), "001"
    # Good (no leading zero except "0"): "0", "1" -> 2
    assert sol.numberOfUniqueGoodSubsequences("001") == 2

    # Example 2: "11" -> "1", "11" -> 2
    assert sol.numberOfUniqueGoodSubsequences("11") == 2

    # Example 3: "101" -> "0", "1", "10", "11", "101" -> 5
    assert sol.numberOfUniqueGoodSubsequences("101") == 5

    # "0" -> just "0" -> 1
    assert sol.numberOfUniqueGoodSubsequences("0") == 1

    # "1" -> just "1" -> 1
    assert sol.numberOfUniqueGoodSubsequences("1") == 1

    print("All tests passed for 1987. Number of Unique Good Subsequences")


if __name__ == "__main__":
    test_unique_good_subsequences()
