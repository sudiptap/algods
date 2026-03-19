"""
2310. Sum of Numbers With Units Digit K
https://leetcode.com/problems/sum-of-numbers-with-units-digit-k/

Pattern: 19 - Linear DP (Math)

---
APPROACH: Math - check if num - n*k >= 0 and divisible by 10
- We need n positive integers each with units digit k that sum to num.
- Sum of n numbers each with units digit k has units digit (n*k) % 10.
- So we need (n*k) % 10 == num % 10, and n*k <= num (so remainder is non-negative
  and divisible by 10, distributable among the n numbers).
- Try n = 1, 2, ..., up to num//k (if k>0) or special case k=0.
- If k=0, only valid if num%10==0, answer is 1 (just num itself if units digit is 0).

Time: O(1) - at most 10 iterations  Space: O(1)
---
"""


class Solution:
    def minimumNumbers(self, num: int, k: int) -> int:
        if num == 0:
            return 0
        # Try n = 1..10 (units digit cycles every 10)
        for n in range(1, 11):
            if n * k > num:
                break
            if (n * k) % 10 == num % 10:
                return n
        return -1


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.minimumNumbers(58, 9) == 2
    assert sol.minimumNumbers(37, 2) == -1
    assert sol.minimumNumbers(0, 7) == 0
    assert sol.minimumNumbers(10, 5) == 2
    assert sol.minimumNumbers(5, 5) == 1

    print("all tests passed")
