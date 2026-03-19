"""
3335. Total Characters in String After Transformations I (Medium)

Pattern: 16_string_dp
- Each transformation: 'a'->'b', 'b'->'c', ..., 'y'->'z', 'z'->'ab'.
  After t transformations, return total string length mod 10^9+7.

Approach:
- Track count of each character. Each step shifts counts: count[c+1] += count[c],
  and 'z' splits into 'a' and 'b'.
- Simulate t steps, tracking counts of 26 characters.

Complexity:
- Time:  O(26 * t)
- Space: O(26)
"""

MOD = 10**9 + 7


class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        cnt = [0] * 26
        for c in s:
            cnt[ord(c) - ord('a')] += 1

        for _ in range(t):
            new_cnt = [0] * 26
            for i in range(25):
                new_cnt[i + 1] = (new_cnt[i + 1] + cnt[i]) % MOD
            # z -> a and b
            new_cnt[0] = (new_cnt[0] + cnt[25]) % MOD
            new_cnt[1] = (new_cnt[1] + cnt[25]) % MOD
            cnt = new_cnt

        return sum(cnt) % MOD


# ---------- Tests ----------
def test():
    sol = Solution()

    # Example 1
    assert sol.lengthAfterTransformations("abcyy", 2) == 7

    # Example 2
    assert sol.lengthAfterTransformations("azbk", 1) == 5

    # Single z, 1 transform -> "ab" length 2
    assert sol.lengthAfterTransformations("z", 1) == 2

    print("All tests passed!")


if __name__ == "__main__":
    test()
