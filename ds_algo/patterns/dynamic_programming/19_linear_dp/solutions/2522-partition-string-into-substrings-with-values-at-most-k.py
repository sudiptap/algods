"""
2522. Partition String Into Substrings With Values at Most K
https://leetcode.com/problems/partition-string-into-substrings-with-values-at-most-k/

Pattern: 19 - Linear DP (Greedy)

---
APPROACH: Greedy - extend current number while <= k
- Build current number digit by digit. If adding next digit makes it > k,
  start a new partition.
- If any single digit > k, return -1.

Time: O(n)  Space: O(1)
---
"""


class Solution:
    def minimumPartition(self, s: str, k: int) -> int:
        parts = 1
        cur = 0

        for c in s:
            d = int(c)
            if d > k:
                return -1
            cur = cur * 10 + d
            if cur > k:
                parts += 1
                cur = d

        return parts


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.minimumPartition("165462", 60) == 4
    assert sol.minimumPartition("238182", 5) == -1
    assert sol.minimumPartition("1", 1) == 1
    assert sol.minimumPartition("999", 1000) == 1

    print("all tests passed")
