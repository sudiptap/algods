"""
1467. Probability of a Two Boxes Having Same Number of Distinct Balls (Hard)
https://leetcode.com/problems/probability-of-a-two-boxes-having-same-number-of-distinct-balls/

Problem:
    Given balls of k colors (balls[i] = count of color i), split them
    equally into two boxes. Find the probability that both boxes have
    the same number of distinct colors.

Pattern: 17 - Probability DP

Approach:
    1. DFS/backtracking over each color, deciding how many balls of that
       color go to box 1 (rest go to box 2).
    2. Track: diff in count (box1_count - box2_count), diff in distinct
       colors (box1_distinct - box2_distinct).
    3. Use multinomial coefficients: for each color i with balls[i] total,
       choosing j for box1 contributes C(balls[i], j).
    4. Valid distributions: diff_count == 0 and diff_distinct == 0.
    5. Probability = valid_arrangements / total_arrangements.

Complexity:
    Time:  O(product of (balls[i]+1)) - enumerate all splits per color
    Space: O(k) for recursion depth
"""

from typing import List
from math import comb, factorial


class Solution:
    def getProbability(self, balls: List[int]) -> float:
        k = len(balls)
        total = sum(balls)
        half = total // 2

        total_ways = 0.0
        valid_ways = 0.0

        def dfs(idx, cnt1, cnt2, dist1, dist2, ways):
            nonlocal total_ways, valid_ways

            if cnt1 > half or cnt2 > half:
                return

            if idx == k:
                if cnt1 == cnt2:
                    total_ways += ways
                    if dist1 == dist2:
                        valid_ways += ways
                return

            for j in range(0, balls[idx] + 1):
                # j balls of color idx go to box1, balls[idx]-j go to box2
                d1 = 1 if j > 0 else 0
                d2 = 1 if (balls[idx] - j) > 0 else 0
                dfs(idx + 1, cnt1 + j, cnt2 + balls[idx] - j,
                    dist1 + d1, dist2 + d2,
                    ways * comb(balls[idx], j))

        dfs(0, 0, 0, 0, 0, 1.0)
        return valid_ways / total_ways


# ---------- tests ----------
def run_tests():
    sol = Solution()

    # Test 1
    result = sol.getProbability([1, 1])
    assert abs(result - 1.0) < 1e-5, f"Test 1 failed: {result}"

    # Test 2
    result = sol.getProbability([2, 1, 1])
    assert abs(result - 0.66667) < 1e-4, f"Test 2 failed: {result}"

    # Test 3
    result = sol.getProbability([1, 2, 1, 2])
    assert abs(result - 0.60000) < 1e-4, f"Test 3 failed: {result}"

    # Test 4
    result = sol.getProbability([3, 2, 1])
    assert abs(result - 0.30000) < 1e-4, f"Test 4 failed: {result}"

    # Test 5
    result = sol.getProbability([6, 6, 6, 6, 6, 6])
    assert 0 <= result <= 1, f"Test 5 failed: {result}"

    print("All tests passed for 1467. Probability of Two Boxes Having Same Number of Distinct Balls!")


if __name__ == "__main__":
    run_tests()
