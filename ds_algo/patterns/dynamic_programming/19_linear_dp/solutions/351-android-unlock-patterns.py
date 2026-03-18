"""
351. Android Unlock Patterns (Medium)

Given an Android 3x3 key lock screen and two integers m and n,
count the total number of unlock patterns of length between m and n
(inclusive) where each pattern must connect at least m keys and at most
n keys.

Rules:
- Each pattern must connect at least m keys and at most n keys.
- All keys must be distinct.
- If the line connecting two consecutive keys passes through any other
  keys, the other keys must have been previously selected.
  E.g., 1 -> 3 is valid only if 2 was already selected.

Approach:
- DFS/backtracking with a visited set.
- Precompute "skip" table: skip[i][j] = the key that must be visited
  before going from i to j (0 if no skip needed).
- Exploit symmetry: patterns starting from corners (1,3,7,9) are
  equivalent, and patterns starting from edges (2,4,6,8) are equivalent.
  Only need to compute for 1, 2, and 5, then multiply.

Time:  O(n!) in the worst case, but the search space is small (9 keys).
Space: O(n) for recursion depth.
"""

from typing import List


class Solution:
    def numberOfPatterns(self, m: int, n: int) -> int:
        """Count valid unlock patterns of length between m and n."""
        # skip[i][j] = key that must be visited before going from i to j
        # 0 means no intermediate key is needed
        skip = [[0] * 10 for _ in range(10)]
        skip[1][3] = skip[3][1] = 2
        skip[1][7] = skip[7][1] = 4
        skip[3][9] = skip[9][3] = 6
        skip[7][9] = skip[9][7] = 8
        skip[1][9] = skip[9][1] = 5
        skip[3][7] = skip[7][3] = 5
        skip[2][8] = skip[8][2] = 5
        skip[4][6] = skip[6][4] = 5

        visited = [False] * 10

        def dfs(cur: int, remaining: int) -> int:
            """Count patterns from cur with 'remaining' more keys to pick."""
            if remaining == 0:
                return 1
            visited[cur] = True
            count = 0
            for nxt in range(1, 10):
                mid = skip[cur][nxt]
                # nxt must be unvisited; if there's a skip key, it must be visited
                if not visited[nxt] and (mid == 0 or visited[mid]):
                    count += dfs(nxt, remaining - 1)
            visited[cur] = False
            return count

        total = 0
        for length in range(m, n + 1):
            # Corner keys (1,3,7,9): 4 symmetric starts
            total += dfs(1, length - 1) * 4
            # Edge keys (2,4,6,8): 4 symmetric starts
            total += dfs(2, length - 1) * 4
            # Center key (5): 1 start
            total += dfs(5, length - 1)
        return total


# ---------- Tests ----------

def test_single_key():
    sol = Solution()
    # Patterns of length 1: each of the 9 keys alone
    assert sol.numberOfPatterns(1, 1) == 9

def test_m1_n1():
    sol = Solution()
    assert sol.numberOfPatterns(1, 1) == 9

def test_m1_n2():
    sol = Solution()
    # Length 1: 9, Length 2: 56
    assert sol.numberOfPatterns(1, 2) == 65

def test_m1_n3():
    sol = Solution()
    assert sol.numberOfPatterns(1, 3) == 385

def test_full_range():
    sol = Solution()
    # Total patterns of all lengths 1-9
    assert sol.numberOfPatterns(1, 9) == 389497

def test_length_2():
    sol = Solution()
    assert sol.numberOfPatterns(2, 2) == 56

def test_length_3():
    sol = Solution()
    assert sol.numberOfPatterns(3, 3) == 320

def test_length_9():
    sol = Solution()
    # Full 9-key patterns
    assert sol.numberOfPatterns(9, 9) == 140704


if __name__ == "__main__":
    test_single_key()
    test_m1_n1()
    test_m1_n2()
    test_m1_n3()
    test_full_range()
    test_length_2()
    test_length_3()
    test_length_9()
    print("All tests passed!")
