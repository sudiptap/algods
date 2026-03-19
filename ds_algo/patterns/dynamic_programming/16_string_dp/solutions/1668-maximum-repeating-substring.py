"""
1668. Maximum Repeating Substring
https://leetcode.com/problems/maximum-repeating-substring/

Pattern: 16 - String DP

---
APPROACH: Linear check / KMP-based
- Try word repeated k times for k = 1, 2, 3, ... until it's no longer a substring.
- Max k is len(sequence) // len(word).
- Simple approach: incrementally build repeated string and check substring membership.

Time: O(n * k) where n = len(sequence), k = max repeats
Space: O(n)
---
"""


class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        k = 0
        repeated = word
        while repeated in sequence:
            k += 1
            repeated += word
        return k


# --- Tests ---
def test():
    sol = Solution()

    assert sol.maxRepeating("ababc", "ab") == 2
    assert sol.maxRepeating("ababc", "ba") == 1
    assert sol.maxRepeating("ababc", "ac") == 0
    assert sol.maxRepeating("aaabaaaabaaabaaaabaaaabaaaabaaaaba", "aaaba") == 5
    assert sol.maxRepeating("a", "a") == 1
    assert sol.maxRepeating("aaa", "a") == 3

    print("All tests passed!")


if __name__ == "__main__":
    test()
