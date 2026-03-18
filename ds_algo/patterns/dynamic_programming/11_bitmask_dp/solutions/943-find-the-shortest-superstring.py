"""
943. Find the Shortest Superstring
https://leetcode.com/problems/find-the-shortest-superstring/

Pattern: 11 - Bitmask DP (TSP variant)

---
APPROACH: Bitmask DP — Travelling Salesman on words
1. Precompute overlap[i][j] = max overlap when word j is appended after word i
   (longest suffix of words[i] that is a prefix of words[j]).
2. dp[mask][i] = minimum total superstring length using the set of words in
   `mask`, ending with word i. Transition: try adding word j not in mask.
3. Track parent pointers to reconstruct the actual superstring.

Time: O(n^2 * 2^n)  Space: O(n * 2^n)  where n = len(words) <= 12
---
"""

from typing import List


class Solution:
    def shortestSuperstring(self, words: List[str]) -> str:
        """Return the shortest string that contains each word as a substring."""
        n = len(words)

        # Precompute overlaps: overlap[i][j] = length of longest suffix of
        # words[i] that equals a prefix of words[j].
        overlap = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                max_k = min(len(words[i]), len(words[j]))
                for k in range(max_k, 0, -1):
                    if words[i].endswith(words[j][:k]):
                        overlap[i][j] = k
                        break

        full = (1 << n) - 1
        INF = float("inf")

        # dp[mask][i] = min superstring length for words in mask, ending at i
        dp = [[INF] * n for _ in range(1 << n)]
        parent = [[-1] * n for _ in range(1 << n)]

        # Base cases: each word alone
        for i in range(n):
            dp[1 << i][i] = len(words[i])

        # Fill DP
        for mask in range(1, 1 << n):
            for i in range(n):
                if dp[mask][i] == INF:
                    continue
                if not (mask & (1 << i)):
                    continue
                for j in range(n):
                    if mask & (1 << j):
                        continue
                    new_mask = mask | (1 << j)
                    cost = dp[mask][i] + len(words[j]) - overlap[i][j]
                    if cost < dp[new_mask][j]:
                        dp[new_mask][j] = cost
                        parent[new_mask][j] = i

        # Find optimal last word
        last = min(range(n), key=lambda i: dp[full][i])

        # Reconstruct path
        path = []
        mask = full
        cur = last
        while cur != -1:
            path.append(cur)
            prev = parent[mask][cur]
            mask ^= (1 << cur)
            cur = prev
        path.reverse()

        # Build result string
        result = [words[path[0]]]
        for k in range(1, len(path)):
            i, j = path[k - 1], path[k]
            result.append(words[j][overlap[i][j]:])

        return "".join(result)


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    # Example 1
    res1 = sol.shortestSuperstring(["alex", "loves", "leetcode"])
    assert len(res1) == len("alexlovesleetcode")
    for w in ["alex", "loves", "leetcode"]:
        assert w in res1, f"{w} not in {res1}"

    # Example 2
    res2 = sol.shortestSuperstring(["catg", "ctaagt", "gcta", "ttca", "atgcatc"])
    for w in ["catg", "ctaagt", "gcta", "ttca", "atgcatc"]:
        assert w in res2, f"{w} not in {res2}"
    assert len(res2) == 16  # known optimal length

    # Single word
    res3 = sol.shortestSuperstring(["abc"])
    assert res3 == "abc"

    # Full overlap
    res4 = sol.shortestSuperstring(["abc", "bcd"])
    assert len(res4) == 4
    assert "abc" in res4 and "bcd" in res4

    # No overlap
    res5 = sol.shortestSuperstring(["ab", "cd"])
    assert len(res5) == 4
    assert "ab" in res5 and "cd" in res5

    print("all tests passed")
