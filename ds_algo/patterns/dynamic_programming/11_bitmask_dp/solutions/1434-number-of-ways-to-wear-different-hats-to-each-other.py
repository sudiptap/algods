"""
1434. Number of Ways to Wear Different Hats to Each Other (Hard)
https://leetcode.com/problems/number-of-ways-to-wear-different-hats-to-each-other/

Problem:
    There are n people and 40 types of hats. Each person has a list of
    preferred hats. Assign exactly one hat to each person such that each
    person wears a different hat. Count the number of ways.

Pattern: 11 - Bitmask DP

Approach:
    1. Since n <= 10 but hats <= 40, bitmask over people (not hats).
    2. Invert: for each hat, list which people can wear it.
    3. dp[mask] = number of ways to assign hats to the set of people in mask.
    4. Iterate over hats 1..40. For each hat, either skip it or assign it
       to an unassigned person who likes it.
    5. Final answer: dp[(1 << n) - 1].

Complexity:
    Time:  O(40 * 2^n * n) where n <= 10
    Space: O(2^n) for DP table
"""

from typing import List

MOD = 10**9 + 7


class Solution:
    def numberWays(self, hats: List[List[int]]) -> int:
        n = len(hats)
        full = (1 << n) - 1

        # hat_to_people: for each hat, which people can wear it
        hat_to_people = [[] for _ in range(41)]
        for person in range(n):
            for h in hats[person]:
                hat_to_people[h].append(person)

        dp = [0] * (full + 1)
        dp[0] = 1

        for hat in range(1, 41):
            # Process in reverse to avoid using same hat twice
            ndp = dp[:]
            for person in hat_to_people[hat]:
                bit = 1 << person
                for mask in range(full + 1):
                    if mask & bit:
                        continue  # person already assigned
                    ndp[mask | bit] = (ndp[mask | bit] + dp[mask]) % MOD
            dp = ndp

        return dp[full]


# ---------- tests ----------
def run_tests():
    sol = Solution()

    # Test 1
    assert sol.numberWays([[3, 4], [4, 5], [5]]) == 1, \
        f"Test 1 failed: {sol.numberWays([[3, 4], [4, 5], [5]])}"

    # Test 2
    assert sol.numberWays([[3, 5, 1], [3, 5]]) == 4, \
        f"Test 2 failed: {sol.numberWays([[3, 5, 1], [3, 5]])}"

    # Test 3
    assert sol.numberWays([[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]]) == 24, \
        f"Test 3 failed: {sol.numberWays([[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]])}"

    # Test 4: single person
    assert sol.numberWays([[1, 2, 3]]) == 3, "Test 4 failed"

    # Test 5: impossible
    assert sol.numberWays([[1], [1]]) == 0, "Test 5 failed"

    print("All tests passed for 1434. Number of Ways to Wear Different Hats to Each Other!")


if __name__ == "__main__":
    run_tests()
