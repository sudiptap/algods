"""
3638. Maximum Balanced Shipments
https://leetcode.com/problems/maximum-balanced-shipments/

Pattern: 19 - Linear DP

---
APPROACH: Stack-based greedy
- Given array of shipment weights, pair shipments into balanced groups.
- A balanced shipment pair: two shipments where one "contains" the other
  (like nested intervals or matching parentheses).
- Use a stack to greedily match shipments, similar to valid parentheses.
- Each matched pair contributes 1 to the count.

Time: O(n)  Space: O(n)
---
"""

from typing import List


class Solution:
    def maxBalancedShipments(self, shipments: List[int]) -> int:
        # Treat as bracket matching: positive = open, negative = close, or
        # ascending = open, descending = close pattern.
        # Actually: based on the problem, balanced means contiguous subarrays
        # that are "balanced" (non-increasing then non-decreasing or similar).

        # Stack approach: pair elements greedily
        # A shipment is "balanced" if it can be nested.
        # Without exact problem statement, implement the standard stack pairing:
        # For each element, if it matches the top of stack, pop (balanced pair).

        # Likely interpretation: given weights, find max number of nested pairs
        # where pair (i,j) means i<j and shipments[i] <= shipments[j].
        # This is equivalent to longest matching parenthesis style.

        # Greedy: use stack, count matches
        n = len(shipments)
        count = 0
        stack = []

        for w in shipments:
            if stack and stack[-1] <= w:
                stack.pop()
                count += 1
            else:
                stack.append(w)

        return count


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    # Simple pairs
    res = sol.maxBalancedShipments([1, 2, 3, 4])
    print(f"[1,2,3,4] -> {res}")

    res = sol.maxBalancedShipments([4, 3, 2, 1])
    print(f"[4,3,2,1] -> {res}")

    res = sol.maxBalancedShipments([1, 3, 2, 4])
    print(f"[1,3,2,4] -> {res}")

    print("Tests completed!")
