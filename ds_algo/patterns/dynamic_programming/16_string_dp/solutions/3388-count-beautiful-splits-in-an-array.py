"""
3388. Count Beautiful Splits in an Array (Medium)

Pattern: 16_string_dp
- Split array into 3 non-empty parts. A split is beautiful if part1 is a prefix of
  part2, OR part2 is a prefix of part3. Count beautiful splits.

Approach:
- Precompute LCP[i][j] = length of longest common prefix of nums[i:] and nums[j:].
- LCP[i][j] = 0 if nums[i] != nums[j], else 1 + LCP[i+1][j+1].
- For split (i, j) where part1 = [0..i-1], part2 = [i..j-1], part3 = [j..n-1]:
  - len1 = i, len2 = j - i, len3 = n - j
  - Beautiful if LCP[0][i] >= len1 (part1 is prefix of part2) or
    LCP[i][j] >= len2 (part2 is prefix of part3).

Complexity:
- Time:  O(n^2)
- Space: O(n^2)
"""

from typing import List


class Solution:
    def beautifulSplits(self, nums: List[int]) -> int:
        n = len(nums)

        # LCP[i][j] = longest common prefix of nums[i:] and nums[j:]
        lcp = [[0] * (n + 1) for _ in range(n + 1)]
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if nums[i] == nums[j]:
                    lcp[i][j] = lcp[i + 1][j + 1] + 1

        count = 0
        for i in range(1, n - 1):  # end of part1 (exclusive), start of part2
            for j in range(i + 1, n):  # end of part2 (exclusive), start of part3
                len1 = i
                len2 = j - i
                # part1 is prefix of part2
                if lcp[0][i] >= len1:
                    count += 1
                # part2 is prefix of part3
                elif lcp[i][j] >= len2:
                    count += 1

        return count


# ---------- Tests ----------
def test():
    sol = Solution()

    # Example 1
    assert sol.beautifulSplits([1, 1, 2, 1]) == 2

    # Example 2
    assert sol.beautifulSplits([1, 2, 3, 4]) == 0

    # All same
    assert sol.beautifulSplits([1, 1, 1]) == 1

    print("All tests passed!")


if __name__ == "__main__":
    test()
