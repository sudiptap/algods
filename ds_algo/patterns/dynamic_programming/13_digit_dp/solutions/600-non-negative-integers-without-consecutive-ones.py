"""
600. Non-negative Integers without Consecutive Ones
https://leetcode.com/problems/non-negative-integers-without-consecutive-ones/

Pattern: 13 - Digit DP

---
APPROACH: Digit DP on binary representation
- Convert n to binary. Process bits from the most significant bit downward.
- Track two states: whether the previous bit was 1, and whether we are still
  tight (i.e., constrained by n's bits).
- If previous bit was 1 and current bit is also 1 under tight constraint,
  we can't place 1 here AND all numbers with 0 at this position (still tight)
  have already been counted, so we stop.
- Use Fibonacci-like counts: f[k] = count of valid binary strings of length k
  (no consecutive 1s). f[k] = f[k-1] + f[k-2].

Time: O(log n)   Space: O(log n)
---
"""


class Solution:
    def findIntegers(self, n: int) -> int:
        """Return the count of non-negative integers <= n without consecutive ones in binary."""
        # Get binary representation (without '0b' prefix)
        bits = bin(n)[2:]
        length = len(bits)

        # Precompute Fibonacci: fib[k] = number of valid binary strings of length k
        # (no consecutive 1s), including leading zeros.
        # fib[1] = 2 ("0","1"), fib[2] = 3 ("00","01","10"), etc.
        fib = [0] * (length + 1)
        fib[0] = 1  # empty string
        fib[1] = 2
        for i in range(2, length + 1):
            fib[i] = fib[i - 1] + fib[i - 2]

        result = 0
        prev_bit = 0

        for i in range(length):
            if bits[i] == '1':
                # Count all valid numbers with 0 at position i (remaining bits free)
                remaining = length - i - 1
                result += fib[remaining]

                # If previous bit was also 1, we've hit consecutive ones —
                # all valid numbers have already been counted above.
                if prev_bit == 1:
                    break
                prev_bit = 1
            else:
                prev_bit = 0
        else:
            # Loop completed without break — n itself has no consecutive ones,
            # so include it in the count.
            result += 1

        return result


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.findIntegers(5) == 5    # 0,1,2,4,5 — skip 3 (11)
    assert sol.findIntegers(1) == 2    # 0, 1
    assert sol.findIntegers(2) == 3    # 0, 1, 2
    assert sol.findIntegers(3) == 3    # 0, 1, 2  (3=11 has consecutive ones)
    assert sol.findIntegers(10) == 8   # 0,1,2,4,5,8,9,10
    assert sol.findIntegers(0) == 1    # just 0
    assert sol.findIntegers(1000000000) == 2178309

    print("all tests passed")
