"""
1774. Closest Dessert Cost
https://leetcode.com/problems/closest-dessert-cost/

Pattern: 19 - Linear DP

---
APPROACH: DFS/backtracking trying all topping combinations
- Must choose exactly one base. Each topping can be used 0, 1, or 2 times.
- For each base, try all combinations of toppings using DFS.
- Track the closest cost to target (prefer lower cost on tie).
- Since n, m <= 10 and toppings at most 2 each, total combos = 3^10 = 59049 per base.

Time: O(n * 3^m) where n = bases, m = toppings
Space: O(m) recursion depth
---
"""

from typing import List


class Solution:
    def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
        self.best = float('inf')

        def dfs(idx, current):
            # Update best
            if (abs(current - target) < abs(self.best - target) or
                (abs(current - target) == abs(self.best - target) and current < self.best)):
                self.best = current

            if idx == len(toppingCosts):
                return
            if current > target:  # Pruning: adding more only goes further
                return

            # Try 0, 1, or 2 of this topping
            dfs(idx + 1, current)
            dfs(idx + 1, current + toppingCosts[idx])
            dfs(idx + 1, current + 2 * toppingCosts[idx])

        for base in baseCosts:
            dfs(0, base)

        return self.best


# --- Tests ---
def test():
    sol = Solution()

    assert sol.closestCost([1, 7], [3, 4], 10) == 10
    assert sol.closestCost([2, 3], [4, 5, 100], 18) == 17
    assert sol.closestCost([3, 10], [2, 5], 9) == 8
    assert sol.closestCost([10], [1], 1) == 10

    print("All tests passed!")


if __name__ == "__main__":
    test()
