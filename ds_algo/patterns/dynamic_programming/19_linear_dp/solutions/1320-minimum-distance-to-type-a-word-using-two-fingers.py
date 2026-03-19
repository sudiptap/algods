"""
1320. Minimum Distance to Type a Word Using Two Fingers (Hard)
https://leetcode.com/problems/minimum-distance-to-type-a-word-using-two-fingers/

Problem:
    Given a word string on a 6x5 keyboard (A-Z laid out row by row), find
    the minimum total distance to type the word using two fingers. Distance
    between keys is |row1 - row2| + |col1 - col2|. Fingers start above the
    keyboard (no initial cost).

Pattern: 19 - Linear DP

Approach:
    1. dp[prev1][prev2] = min cost so far where finger 1 was last at position
       prev1 and finger 2 at prev2. Use 27 positions: 0-25 for letters A-Z,
       26 for "hovering" (start position, zero cost to reach any key).
    2. For each character in word, try using either finger. Update the
       corresponding finger's position.
    3. Cost function: if finger is at position 26 (start), cost is 0;
       otherwise Manhattan distance on the 6x5 grid.

Complexity:
    Time:  O(n * 27^2) where n = len(word), but with optimization O(n * 27)
    Space: O(27^2) for DP table, reducible to O(27) with rolling
"""


class Solution:
    def minimumDistance(self, word: str) -> int:
        def cost(a: int, b: int) -> int:
            if a == 26 or b == 26:
                return 0
            r1, c1 = divmod(a, 6)
            r2, c2 = divmod(b, 6)
            return abs(r1 - r2) + abs(c1 - c2)

        INF = float('inf')
        # dp[p1][p2] = min cost, where p1 = last pos of finger1, p2 = finger2
        dp = [[INF] * 27 for _ in range(27)]
        dp[26][26] = 0  # both fingers hovering

        for ch in word:
            c = ord(ch) - ord('A')
            ndp = [[INF] * 27 for _ in range(27)]
            for p1 in range(27):
                for p2 in range(27):
                    if dp[p1][p2] == INF:
                        continue
                    # Use finger 1
                    val = dp[p1][p2] + cost(p1, c)
                    if val < ndp[c][p2]:
                        ndp[c][p2] = val
                    # Use finger 2
                    val = dp[p1][p2] + cost(p2, c)
                    if val < ndp[p1][c]:
                        ndp[p1][c] = val
            dp = ndp

        ans = INF
        for p1 in range(27):
            for p2 in range(27):
                ans = min(ans, dp[p1][p2])
        return ans


# ---------- tests ----------
def run_tests():
    sol = Solution()

    # Test 1
    assert sol.minimumDistance("CAKE") == 3, f"Test 1 failed: {sol.minimumDistance('CAKE')}"

    # Test 2
    assert sol.minimumDistance("HAPPY") == 6, f"Test 2 failed: {sol.minimumDistance('HAPPY')}"

    # Test 3: single char
    assert sol.minimumDistance("A") == 0, "Test 3 failed"

    # Test 4: two chars
    assert sol.minimumDistance("AB") == 0, f"Test 4 failed: {sol.minimumDistance('AB')}"

    # Test 5: repeated char
    assert sol.minimumDistance("AAA") == 0, "Test 5 failed"

    # Test 6
    assert sol.minimumDistance("NEW") == 3, f"Test 6 failed: {sol.minimumDistance('NEW')}"

    print("All tests passed for 1320. Minimum Distance to Type a Word Using Two Fingers!")


if __name__ == "__main__":
    run_tests()
