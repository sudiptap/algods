"""
3747. Count Distinct Integers After Removing Zeros
https://leetcode.com/problems/count-distinct-integers-after-removing-zeros/

Pattern: 19 - Linear DP (Math/Digit DP)

---
APPROACH: Count zero-free integers in [1, n]
- For x in [1..n], removing zeros from x gives some integer y.
- Two different x values may map to the same y.
- But y is always a zero-free integer.
- Key insight: the distinct results are exactly the set of zero-free
  integers in [1, n'] where n' = remove_zeros(n).
  Wait, that's not quite right because e.g. x=203 -> y=23, and
  23 < 203, so 23 is already counted.
- Actually: the set of results is exactly the set of zero-free
  integers y such that there exists x in [1,n] with remove_zeros(x)=y.
- The smallest x mapping to y is y itself (if y has no zeros).
- So the answer = count of zero-free integers in [1, n].
  Because: every zero-free integer y <= n maps to itself.
  And any y from remove_zeros(x) where x <= n is also <= n
  (removing zeros can only decrease or maintain the number of digits).
  Wait, remove_zeros(10) = 1. Yes, result <= original.
  So the set of results is a subset of zero-free integers in [1, n].
  And every zero-free integer y in [1, n] is its own result.
  So the answer is exactly the count of zero-free integers in [1, n].

- Use digit DP to count integers in [1, n] with no zero digit.

Time: O(d^2) where d = number of digits  Space: O(d)
---
"""

from functools import lru_cache


class Solution:
    def countDistinctIntegers(self, n: int) -> int:
        s = str(n)
        L = len(s)

        @lru_cache(maxsize=None)
        def dp(pos, tight, started):
            if pos == L:
                return 1 if started else 0

            limit = int(s[pos]) if tight else 9
            count = 0

            for d in range(0, limit + 1):
                if d == 0:
                    if not started:
                        # Leading zero, skip
                        count += dp(pos + 1, tight and d == limit, False)
                    else:
                        # Zero digit in the middle - skip (not allowed)
                        pass
                else:
                    count += dp(pos + 1, tight and d == limit, True)

            return count

        result = dp(0, True, False)
        dp.cache_clear()
        return result


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.countDistinctIntegers(10) == 9   # 1-9 are zero-free, 10 maps to 1
    assert sol.countDistinctIntegers(3) == 3
    assert sol.countDistinctIntegers(1) == 1
    assert sol.countDistinctIntegers(20) == 18  # 1-9 (9) + 11-19 (9) = 18
    # 10->1, 20->2, both already counted via 1 and 2

    print("all tests passed")
