"""
2380. Time Needed to Rearrange a Binary String
https://leetcode.com/problems/time-needed-to-rearrange-a-binary-string/

Pattern: 19 - Linear DP

---
APPROACH: Track zeros before each 1
- Each second, every "01" becomes "10" simultaneously.
- For each '1', the number of steps it needs = max(prev_steps, zeros_before_it)
  where zeros_before_it is the count of '0's to its left.
- This is because a '1' must wait for the previous '1' to finish moving,
  or move past all zeros ahead of it.

Time: O(n)  Space: O(1)
---
"""


class Solution:
    def secondsToRemoveOccurrences(self, s: str) -> int:
        zeros = 0
        ans = 0

        for c in s:
            if c == '0':
                zeros += 1
            else:
                if zeros > 0:
                    ans = max(ans + 1, zeros)

        return ans


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.secondsToRemoveOccurrences("0110101") == 4
    assert sol.secondsToRemoveOccurrences("11100") == 0
    assert sol.secondsToRemoveOccurrences("001011") == 4
    assert sol.secondsToRemoveOccurrences("1") == 0
    assert sol.secondsToRemoveOccurrences("0") == 0

    print("all tests passed")
