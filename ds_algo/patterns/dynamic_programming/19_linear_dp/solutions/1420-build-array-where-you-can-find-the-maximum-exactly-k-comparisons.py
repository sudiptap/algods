"""
1420. Build Array Where You Can Find The Maximum Exactly K Comparisons (Hard)
https://leetcode.com/problems/build-array-where-you-can-find-the-maximum-exactly-k-comparisons/

Problem:
    Build an array of length n where each element is in [1, m]. The
    "search cost" is the number of times a new maximum is found when
    scanning left to right. Return the count of arrays with search cost
    exactly k, mod 10^9+7.

Pattern: 19 - Linear DP

Approach:
    1. dp[i][j][c] = number of arrays of length i where max so far is j
       and search cost is c.
    2. Transition: for the (i+1)-th element:
       - If we place a value <= j: j choices, cost stays c.
       - If we place a value v > j: v becomes new max, cost becomes c+1.
    3. Base: dp[1][j][1] = 1 for all j in [1, m].
    4. Use prefix sums to optimize the "place value > j" transition.

Complexity:
    Time:  O(n * m * k) with prefix sum optimization
    Space: O(n * m * k), reducible to O(m * k)
"""

MOD = 10**9 + 7


class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        # dp[j][c] = ways to build array of current length with max=j and cost=c
        dp = [[0] * (k + 1) for _ in range(m + 1)]

        # Base: length 1
        for j in range(1, m + 1):
            if k >= 1:
                dp[j][1] = 1

        for i in range(2, n + 1):
            ndp = [[0] * (k + 1) for _ in range(m + 1)]
            # Prefix sum of dp[1..j][c] over j for the "new max" transition
            for c in range(1, k + 1):
                prefix = 0
                for j in range(1, m + 1):
                    # Place value <= j: j choices, max stays j, cost stays c
                    ndp[j][c] = (ndp[j][c] + dp[j][c] * j) % MOD
                    # Place value = j as new max: previous max was some v < j, cost was c-1
                    # This is sum of dp[v][c-1] for v in [1, j-1]
                    ndp[j][c] = (ndp[j][c] + prefix) % MOD
                    prefix = (prefix + dp[j][c - 1]) % MOD
            dp = ndp

        result = 0
        for j in range(1, m + 1):
            result = (result + dp[j][k]) % MOD
        return result


# ---------- tests ----------
def run_tests():
    sol = Solution()

    # Test 1
    assert sol.numOfArrays(2, 3, 1) == 6, f"Test 1 failed: {sol.numOfArrays(2, 3, 1)}"

    # Test 2
    assert sol.numOfArrays(5, 2, 3) == 0, f"Test 2 failed: {sol.numOfArrays(5, 2, 3)}"

    # Test 3
    assert sol.numOfArrays(9, 1, 1) == 1, f"Test 3 failed: {sol.numOfArrays(9, 1, 1)}"

    # Test 4
    assert sol.numOfArrays(50, 100, 25) == 34549172, f"Test 4 failed: {sol.numOfArrays(50, 100, 25)}"

    # Test 5
    assert sol.numOfArrays(2, 3, 2) == 3, f"Test 5 failed: {sol.numOfArrays(2, 3, 2)}"

    print("All tests passed for 1420. Build Array Where You Can Find The Maximum Exactly K Comparisons!")


if __name__ == "__main__":
    run_tests()
