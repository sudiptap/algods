"""
1553. Minimum Number of Days to Eat N Oranges
https://leetcode.com/problems/minimum-number-of-days-to-eat-n-oranges/

Pattern: 19 - Linear DP

---
APPROACH: Memoized DFS (BFS-like recursion)
- At each step: eat 1 orange (n-1), or if n%2==0 eat n/2, or if n%3==0 eat 2n/3.
- Key insight: always optimal to reduce to nearest multiple of 2 or 3 first
  (eat n%2 or n%3 oranges one-by-one), then divide.
- So: dp(n) = 1 + min(n%2 + dp(n//2), n%3 + dp(n//3))
- This reduces search space to O(log^2 n) states.

Time: O(log^2 n) - each call reduces n to n//2 or n//3
Space: O(log^2 n) for memoization
---
"""

from functools import lru_cache


class Solution:
    def minDays(self, n: int) -> int:
        @lru_cache(maxsize=None)
        def dp(n):
            if n <= 1:
                return n
            # Reduce to multiple of 2 or 3, then divide
            return 1 + min(
                n % 2 + dp(n // 2),
                n % 3 + dp(n // 3)
            )
        return dp(n)


# --- Tests ---
def test():
    sol = Solution()

    assert sol.minDays(10) == 4   # 10->9->3->1->0
    assert sol.minDays(6) == 3    # 6->3->1->0
    assert sol.minDays(1) == 1
    assert sol.minDays(56) == 6
    assert sol.minDays(0) == 0
    assert sol.minDays(2) == 2    # 2->1->0
    assert sol.minDays(3) == 2    # 3->1->0

    # Large input
    assert sol.minDays(10**9) > 0  # Just check it runs fast

    print("All tests passed!")


if __name__ == "__main__":
    test()
