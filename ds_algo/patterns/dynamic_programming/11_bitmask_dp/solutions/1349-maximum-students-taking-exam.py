"""
1349. Maximum Students Taking Exam (Hard)
https://leetcode.com/problems/maximum-students-taking-exam/

Problem:
    Given an m x n matrix of seats ('.' = good, '#' = broken), place
    students such that no student can see another's answer. A student can
    see the upper-left, upper-right, left, and right seats. Maximize the
    number of students seated.

Pattern: 11 - Bitmask DP

Approach:
    1. For each row, enumerate all valid bitmasks of seated students:
       - No two adjacent students in the same row (no left/right cheating).
       - Students only sit on good seats (mask & available == mask).
    2. dp[row][mask] = max students from row 0..row with mask configuration
       in current row.
    3. Transition: check compatibility with previous row's mask (no diagonal
       cheating: prev_mask shifted left/right must not overlap with cur_mask).

Complexity:
    Time:  O(m * 4^n) where m = rows, n = cols (2^n masks x 2^n prev masks)
    Space: O(m * 2^n) for the DP table
"""

from typing import List


class Solution:
    def maxStudents(self, seats: List[List[str]]) -> int:
        m, n = len(seats), len(seats[0])

        # Precompute available seats as bitmask per row
        avail = []
        for i in range(m):
            mask = 0
            for j in range(n):
                if seats[i][j] == '.':
                    mask |= (1 << j)
            avail.append(mask)

        def valid(mask: int, row: int) -> bool:
            # Must sit on available seats
            if mask & avail[row] != mask:
                return False
            # No two adjacent in same row
            if mask & (mask >> 1):
                return False
            return True

        def popcount(x: int) -> int:
            return bin(x).count('1')

        # dp[mask] = max students with this mask in the current row
        prev_dp = {}

        # First row
        for mask in range(1 << n):
            if valid(mask, 0):
                prev_dp[mask] = popcount(mask)

        for row in range(1, m):
            cur_dp = {}
            for mask in range(1 << n):
                if not valid(mask, row):
                    continue
                best = 0
                for prev_mask, prev_val in prev_dp.items():
                    # Check no diagonal cheating
                    if (prev_mask >> 1) & mask:
                        continue
                    if (prev_mask << 1) & mask:
                        continue
                    best = max(best, prev_val)
                cur_dp[mask] = best + popcount(mask)
            prev_dp = cur_dp

        return max(prev_dp.values()) if prev_dp else 0


# ---------- tests ----------
def run_tests():
    sol = Solution()

    # Test 1
    seats = [["#", ".", "#", "#", ".", "#"],
             [".", "#", "#", "#", "#", "."],
             ["#", ".", "#", "#", ".", "#"]]
    assert sol.maxStudents(seats) == 4, f"Test 1 failed: {sol.maxStudents(seats)}"

    # Test 2
    seats = [[".", "#"],
             ["#", "#"],
             ["#", "."],
             ["#", "#"],
             [".", "#"]]
    assert sol.maxStudents(seats) == 3, f"Test 2 failed: {sol.maxStudents(seats)}"

    # Test 3
    seats = [["#", ".", ".", ".", "#"],
             [".", "#", ".", "#", "."],
             [".", ".", "#", ".", "."],
             [".", "#", ".", "#", "."],
             ["#", ".", ".", ".", "#"]]
    assert sol.maxStudents(seats) == 10, f"Test 3 failed: {sol.maxStudents(seats)}"

    # Test 4: all broken
    seats = [["#", "#"], ["#", "#"]]
    assert sol.maxStudents(seats) == 0, "Test 4 failed"

    # Test 5: single seat
    seats = [["."]]
    assert sol.maxStudents(seats) == 1, "Test 5 failed"

    print("All tests passed for 1349. Maximum Students Taking Exam!")


if __name__ == "__main__":
    run_tests()
