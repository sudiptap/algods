"""
1525. Number of Good Ways to Split a String (Medium)
https://leetcode.com/problems/number-of-good-ways-to-split-a-string/

Problem:
    Split string s into two non-empty parts. A split is "good" if both
    parts have the same number of distinct characters. Count good splits.

Pattern: 19 - Linear DP

Approach:
    1. Compute prefix distinct counts: for each position i, how many
       distinct characters are in s[:i+1].
    2. Compute suffix distinct counts: for each position i, how many
       distinct characters are in s[i:].
    3. A split after position i is good if prefix_distinct[i] == suffix_distinct[i+1].

Complexity:
    Time:  O(n)
    Space: O(n) for prefix/suffix arrays (or O(26) with rolling sets)
"""


class Solution:
    def numSplits(self, s: str) -> int:
        n = len(s)

        # Prefix distinct counts
        prefix = [0] * n
        seen = set()
        for i in range(n):
            seen.add(s[i])
            prefix[i] = len(seen)

        # Suffix distinct counts
        suffix = [0] * n
        seen = set()
        for i in range(n - 1, -1, -1):
            seen.add(s[i])
            suffix[i] = len(seen)

        count = 0
        for i in range(n - 1):
            if prefix[i] == suffix[i + 1]:
                count += 1

        return count


# ---------- tests ----------
def run_tests():
    sol = Solution()

    # Test 1
    assert sol.numSplits("aacaba") == 2, f"Test 1 failed: {sol.numSplits('aacaba')}"

    # Test 2
    assert sol.numSplits("abcd") == 1, f"Test 2 failed: {sol.numSplits('abcd')}"

    # Test 3
    assert sol.numSplits("aaaaa") == 4, f"Test 3 failed: {sol.numSplits('aaaaa')}"

    # Test 4
    assert sol.numSplits("acbadbaada") == 2, \
        f"Test 4 failed: {sol.numSplits('acbadbaada')}"

    # Test 5: two chars
    assert sol.numSplits("ab") == 1, "Test 5 failed"

    print("All tests passed for 1525. Number of Good Ways to Split a String!")


if __name__ == "__main__":
    run_tests()
