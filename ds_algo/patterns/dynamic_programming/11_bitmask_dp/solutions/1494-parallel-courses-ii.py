"""
1494. Parallel Courses II (Hard)

Pattern: Bitmask DP (11)
Approach:
    Represent the set of completed courses as a bitmask.
    dp[mask] = minimum number of semesters to complete courses in mask.

    For each state 'mask':
        1. Find 'available' courses: prerequisites fully met by mask and not yet taken.
        2. Enumerate all subsets of 'available' of size <= k.
        3. For each valid subset 'sub': dp[mask | sub] = min(dp[mask | sub], dp[mask] + 1).

    Enumerating subsets of a bitmask efficiently: iterate sub = avail, then
    sub = (sub - 1) & avail until 0.

Complexity:
    Time:  O(3^n * n) in the worst case (subset enumeration)
    Space: O(2^n)
"""

from typing import List


class Solution:
    def minNumberOfSemesters(self, n: int, relations: List[List[int]], k: int) -> int:
        """Return minimum number of semesters to take all n courses."""
        # Build prerequisite mask for each course (0-indexed)
        prereq = [0] * n
        for u, v in relations:
            prereq[v - 1] |= 1 << (u - 1)

        full = (1 << n) - 1
        INF = float('inf')
        dp = [INF] * (full + 1)
        dp[0] = 0

        for mask in range(full):
            if dp[mask] == INF:
                continue

            # Find available courses: prereqs met and not yet taken
            avail = 0
            for i in range(n):
                if not (mask & (1 << i)) and (prereq[i] & mask) == prereq[i]:
                    avail |= 1 << i

            # If available courses <= k, take them all
            if bin(avail).count('1') <= k:
                dp[mask | avail] = min(dp[mask | avail], dp[mask] + 1)
            else:
                # Enumerate all subsets of avail
                sub = avail
                while sub:
                    if bin(sub).count('1') <= k:
                        dp[mask | sub] = min(dp[mask | sub], dp[mask] + 1)
                    sub = (sub - 1) & avail

        return dp[full]


# ---------- Tests ----------
import unittest


class TestParallelCoursesII(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        self.assertEqual(
            self.sol.minNumberOfSemesters(4, [[2, 1], [3, 1], [1, 4]], 2), 3
        )

    def test_example2(self):
        self.assertEqual(
            self.sol.minNumberOfSemesters(5, [[2, 1], [3, 1], [4, 1], [1, 5]], 2), 4
        )

    def test_no_relations(self):
        # No prerequisites, k=2, 4 courses -> ceil(4/2) = 2
        self.assertEqual(
            self.sol.minNumberOfSemesters(4, [], 2), 2
        )

    def test_single_course(self):
        self.assertEqual(
            self.sol.minNumberOfSemesters(1, [], 1), 1
        )

    def test_chain(self):
        # Linear chain: 1->2->3, k=2 -> 3 semesters (must take sequentially)
        self.assertEqual(
            self.sol.minNumberOfSemesters(3, [[1, 2], [2, 3]], 2), 3
        )

    def test_all_parallel(self):
        # 5 independent courses, k=3 -> ceil(5/3) = 2
        self.assertEqual(
            self.sol.minNumberOfSemesters(5, [], 3), 2
        )


if __name__ == "__main__":
    unittest.main()
