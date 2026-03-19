"""
3292. Minimum Number of Valid Strings to Form Target II (Hard)

Pattern: 16_string_dp
- Same as 3291 but with larger constraints requiring optimized approach.

Approach:
- For each word, compute Z-function on word + '#' + target to find, for each position
  in target, the max prefix length of that word matching starting there.
- max_reach[i] = max prefix length of any word matching target starting at i.
- Then greedy/dp: jump as far as possible each step (like jump game).

Complexity:
- Time:  O(sum of word lengths + n * num_words) for Z, O(n) for greedy
- Space: O(n + max word length)
"""

from typing import List


class Solution:
    def minValidStrings(self, words: List[str], target: str) -> int:
        n = len(target)
        max_reach = [0] * n  # max prefix length starting at position i

        for word in words:
            s = word + '#' + target
            m = len(s)
            z = [0] * m
            l, r = 0, 0
            for i in range(1, m):
                if i < r:
                    z[i] = min(r - i, z[i - l])
                while i + z[i] < m and s[z[i]] == s[i + z[i]]:
                    z[i] += 1
                if i + z[i] > r:
                    l, r = i, i + z[i]

            wl = len(word)
            # Positions in target start at index wl+1 in s
            for i in range(wl + 1, m):
                ti = i - wl - 1  # position in target
                max_reach[ti] = max(max_reach[ti], z[i])

        # Greedy jump game
        ans = 0
        cur_end = 0
        farthest = 0
        for i in range(n):
            farthest = max(farthest, i + max_reach[i])
            if i == cur_end:
                if farthest == i:
                    return -1
                ans += 1
                cur_end = farthest
                if cur_end >= n:
                    return ans

        return ans


# ---------- Tests ----------
def test():
    sol = Solution()

    # Example 1
    assert sol.minValidStrings(["abc", "aaaaa", "bcdef"], "aabcdabc") == 3

    # Example 2
    assert sol.minValidStrings(["abababab", "ab"], "ababaababa") == 2

    # Example 3
    assert sol.minValidStrings(["abcdef"], "xyz") == -1

    print("All tests passed!")


if __name__ == "__main__":
    test()
