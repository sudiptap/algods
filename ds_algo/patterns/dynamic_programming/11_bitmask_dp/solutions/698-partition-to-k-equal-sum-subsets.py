"""
698. Partition to K Equal Sum Subsets (Medium)
https://leetcode.com/problems/partition-to-k-equal-sum-subsets/

Pattern: 11 - Bitmask DP

---
APPROACH: Bitmask DP
- If total sum is not divisible by k, return False immediately.
- target = total_sum / k.
- dp[mask] = the current partial sum of the bucket being filled,
  using exactly the elements indicated by set bits in mask,
  modulo target.  If dp[mask] == -1, the state is unreachable.
- For each reachable mask, try adding each unused element j.
  If adding nums[j] does not exceed target, set
  dp[mask | (1<<j)] = (dp[mask] + nums[j]) % target.
  (When partial sum hits target, it resets to 0 for the next bucket.)
- Answer: dp[(1<<n)-1] == 0  (all elements used, last bucket complete).

Optimisation: sort nums descending so large elements prune early.

Time:  O(2^n * n)
Space: O(2^n)
---
"""


class Solution:
    def canPartitionKSubsets(self, nums: list[int], k: int) -> bool:
        """Return True if nums can be partitioned into k subsets of equal sum.

        Args:
            nums: List of positive integers (1 <= len(nums) <= 16).
            k: Number of subsets.

        Returns:
            True if a valid partition exists.
        """
        total = sum(nums)
        if total % k != 0:
            return False

        target = total // k
        n = len(nums)

        # Any single element larger than target makes it impossible
        if max(nums) > target:
            return False

        nums.sort(reverse=True)  # pruning: try large elements first

        full = (1 << n) - 1
        # dp[mask] = current bucket partial sum; -1 means unreachable
        dp = [-1] * (1 << n)
        dp[0] = 0

        for mask in range(full):
            if dp[mask] == -1:
                continue

            for j in range(n):
                if mask & (1 << j):
                    continue  # already used
                if dp[mask] + nums[j] > target:
                    continue  # would exceed bucket target

                new_mask = mask | (1 << j)
                new_val = (dp[mask] + nums[j]) % target
                # Only set if not already reached (first reach is fine
                # since all paths produce same modular value for valid states,
                # but we just need reachability).
                if dp[new_mask] == -1:
                    dp[new_mask] = new_val

        return dp[full] == 0


# ---------- Tests ----------
def test_partition_k_subsets():
    sol = Solution()

    # Example 1
    assert sol.canPartitionKSubsets([4, 3, 2, 3, 5, 2, 1], 4) is True

    # Example 2: impossible
    assert sol.canPartitionKSubsets([1, 2, 3, 4], 3) is False

    # All equal elements
    assert sol.canPartitionKSubsets([2, 2, 2, 2], 2) is True

    # k = 1: always true (total is one subset)
    assert sol.canPartitionKSubsets([1, 2, 3], 1) is True

    # Single element equals target
    assert sol.canPartitionKSubsets([5, 5, 5, 5], 4) is True

    # One element too large
    assert sol.canPartitionKSubsets([10, 1, 1, 1], 2) is False

    # Larger case
    assert sol.canPartitionKSubsets([1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 5) is True

    print("All tests passed for 698. Partition to K Equal Sum Subsets")


if __name__ == "__main__":
    test_partition_k_subsets()
