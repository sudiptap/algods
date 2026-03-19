"""
1681. Minimum Incompatibility
https://leetcode.com/problems/minimum-incompatibility/

Pattern: 11 - Bitmask DP

---
APPROACH: Bitmask DP with subset enumeration
- Partition n elements into n/k groups of size k each.
- Incompatibility of a group = max - min (group must have all distinct values).
- dp[mask] = min total incompatibility for elements in mask, partitioned into groups of size k.
- Precompute cost of each valid subset of size k (no duplicate values).
- Transition: for each mask, try removing a valid group (submask of size k).

Time: O(3^n) for subset enumeration (n <= 16)
Space: O(2^n)
---
"""

from typing import List


class Solution:
    def minimumIncompatibility(self, nums: List[int], k: int) -> int:
        n = len(nums)
        group_size = n // k
        full = (1 << n) - 1
        INF = float('inf')

        # Precompute cost for each subset of size group_size
        cost = {}
        for mask in range(1, full + 1):
            if bin(mask).count('1') != group_size:
                continue
            vals = []
            for i in range(n):
                if mask & (1 << i):
                    vals.append(nums[i])
            if len(set(vals)) != group_size:
                continue  # duplicates
            cost[mask] = max(vals) - min(vals)

        # DP
        dp = [INF] * (full + 1)
        dp[0] = 0

        for mask in range(1, full + 1):
            if bin(mask).count('1') % group_size != 0:
                continue
            # Try all valid submasks of mask
            sub = mask
            while sub > 0:
                if sub in cost and dp[mask ^ sub] < INF:
                    dp[mask] = min(dp[mask], dp[mask ^ sub] + cost[sub])
                sub = (sub - 1) & mask

        return dp[full] if dp[full] < INF else -1


# --- Tests ---
def test():
    sol = Solution()

    assert sol.minimumIncompatibility([1, 2, 1, 4], 2) == 4
    assert sol.minimumIncompatibility([6, 3, 8, 1, 3, 1, 2, 2], 4) == 6
    assert sol.minimumIncompatibility([5, 3, 3, 6, 3, 3], 3) == -1

    # All same
    assert sol.minimumIncompatibility([1, 1, 1, 1], 4) == 0

    print("All tests passed!")


if __name__ == "__main__":
    test()
