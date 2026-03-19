"""
1387. Sort Integers by The Power Value (Medium)
https://leetcode.com/problems/sort-integers-by-the-power-value/

Problem:
    The power of an integer x is the number of steps to reduce it to 1
    using the Collatz sequence (if even, x/2; if odd, 3x+1). Sort
    integers in [lo, hi] by their power value, return the k-th integer.

Pattern: 19 - Linear DP

Approach:
    1. Memoize the Collatz sequence length for each number.
    2. Compute power for all integers in [lo, hi].
    3. Sort by (power, value) and return the k-th element.

Complexity:
    Time:  O(n * C + n log n) where n = hi - lo + 1, C = avg Collatz length
    Space: O(n + M) where M = memoization cache size
"""


class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        memo = {1: 0}

        def power(x: int) -> int:
            if x in memo:
                return memo[x]
            if x % 2 == 0:
                memo[x] = 1 + power(x // 2)
            else:
                memo[x] = 1 + power(3 * x + 1)
            return memo[x]

        nums = list(range(lo, hi + 1))
        nums.sort(key=lambda x: (power(x), x))
        return nums[k - 1]


# ---------- tests ----------
def run_tests():
    sol = Solution()

    # Test 1
    assert sol.getKth(12, 15, 2) == 13, f"Test 1 failed: {sol.getKth(12, 15, 2)}"

    # Test 2
    assert sol.getKth(1, 1, 1) == 1, "Test 2 failed"

    # Test 3
    assert sol.getKth(7, 11, 4) == 7, f"Test 3 failed: {sol.getKth(7, 11, 4)}"

    # Test 4
    assert sol.getKth(10, 20, 5) == 13, f"Test 4 failed: {sol.getKth(10, 20, 5)}"

    # Test 5
    assert sol.getKth(1, 1000, 777) == 570, f"Test 5 failed: {sol.getKth(1, 1000, 777)}"

    print("All tests passed for 1387. Sort Integers by The Power Value!")


if __name__ == "__main__":
    run_tests()
