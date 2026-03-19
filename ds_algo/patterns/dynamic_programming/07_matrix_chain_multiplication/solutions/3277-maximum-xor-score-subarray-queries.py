"""
3277. Maximum XOR Score Subarray Queries (Hard)

Pattern: 07_matrix_chain_multiplication (Interval DP)
- Given array nums, XOR score of subarray [l,r] is computed by repeatedly XORing
  adjacent pairs until one value remains. Answer queries [l,r] with max XOR score
  in any subarray within [l,r].

Approach:
- The XOR score of [l,r] follows interval DP: score[l][r] = score[l][r-1] ^ score[l+1][r].
- Base case: score[i][i] = nums[i].
- Then compute mx[l][r] = max XOR score over all subarrays in [l,r]:
  mx[l][r] = max(score[l][r], mx[l][r-1], mx[l+1][r]).
- Answer each query (l,r) with mx[l][r].

Complexity:
- Time:  O(n^2 + q) where n = len(nums), q = number of queries
- Space: O(n^2)
"""

from typing import List


class Solution:
    def maximumSubarrayXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums)
        # score[l][r] = XOR score of subarray [l..r]
        score = [[0] * n for _ in range(n)]
        mx = [[0] * n for _ in range(n)]

        for i in range(n):
            score[i][i] = nums[i]
            mx[i][i] = nums[i]

        for length in range(2, n + 1):
            for l in range(n - length + 1):
                r = l + length - 1
                score[l][r] = score[l][r - 1] ^ score[l + 1][r]
                mx[l][r] = max(score[l][r], mx[l][r - 1], mx[l + 1][r])

        return [mx[l][r] for l, r in queries]


# ---------- Tests ----------
def test():
    sol = Solution()

    # Example 1
    assert sol.maximumSubarrayXor([2, 8, 4, 32, 16, 1], [[0, 1], [1, 4], [0, 5]]) == [10, 60, 60]

    # Example 2
    assert sol.maximumSubarrayXor([0, 7, 3, 2, 8, 5, 1], [[0, 3], [1, 5], [2, 4], [2, 6], [5, 6]]) == [7, 14, 11, 14, 5]

    # Single element
    assert sol.maximumSubarrayXor([5], [[0, 0]]) == [5]

    print("All tests passed!")


if __name__ == "__main__":
    test()
