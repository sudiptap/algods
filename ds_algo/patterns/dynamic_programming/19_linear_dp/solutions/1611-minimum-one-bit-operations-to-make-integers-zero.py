"""
1611. Minimum One Bit Operations to Make Integers Zero
https://leetcode.com/problems/minimum-one-bit-operations-to-make-integers-zero/

Pattern: 19 - Linear DP

---
APPROACH: Gray code / recursion
- To turn off the highest bit (bit k) of n, we need 2^(k+1) - 1 operations.
- But some lower bits may already be set, saving or costing operations.
- Key relation: f(n) = f(n ^ (n >> 1))... actually simpler:
  f(n) = n ^ f(n >> 1) -- this is the Gray code inverse.
- Alternatively: if highest bit is at position k,
  f(n) = (2^(k+1) - 1) - f(n ^ (1 << k))
  because to clear bit k, we need 2^(k+1)-1 ops minus what we already have below.

Time: O(log n)
Space: O(log n) recursion depth
---
"""


class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        # Gray code inverse approach
        # f(n) = n ^ n>>1 ^ n>>2 ^ ... until 0
        result = 0
        while n:
            result ^= n
            n >>= 1
        return result


# --- Tests ---
def test():
    sol = Solution()

    assert sol.minimumOneBitOperations(3) == 2
    assert sol.minimumOneBitOperations(6) == 4
    assert sol.minimumOneBitOperations(0) == 0
    assert sol.minimumOneBitOperations(1) == 1
    assert sol.minimumOneBitOperations(2) == 3  # 2->3->1->0
    assert sol.minimumOneBitOperations(9) == 14

    print("All tests passed!")


if __name__ == "__main__":
    test()
