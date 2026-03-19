"""
3621. Number of Integers With Popcount-Depth Equal to K I
https://leetcode.com/problems/number-of-integers-with-popcount-depth-equal-to-k-i/

Pattern: 13 - Digit DP

---
APPROACH: Digit DP on binary representation
- "Popcount-depth" of a number: repeatedly take popcount until reaching 1.
  depth = number of steps to reach 1.
  E.g., 15 -> popcount(15)=4 -> popcount(4)=1, depth=2.
- Count numbers in [1, n] with popcount-depth exactly k.
- Use digit DP on binary digits of n.
- State: position, popcount so far, tight constraint, started.
- After getting the popcount, compute depth recursively (small numbers).

Time: O(log(n)^2 * log(log(n)))  Space: O(log(n)^2)
---
"""


class Solution:
    def countIntegers(self, n: int, k: int) -> int:
        if n <= 0:
            return 0

        def popcount_depth(x):
            """Compute depth: repeatedly take popcount until 1."""
            if x <= 0:
                return -1  # undefined
            depth = 0
            while x > 1:
                x = bin(x).count('1')
                depth += 1
            return depth

        # Digit DP on binary representation of n
        bits = bin(n)[2:]
        L = len(bits)
        from functools import lru_cache

        @lru_cache(maxsize=None)
        def dp(pos, popcount, tight, started):
            """Count numbers with popcount-depth == k."""
            if pos == L:
                if not started:
                    return 0
                # popcount is the popcount of the number.
                # If popcount == 1, the number is a power of 2.
                # If the number is 1, depth = 0. Otherwise depth = 1 + depth(popcount).
                # But we don't know if the number is 1 vs another power of 2.
                # We DO know: number is 1 iff popcount==1 and the number uses 1 bit total,
                # i.e., the number representation is just "1" in binary.
                # We can track this separately, but simpler: the number has L bits
                # (possibly with leading zeros absorbed). If popcount==1, depth=0 only
                # if number==1. Number==1 means all bits are 0 except the last.
                # Since we're counting with started flag, popcount=1 and started=True
                # means the number has exactly one 1-bit. It's 1 only if L-position=0
                # at that point, but we lose that info. Use a workaround:
                # just compute depth as 1 + popcount_depth(popcount) for popcount > 1,
                # and depth=1 for popcount==1 (covers powers of 2 >= 2).
                # Number 1 will have depth=1 here, but actual depth(1)=0.
                # We'll subtract 1 at the end if k==0 (for number 1) or add 1 if k==1.
                if popcount <= 1:
                    depth = popcount  # 0 if popcount=0 (shouldn't happen with started), 1 if popcount=1
                else:
                    depth = 1 + popcount_depth(popcount)
                return 1 if depth == k else 0

            limit = int(bits[pos]) if tight else 1
            result = 0
            for d in range(0, limit + 1):
                new_tight = tight and (d == limit)
                new_started = started or (d == 1)
                new_pop = (popcount + d) if started else (d if d == 1 else 0)
                result += dp(pos + 1, new_pop, new_tight, new_started)

            return result

        count = dp(0, 0, True, False)
        # Fix: number 1 has depth 0 but we counted it as depth 1.
        # Adjust: if k==0 and n>=1, add 1 (number 1). If k==1 and n>=1, subtract 1.
        if n >= 1:
            if k == 0:
                count += 1
            elif k == 1:
                count -= 1
        return count


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    # depth(1)=0, depth(2)=1(popcount=1), depth(3)=1(popcount=2->1)
    # depth(4)=1, depth(5)=2(popcount=2->1, wait 5=101,pc=2,depth(2)=1,so depth(5)=2)
    # No: depth(5): 5->popcount(5)=2->popcount(2)=1. Steps=2. depth=2.
    # depth(1)=0. depth(2)=1. depth(3): 3->2->1, depth=2.
    # Count in [1,10] with depth=1: {2,4,8} -> popcount is 1, depth=1. Also numbers
    # with popcount in {2,4,8,...} that have depth 1? No: depth=1 means popcount=1.
    # So numbers with exactly one 1-bit: 1,2,4,8 in [1,10]. But depth(1)=0.
    # So depth=1: {2,4,8}. Count=3.
    res = sol.countIntegers(10, 1)
    assert res == 3, f"Got {res}"

    # depth=0: only number 1
    res = sol.countIntegers(10, 0)
    assert res == 1, f"Got {res}"

    # depth=2: popcount maps to something with depth 1 (i.e., popcount is a power of 2 > 1)
    # depth(3)=2: 3->2->1. depth(5)=2: 5->2->1. depth(6)=2: 6->2->1.
    # depth(9)=2: 9->2->1. depth(10)=2: 10->2->1.
    # Also popcount=4: depth(4)=1->no. depth(popcount)=1 means popcount is power of 2.
    # So depth=2: numbers whose popcount is a power of 2 >= 2.
    # Popcount=2: 3,5,6,9,10 in [1,10]. Popcount=4: need 4 bits, min=15. Not in range.
    # So count = 5.
    res = sol.countIntegers(10, 2)
    assert res == 5, f"Got {res}"

    print("All tests passed!")
