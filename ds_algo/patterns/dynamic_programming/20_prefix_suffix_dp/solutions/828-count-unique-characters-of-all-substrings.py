"""
828. Count Unique Characters of All Substrings of a Given String
https://leetcode.com/problems/count-unique-characters-of-all-substrings-of-a-given-string/

Pattern: 20 - Prefix/Suffix DP

---
APPROACH: Contribution of each character
- For each character at position i, count how many substrings have this
  character appearing exactly once (making it "unique").
- Track last two occurrences of each character: prev_prev and prev.
- If character c is at position i, its previous occurrence is at prev,
  and the one before that is at prev_prev:
  - It contributes to substrings [l, r] where prev_prev < l <= prev and i <= r < next_occurrence.
  - Simplified: contribution = (i - prev) * (prev - prev_prev) for prev.
  - Process left-to-right, and at end flush remaining.
- Alternative: at each index i, add (i - last[c]) * (last[c] - second_last[c]) when we see c.

Time: O(n)  Space: O(26) = O(1)
---
"""


class Solution:
    def uniqueLetterString(self, s: str) -> int:
        # Track last two positions for each character
        # last[c] = most recent index of c, second_last[c] = one before that
        last = {}
        second_last = {}
        result = 0

        for i, c in enumerate(s):
            prev = last.get(c, -1)
            prev_prev = second_last.get(c, -1)

            # Character at position prev contributed to substrings where it
            # was unique. Now that we see c again at i, we finalize the
            # contribution of the occurrence at prev.
            # But actually, we can compute contribution incrementally.

            # Let's use a different approach: running sum.
            # dp[i] = sum of uniqueChars for all substrings ending at i.
            # When we see s[i] = c:
            #   dp[i] = dp[i-1] + (i - last[c]) - (last[c] - second_last[c])
            # Result = sum of all dp[i].
            pass

        # Reset and use the dp approach
        last = {}
        second_last = {}
        dp = 0
        result = 0

        for i, c in enumerate(s):
            prev = last.get(c, -1)
            prev_prev = second_last.get(c, -1)

            # dp += new substrings where c at i is unique: (i - prev)
            # dp -= substrings where c at prev was unique but now isn't: (prev - prev_prev)
            dp += (i - prev) - (prev - prev_prev)
            result += dp

            second_last[c] = prev
            last[c] = i

        return result


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.uniqueLetterString("ABC") == 10
    # Substrings: A(1), B(1), C(1), AB(2), BC(2), ABC(3) = 10
    assert sol.uniqueLetterString("ABA") == 8
    # A(1),B(1),A(1),AB(2),BA(2),ABA(1) = 8
    assert sol.uniqueLetterString("LEETCODE") == 92
    assert sol.uniqueLetterString("A") == 1

    print("all tests passed")
