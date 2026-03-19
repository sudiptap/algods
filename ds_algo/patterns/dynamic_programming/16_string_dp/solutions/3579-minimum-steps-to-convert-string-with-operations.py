"""
3579. Minimum Steps to Convert String with Operations
https://leetcode.com/problems/minimum-steps-to-convert-string-with-operations/

Pattern: 16 - String DP

---
APPROACH: DP on transformation
- Given source and target strings, find minimum operations to convert.
- Operations: select a substring, then either shift all chars by same amount
  or reverse the substring (each counts as one step).
- DP approach: dp[i] = min steps to convert source[0..i-1] to target[0..i-1].
- For each position i, try extending a previous operation or starting new one.
- Key insight: a single shift operation can convert a contiguous block where
  all chars need the same shift. A reverse+shift can handle reversed blocks.
- Greedy/DP: partition into minimal segments where each segment can be
  handled by one or two operations.

Time: O(n^2)  Space: O(n)
---
"""


class Solution:
    def minOperations(self, source: str, target: str) -> int:
        n = len(source)
        if source == target:
            return 0

        # Compute shift needed at each position
        shifts = [(ord(target[i]) - ord(source[i])) % 26 for i in range(n)]

        # dp[i] = min operations to handle positions 0..i-1
        dp = [0] * (n + 1)

        for i in range(1, n + 1):
            # Option 1: handle position i-1 alone (1 operation if shift != 0)
            dp[i] = dp[i - 1] + (0 if shifts[i - 1] == 0 else 1)

            # Option 2: extend a block [j..i-1] with same shift (1 operation)
            for j in range(i - 1, 0, -1):
                if shifts[j - 1] == shifts[i - 1]:
                    # All positions j-1..i-1 same shift? No, just need contiguous same shift.
                    # Check if all shifts[j-1..i-1] are the same
                    all_same = all(shifts[m] == shifts[i - 1] for m in range(j - 1, i))
                    if all_same:
                        cost = 0 if shifts[i - 1] == 0 else 1
                        dp[i] = min(dp[i], dp[j - 1] + cost)
                else:
                    break

        return dp[n]


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.minOperations("abc", "abc") == 0
    assert sol.minOperations("abc", "bcd") == 1  # shift all by 1
    assert sol.minOperations("abc", "bce") == 2  # different shifts needed
    assert sol.minOperations("a", "z") == 1

    print("All tests passed!")
