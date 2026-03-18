"""
638. Shopping Offers (Medium)
https://leetcode.com/problems/shopping-offers/

In LeetCode Store, there are n items to buy. Each item has a price.
You are also given a set of special offers (bundles). Each offer specifies
the quantity of each item you get plus the bundle price.

You need to buy exactly needs[i] of each item i. Return the lowest price.

Approach - DFS with Memoization:
    For each state (remaining needs as a tuple), try:
      1. Every valid special offer (doesn't exceed remaining needs).
      2. Buying everything individually (base case comparison).
    Memoize on the needs tuple to avoid recomputation.

Time:  O(n * k * m^n) where k = number of offers, m = max need, n = items
       In practice much smaller due to memoization and pruning.
Space: O(m^n) for the memoization table.
"""

from typing import List
from functools import lru_cache


class Solution:
    def shoppingOffers(
        self, price: List[int], special: List[List[int]], needs: List[int]
    ) -> int:
        """Return the minimum cost to buy exactly the required items.

        Uses DFS with memoization. At each state, try all valid offers
        and compare against buying items individually.

        Args:
            price:   price[i] is the price of item i.
            special: each offer is [qty_0, qty_1, ..., qty_n-1, bundle_price].
            needs:   needs[i] is the required quantity of item i.

        Returns:
            Minimum cost to fulfill all needs.
        """
        n = len(price)

        # Filter out offers that cost more than buying items individually
        valid_special = []
        for offer in special:
            individual_cost = sum(offer[i] * price[i] for i in range(n))
            if offer[-1] < individual_cost:
                valid_special.append(offer)

        @lru_cache(maxsize=None)
        def dfs(remaining: tuple) -> int:
            # Base: cost of buying everything individually
            min_cost = sum(remaining[i] * price[i] for i in range(n))

            for offer in valid_special:
                # Check if this offer is applicable (doesn't exceed needs)
                new_remaining = []
                valid = True
                for i in range(n):
                    if remaining[i] < offer[i]:
                        valid = False
                        break
                    new_remaining.append(remaining[i] - offer[i])

                if valid:
                    min_cost = min(min_cost, offer[-1] + dfs(tuple(new_remaining)))

            return min_cost

        return dfs(tuple(needs))


# --- Tests ---

def test_example1():
    sol = Solution()
    assert sol.shoppingOffers([2, 5], [[3, 0, 5], [1, 2, 10]], [3, 2]) == 14

def test_example2():
    sol = Solution()
    assert sol.shoppingOffers([2, 3, 4], [[1, 1, 0, 4], [2, 2, 1, 9]], [1, 2, 1]) == 11

def test_no_offers():
    sol = Solution()
    assert sol.shoppingOffers([1, 2, 3], [], [1, 1, 1]) == 6

def test_offer_not_worth_it():
    sol = Solution()
    # Offer costs more than buying individually, should be ignored
    assert sol.shoppingOffers([1, 1], [[1, 1, 10]], [2, 2]) == 4

def test_single_item():
    sol = Solution()
    assert sol.shoppingOffers([5], [[2, 8]], [4]) == 16

def test_zero_needs():
    sol = Solution()
    assert sol.shoppingOffers([2, 3], [[1, 1, 3]], [0, 0]) == 0


if __name__ == "__main__":
    test_example1()
    test_example2()
    test_no_offers()
    test_offer_not_worth_it()
    test_single_item()
    test_zero_needs()
    print("All tests passed!")
