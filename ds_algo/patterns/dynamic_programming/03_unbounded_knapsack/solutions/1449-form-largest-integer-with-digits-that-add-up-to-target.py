"""
1449. Form Largest Integer With Digits That Add up to Target (Hard)
https://leetcode.com/problems/form-largest-integer-with-digits-that-add-up-to-target/

Problem:
    Given cost[i] = cost to paint digit (i+1), and a target budget,
    paint digits to form the largest possible integer. Return "0" if
    impossible.

Pattern: 03 - Unbounded Knapsack

Approach:
    1. First maximize the number of digits (more digits = larger number).
       dp[t] = max number of digits achievable with budget t.
    2. Then greedily reconstruct: for each position, try digit 9 down to 1,
       pick the largest digit where remaining budget can still fill remaining
       positions.

Complexity:
    Time:  O(target * 9) for DP + O(max_digits * 9) for reconstruction
    Space: O(target) for DP array
"""

from typing import List


class Solution:
    def largestNumber(self, cost: List[int], target: int) -> str:
        # dp[t] = max number of digits with exactly budget t
        dp = [-1] * (target + 1)
        dp[0] = 0

        for t in range(1, target + 1):
            for d in range(9):
                c = cost[d]
                if c <= t and dp[t - c] >= 0:
                    dp[t] = max(dp[t], dp[t - c] + 1)

        if dp[target] <= 0:
            return "0"

        # Reconstruct greedily
        result = []
        remaining = target
        for _ in range(dp[target]):
            for d in range(8, -1, -1):  # try 9 down to 1
                c = cost[d]
                if c <= remaining and dp[remaining - c] == dp[remaining] - 1:
                    result.append(str(d + 1))
                    remaining -= c
                    break

        return ''.join(result)


# ---------- tests ----------
def run_tests():
    sol = Solution()

    # Test 1
    assert sol.largestNumber([4, 3, 2, 5, 6, 7, 2, 5, 5], 9) == "7772", \
        f"Test 1 failed: {sol.largestNumber([4, 3, 2, 5, 6, 7, 2, 5, 5], 9)}"

    # Test 2
    assert sol.largestNumber([7, 6, 5, 5, 5, 6, 8, 7, 8], 12) == "85", \
        f"Test 2 failed: {sol.largestNumber([7, 6, 5, 5, 5, 6, 8, 7, 8], 12)}"

    # Test 3: all costs even, target odd -> impossible
    assert sol.largestNumber([2, 4, 6, 2, 4, 6, 4, 4, 4], 5) == "0", \
        f"Test 3 failed: {sol.largestNumber([2, 4, 6, 2, 4, 6, 4, 4, 4], 5)}"

    # Test 4
    assert sol.largestNumber([1, 1, 1, 1, 1, 1, 1, 1, 1], 3) == "999", \
        f"Test 4 failed"

    # Test 5: impossible
    assert sol.largestNumber([2, 4, 6, 8, 10, 12, 14, 16, 18], 1) == "0", \
        f"Test 5 failed"

    print("All tests passed for 1449. Form Largest Integer With Digits That Add up to Target!")


if __name__ == "__main__":
    run_tests()
