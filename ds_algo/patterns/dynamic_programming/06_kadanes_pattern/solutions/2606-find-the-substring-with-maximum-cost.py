"""
2606. Find the Substring With Maximum Cost
https://leetcode.com/problems/find-the-substring-with-maximum-cost/

Pattern: 06 - Kadane's Pattern

---
APPROACH: Kadane's Algorithm on mapped values
- Map each character to its value: if chars[i] == c then value is vals[i],
  otherwise value is (ord(c) - ord('a') + 1) by default.
- Run Kadane's algorithm on the resulting value array to find the maximum
  subarray sum. The empty substring has cost 0, so answer >= 0.

Time:  O(n)
Space: O(1) (aside from the value mapping)
---
"""

from typing import List


class Solution:
    def maximumCostSubstring(self, s: str, chars: str, vals: List[int]) -> int:
        """Return the maximum cost of any substring of s (including empty)."""
        # Build value mapping: default value of 'a'..'z' is 1..26
        value = {chr(ord("a") + i): i + 1 for i in range(26)}
        for c, v in zip(chars, vals):
            value[c] = v

        # Kadane's algorithm
        max_cost = 0  # empty substring has cost 0
        cur = 0
        for ch in s:
            cur += value[ch]
            if cur < 0:
                cur = 0
            max_cost = max(max_cost, cur)

        return max_cost


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    # Example 1
    assert sol.maximumCostSubstring("adaa", "d", [-1000]) == 2
    # Example 2
    assert sol.maximumCostSubstring("abc", "abc", [-1, -1, -1]) == 0
    # Example 3
    assert sol.maximumCostSubstring("abd", "b", [-3]) == 4
    # All positive default values
    assert sol.maximumCostSubstring("abc", "", []) == 6
    # Single char negative
    assert sol.maximumCostSubstring("a", "a", [-5]) == 0
    # Single char positive
    assert sol.maximumCostSubstring("a", "a", [10]) == 10

    print("Solution: all tests passed")
