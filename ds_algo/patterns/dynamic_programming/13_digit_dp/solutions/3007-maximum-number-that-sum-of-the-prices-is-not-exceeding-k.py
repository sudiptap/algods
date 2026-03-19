"""
3007. Maximum Number That Sum of the Prices Is Not Exceeding K

Pattern: Digit DP
Approach: Binary search on the answer. For a given number n, compute the total
    "price" of all numbers 1..n. Price of a number = count of set bits at positions
    that are multiples of x. Use digit DP / bit counting to compute total price
    for range [1, n] efficiently.
Time Complexity: O(log^2(answer) * 64)
Space Complexity: O(1)
"""

def findMaximumNumber(k, x):
    def total_price(n):
        """Sum of prices of all numbers from 1 to n."""
        if n <= 0:
            return 0
        total = 0
        # For each bit position that is a multiple of x (1-indexed from LSB)
        # Count how many numbers in [1, n] have that bit set
        for bit in range(x - 1, 64, x):  # 0-indexed bit positions: x-1, 2x-1, ...
            # Count numbers in [0, n] with bit 'bit' set
            cycle = 1 << (bit + 1)
            full_cycles = (n + 1) // cycle
            remainder = (n + 1) % cycle
            count = full_cycles * (1 << bit) + max(0, remainder - (1 << bit))
            total += count
        return total

    lo, hi = 1, 10**15
    while lo < hi:
        mid = (lo + hi + 1) // 2
        if total_price(mid) <= k:
            lo = mid
        else:
            hi = mid - 1

    return lo


def test():
    assert findMaximumNumber(9, 1) == 6
    assert findMaximumNumber(7, 2) == 9
    print("All tests passed!")

test()
