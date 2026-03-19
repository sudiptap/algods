"""
2272. Substring With Largest Variance
https://leetcode.com/problems/substring-with-largest-variance/

Pattern: 06 - Kadane's Pattern

---
APPROACH: Modified Kadane's for each pair of characters (a, b)
- For each pair (a, b), find max(count_a - count_b) in any substring
  with at least one occurrence of b.
- Treat a as +1, b as -1, ignore other chars. Run Kadane's with constraint
  that b must appear at least once.
- Track: diff (running count_a - count_b), has_b (seen b in current subarray),
  diff_with_b (best diff that includes at least one b).

Time: O(26^2 * n)  Space: O(1)
---
"""


class Solution:
    def largestVariance(self, s: str) -> int:
        chars = set(s)
        ans = 0

        for a in chars:
            for b in chars:
                if a == b:
                    continue
                # Kadane's: a = +1, b = -1, need at least one b
                diff = 0
                has_b = False
                has_b_in_suffix = s.count(b) > 0  # can we still find b later?
                remaining_b = s.count(b)

                for c in s:
                    if c == a:
                        diff += 1
                    elif c == b:
                        remaining_b -= 1
                        diff -= 1
                        has_b = True

                    if has_b:
                        ans = max(ans, diff)

                    # Reset if diff < 0 and there's still a b ahead
                    if diff < 0:
                        if remaining_b > 0:
                            diff = 0
                            has_b = False

        return ans


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.largestVariance("aababbb") == 3
    assert sol.largestVariance("abcde") == 0
    assert sol.largestVariance("a") == 0
    assert sol.largestVariance("lripaa") == 1
    assert sol.largestVariance("abb") == 1

    print("all tests passed")
