"""
1227. Airplane Seat Assignment Probability (Medium)

Pattern: 15_counting_combinatorial
- Probability that the n-th person gets their own seat when person 1 picks randomly.

Approach:
- Mathematical insight: for n >= 2, the answer is always 0.5.
- Intuition: the first person picks a random seat. If they pick their own, everyone
  is fine (probability 1/n). If they pick the last person's seat, the last person
  is displaced (probability 1/n). If they pick person k's seat, person k faces the
  same sub-problem. By induction/symmetry, the last person either gets seat 1 or
  seat n, each with equal probability.
- For n = 1: the answer is 1.0 (person 1 has only their own seat).

Complexity:
- Time:  O(1)
- Space: O(1)
"""


class Solution:
    def nthPersonGetsNthSeat(self, n: int) -> float:
        return 1.0 if n == 1 else 0.5


# ---------- Tests ----------
def test():
    sol = Solution()

    assert sol.nthPersonGetsNthSeat(1) == 1.0
    assert sol.nthPersonGetsNthSeat(2) == 0.5
    assert sol.nthPersonGetsNthSeat(3) == 0.5
    assert sol.nthPersonGetsNthSeat(100) == 0.5
    assert sol.nthPersonGetsNthSeat(1000) == 0.5

    print("All tests passed!")


if __name__ == "__main__":
    test()
