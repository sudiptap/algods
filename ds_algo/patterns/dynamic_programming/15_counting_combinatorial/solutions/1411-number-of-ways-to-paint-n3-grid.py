"""
1411. Number of Ways to Paint N x 3 Grid (Hard)
https://leetcode.com/problems/number-of-ways-to-paint-n-3-grid/

Problem:
    Paint an n x 3 grid with 3 colors such that no two adjacent cells
    (sharing an edge) have the same color. Return the number of ways mod 10^9+7.

Pattern: 15 - Counting / Combinatorial

Approach:
    1. Each row of 3 cells can be one of two pattern types:
       - ABA pattern (e.g., red-green-red): 6 such colorings
       - ABC pattern (e.g., red-green-blue): 6 such colorings
    2. Row-to-row transitions:
       - ABA -> ABA: 3 ways, ABA -> ABC: 2 ways
       - ABC -> ABA: 2 ways, ABC -> ABC: 2 ways
    3. dp: track count of ABA and ABC patterns per row.

Complexity:
    Time:  O(n)
    Space: O(1)
"""

MOD = 10**9 + 7


class Solution:
    def numOfWays(self, n: int) -> int:
        aba = 6  # ABA patterns for first row
        abc = 6  # ABC patterns for first row

        for _ in range(1, n):
            new_aba = (aba * 3 + abc * 2) % MOD
            new_abc = (aba * 2 + abc * 2) % MOD
            aba, abc = new_aba, new_abc

        return (aba + abc) % MOD


# ---------- tests ----------
def run_tests():
    sol = Solution()

    # Test 1
    assert sol.numOfWays(1) == 12, f"Test 1 failed: {sol.numOfWays(1)}"

    # Test 2
    assert sol.numOfWays(2) == 54, f"Test 2 failed: {sol.numOfWays(2)}"

    # Test 3
    assert sol.numOfWays(3) == 246, f"Test 3 failed: {sol.numOfWays(3)}"

    # Test 4
    assert sol.numOfWays(7) == 106494, f"Test 4 failed: {sol.numOfWays(7)}"

    # Test 5
    assert sol.numOfWays(5000) > 0, "Test 5 failed"

    print("All tests passed for 1411. Number of Ways to Paint N x 3 Grid!")


if __name__ == "__main__":
    run_tests()
