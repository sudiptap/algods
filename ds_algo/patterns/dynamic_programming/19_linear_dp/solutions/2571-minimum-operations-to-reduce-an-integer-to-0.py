"""
2571. Minimum Operations to Reduce an Integer to 0
https://leetcode.com/problems/minimum-operations-to-reduce-an-integer-to-0/

Pattern: 19 - Linear DP (Greedy on binary representation)

---
APPROACH: Greedy on consecutive 1-bits
- We can add or subtract powers of 2.
- For a single 1-bit: one operation (subtract that power of 2).
- For consecutive 1-bits (e.g., 0111 = 7): better to add 1 (making 1000) then
  subtract (2 ops vs 3). So consecutive run of >= 2 ones: add to make single bit.
- Process bits from low to high: if single 1, subtract (1 op). If consecutive 1s,
  add (carry, 1 op) and continue.

Time: O(log n)  Space: O(1)
---
"""


class Solution:
    def minOperations(self, n: int) -> int:
        ops = 0
        while n:
            # Check lowest set bit and if there are consecutive 1s
            if n & 1:
                # Check if next bit is also 1 (consecutive)
                if n & 2:
                    # Add 1 to clear consecutive 1s
                    n += 1
                    ops += 1
                else:
                    # Single 1 bit, subtract
                    n -= 1
                    ops += 1
            else:
                n >>= 1

        return ops


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.minOperations(39) == 3
    assert sol.minOperations(54) == 3
    assert sol.minOperations(1) == 1
    assert sol.minOperations(2) == 1
    assert sol.minOperations(3) == 2

    print("all tests passed")
