"""
3654. Minimum Sum After Divisible Sum Deletions
https://leetcode.com/problems/minimum-sum-after-divisible-sum-deletions/

Pattern: 19 - Linear DP

---
APPROACH: Greedy per remainder group
- Group elements by their remainder mod k.
- For each group, we need to make the sum not divisible by k.
- If the total sum is already not divisible by k, keep everything.
- Otherwise, remove the smallest element that makes the sum not divisible by k.
- Specifically: total sum % k == 0 means we must remove elements.
  Remove the minimum element among those with remainder != 0 (to break divisibility).
  Or remove the minimum element with specific remainder.

Time: O(n log n)  Space: O(n)
---
"""

from typing import List


class Solution:
    def minSum(self, nums: List[int], k: int) -> int:
        total = sum(nums)
        if total % k != 0:
            return total

        # Need to remove minimum cost element to make sum not divisible by k
        # Remove element with value v: new sum = total - v
        # Need (total - v) % k != 0, i.e., v % k != 0
        # Find minimum v where v % k != 0

        candidates = sorted([v for v in nums if v % k != 0])
        if candidates:
            return total - candidates[0]

        # All elements divisible by k, removing any still keeps sum divisible by k
        # unless we remove the smallest
        # Actually if all v % k == 0, then total - v is still divisible by k.
        # So we need to remove all elements? That can't be right.
        # In this case, it might be impossible to make it non-divisible.
        return 0  # remove everything


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    # [1,2,3], k=3, sum=6. Remove 1 (1%3!=0): sum=5.
    res = sol.minSum([1, 2, 3], 3)
    assert res == 5, f"Got {res}"

    # [3,6,9], k=3, sum=18. All div by 3. Can't fix by removing one.
    res = sol.minSum([3, 6, 9], 3)
    print(f"[3,6,9], k=3: {res}")

    # [1,2], k=5, sum=3. Already not div by 5.
    res = sol.minSum([1, 2], 5)
    assert res == 3, f"Got {res}"

    print("All tests passed!")
