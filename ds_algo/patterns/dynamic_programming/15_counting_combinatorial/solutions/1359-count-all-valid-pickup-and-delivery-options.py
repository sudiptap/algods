"""
1359. Count All Valid Pickup and Delivery Options (Hard)
https://leetcode.com/problems/count-all-valid-pickup-and-delivery-options/

Problem:
    Given n orders, each with a pickup (Pi) and delivery (Di), count all
    valid sequences where Pi always comes before Di for each order i.

Pattern: 15 - Counting / Combinatorial

Approach:
    1. Build up from 1 order to n orders.
    2. For k orders already placed (2k slots), adding the (k+1)-th order:
       - We have 2k+1 gaps. Choose where to place P_{k+1} and D_{k+1}.
       - Place P first: (2k+1) choices. Then D goes after P: can be in any
         of the remaining positions after P. This gives (2k+1) * (2k+2)/2
         valid placements, but simpler: dp[n] = dp[n-1] * (2n-1) * n.
    3. Alternatively: (2n)! / 2^n since for each pair the delivery must
       come after pickup (halving choices for each pair).

Complexity:
    Time:  O(n)
    Space: O(1)
"""

MOD = 10**9 + 7


class Solution:
    def countOrders(self, n: int) -> int:
        result = 1
        for i in range(2, n + 1):
            # Insert P_i into 2(i-1)+1 = 2i-1 positions
            # For each, D_i can go in any of the positions after P_i
            # Number of ways = (2i-1) * i  ... wait let me reconsider.
            # With i-1 orders placed (2(i-1) slots), adding order i:
            # Total slots now = 2(i-1)+1 = 2i-1 gaps for P_i.
            # After placing P_i, there are 2(i-1)+1 = 2i slots,
            # and D_i can go in any of the slots at or after P_i's position.
            # Average # of slots after P = (2i-1+1)/2 = i.
            # So total ways = (2i-1) * i.
            # But more directly: we have 2i positions to fill for P_i and D_i.
            # Choose 2 of 2i positions: C(2i, 2) but then P must come first: C(2i,2)/1.
            # Wait, that's just (2i choose 2) = (2i)(2i-1)/2.
            # But we're inserting into 2(i-1) existing items, so we have 2i slots total.
            # Actually: spaces = 2(i-1)+1 for first, then 2(i-1)+2 for second.
            # Pairs where P before D = (2i-1)*2i/2 = (2i-1)*i.
            result = result * (2 * i - 1) * i % MOD
        return result


# ---------- tests ----------
def run_tests():
    sol = Solution()

    # Test 1: n=1 -> P1D1 -> 1
    assert sol.countOrders(1) == 1, "Test 1 failed"

    # Test 2: n=2 -> 6
    assert sol.countOrders(2) == 6, f"Test 2 failed: {sol.countOrders(2)}"

    # Test 3: n=3 -> 90
    assert sol.countOrders(3) == 90, f"Test 3 failed: {sol.countOrders(3)}"

    # Test 4: large n
    assert sol.countOrders(500) > 0, "Test 4 failed"

    # Test 5: n=4 -> 2520
    assert sol.countOrders(4) == 2520, f"Test 5 failed: {sol.countOrders(4)}"

    print("All tests passed for 1359. Count All Valid Pickup and Delivery Options!")


if __name__ == "__main__":
    run_tests()
