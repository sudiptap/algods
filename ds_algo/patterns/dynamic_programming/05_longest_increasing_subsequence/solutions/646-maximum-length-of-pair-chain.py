"""
646. Maximum Length of Pair Chain (Medium)
https://leetcode.com/problems/maximum-length-of-pair-chain/

Given n pairs where pairs[i] = [left_i, right_i] and left_i < right_i,
a pair (c, d) can follow (a, b) if b < c. Find the longest chain.

Approach 1 - Greedy (Activity Selection):
    Sort pairs by their second element. Greedily pick the next pair whose
    start is strictly greater than the current chain's last end.
    This is identical to the classic activity selection / interval scheduling
    problem.

Approach 2 - LIS-style DP:
    Sort by first element, then dp[i] = max chain ending at pair i.

Time:  O(n log n) greedy, O(n^2) DP
Space: O(1) greedy (ignoring sort), O(n) DP
"""

from typing import List


class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        """Return the maximum length of a pair chain.

        Uses greedy activity selection: sort by end value, always pick
        the next compatible pair with the smallest end.

        Args:
            pairs: List of [left, right] pairs with left < right.

        Returns:
            Length of the longest chain of pairs.
        """
        pairs.sort(key=lambda p: p[1])

        chain_length = 0
        cur_end = float("-inf")

        for left, right in pairs:
            if left > cur_end:
                chain_length += 1
                cur_end = right

        return chain_length

    def findLongestChain_dp(self, pairs: List[List[int]]) -> int:
        """LIS-style O(n^2) DP approach for reference.

        Args:
            pairs: List of [left, right] pairs with left < right.

        Returns:
            Length of the longest chain of pairs.
        """
        pairs.sort()
        n = len(pairs)
        dp = [1] * n

        for i in range(1, n):
            for j in range(i):
                if pairs[j][1] < pairs[i][0]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)


# --- Tests ---

def test_example1():
    sol = Solution()
    assert sol.findLongestChain([[1, 2], [2, 3], [3, 4]]) == 2

def test_example2():
    sol = Solution()
    assert sol.findLongestChain([[1, 2], [7, 8], [4, 5]]) == 3

def test_single_pair():
    sol = Solution()
    assert sol.findLongestChain([[1, 5]]) == 1

def test_all_overlapping():
    sol = Solution()
    assert sol.findLongestChain([[1, 10], [2, 9], [3, 8]]) == 1

def test_negative_values():
    sol = Solution()
    assert sol.findLongestChain([[-10, -5], [-3, 0], [1, 4]]) == 3

def test_dp_matches_greedy():
    sol = Solution()
    cases = [
        [[1, 2], [2, 3], [3, 4]],
        [[1, 2], [7, 8], [4, 5]],
        [[-10, -5], [-3, 0], [1, 4]],
    ]
    for pairs in cases:
        assert sol.findLongestChain(pairs) == sol.findLongestChain_dp(pairs)


if __name__ == "__main__":
    test_example1()
    test_example2()
    test_single_pair()
    test_all_overlapping()
    test_negative_values()
    test_dp_matches_greedy()
    print("All tests passed!")
