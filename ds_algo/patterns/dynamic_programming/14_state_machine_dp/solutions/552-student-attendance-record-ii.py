"""
552. Student Attendance Record II (Hard)
https://leetcode.com/problems/student-attendance-record-ii/

An attendance record is a string of length n containing only 'A' (absent),
'L' (late), or 'P' (present). A student is eligible for an award if:
  - Total absences < 2, AND
  - Never has 3 or more consecutive lates.

Given n, return the number of valid records of length n, modulo 10^9 + 7.

Pattern: State Machine DP
- 6 states = (absences: 0 or 1) x (trailing consecutive lates: 0, 1, or 2).
- State (a, l):
    - Append 'P' -> (a, 0)
    - Append 'L' -> (a, l+1) if l+1 < 3
    - Append 'A' -> (a+1, 0) if a+1 < 2
- dp[a][l] = number of valid records ending in state (a, l).
- Base case: dp[0][0] = 1 (empty record).
- Iterate n steps; answer = sum of all 6 states.

Time:  O(n)   — 6 states, constant transitions per step
Space: O(1)   — only 6 values needed
"""

MOD = 10**9 + 7


class Solution:
    def checkRecord(self, n: int) -> int:
        """Return the number of valid attendance records of length n, mod 10^9+7.

        Args:
            n: Length of attendance record, 1 <= n <= 10^5.

        Returns:
            Count of valid records modulo 10^9 + 7.
        """
        # dp[a][l] where a in {0,1}, l in {0,1,2}
        # Initialize: one empty record in state (0, 0)
        dp = [[0, 0, 0], [0, 0, 0]]
        dp[0][0] = 1

        for _ in range(n):
            new = [[0, 0, 0], [0, 0, 0]]
            for a in range(2):
                for l in range(3):
                    if dp[a][l] == 0:
                        continue
                    val = dp[a][l]
                    # Append 'P': reset trailing lates to 0
                    new[a][0] = (new[a][0] + val) % MOD
                    # Append 'L': increment trailing lates if < 3
                    if l + 1 < 3:
                        new[a][l + 1] = (new[a][l + 1] + val) % MOD
                    # Append 'A': increment absences if < 2, reset lates
                    if a + 1 < 2:
                        new[a + 1][0] = (new[a + 1][0] + val) % MOD
            dp = new

        total = 0
        for a in range(2):
            for l in range(3):
                total = (total + dp[a][l]) % MOD
        return total


# ---------- tests ----------
def test_student_attendance_record_ii():
    sol = Solution()

    # n=1: P, L, A -> 3
    assert sol.checkRecord(1) == 3

    # n=2: 8 valid records
    assert sol.checkRecord(2) == 8

    # n=3: known result is 19
    assert sol.checkRecord(3) == 19

    # n=10: known result
    assert sol.checkRecord(10) == 3536

    # n=10101: known result
    assert sol.checkRecord(10101) == 183236316

    # Large: n=100000 (should complete quickly)
    result = sol.checkRecord(100000)
    assert 0 <= result < MOD

    print("All tests passed for 552. Student Attendance Record II")


if __name__ == "__main__":
    test_student_attendance_record_ii()
