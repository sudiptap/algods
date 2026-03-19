"""
3751. Total Waviness of Numbers in Range I
https://leetcode.com/problems/total-waviness-of-numbers-in-range-i/

Pattern: 13 - Digit DP

---
APPROACH: Brute force (constraints: num2 <= 10^5)
- Waviness = count of peaks + valleys among interior digits.
- A peak: digit > both neighbors. A valley: digit < both neighbors.
- Since num2 <= 10^5, iterate and compute waviness for each number.

Time: O((num2 - num1) * d)  Space: O(d)
where d = number of digits (at most 6)
---
"""


class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        def waviness(x):
            digits = []
            while x > 0:
                digits.append(x % 10)
                x //= 10
            digits.reverse()
            if len(digits) < 3:
                return 0
            w = 0
            for i in range(1, len(digits) - 1):
                if digits[i] > digits[i - 1] and digits[i] > digits[i + 1]:
                    w += 1
                elif digits[i] < digits[i - 1] and digits[i] < digits[i + 1]:
                    w += 1
            return w

        return sum(waviness(x) for x in range(num1, num2 + 1))


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.totalWaviness(120, 130) == 3
    assert sol.totalWaviness(198, 202) == 3
    assert sol.totalWaviness(4848, 4848) == 2
    assert sol.totalWaviness(1, 9) == 0
    assert sol.totalWaviness(10, 99) == 0

    print("all tests passed")
