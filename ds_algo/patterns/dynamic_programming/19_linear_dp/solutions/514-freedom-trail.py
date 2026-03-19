"""
514. Freedom Trail (Hard)
https://leetcode.com/problems/freedom-trail/

Pattern: Linear DP

Given a ring string and a key string, find the minimum number of steps
to spell the key. The ring is circular; at each step you can rotate
clockwise or counterclockwise. Each character spelled costs 1 button
press in addition to rotation steps.

Approach:
    dp[i][j] = minimum steps to spell key[i:] when ring is aligned at
    position j.

    For each character key[i], try all positions in ring that match it.
    Cost = min(clockwise, counterclockwise) rotation + 1 (press) + dp[i+1][new_pos].

    Process from last character of key backward.

Time:  O(len(key) * len(ring)^2)
Space: O(len(key) * len(ring))
"""

from collections import defaultdict


class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        """Return min steps to spell key on the ring."""
        n = len(ring)
        m = len(key)

        # Precompute positions of each character
        pos = defaultdict(list)
        for i, ch in enumerate(ring):
            pos[ch].append(i)

        # dp[j] = min cost to finish from current key char when ring at j
        dp = [0] * n

        for i in range(m - 1, -1, -1):
            new_dp = [float("inf")] * n
            for j in range(n):
                for k in pos[key[i]]:
                    dist = abs(j - k)
                    min_dist = min(dist, n - dist)
                    new_dp[j] = min(new_dp[j], min_dist + 1 + dp[k])
            dp = new_dp

        return dp[0]


# ───────────────────────── tests ─────────────────────────

def test_example1():
    assert Solution().findRotateSteps("godding", "gd") == 4

def test_example2():
    assert Solution().findRotateSteps("godding", "godding") == 13

def test_single_char():
    assert Solution().findRotateSteps("a", "a") == 1

def test_ring_rotation():
    # ring="abc", key="c" -> rotate 1 step CCW + 1 press = 2
    assert Solution().findRotateSteps("abc", "c") == 2

def test_multiple_same_char():
    # ring="abcab", key="a" -> already at a, just press = 1
    assert Solution().findRotateSteps("abcab", "a") == 1

def test_circular():
    # ring = "edcba", key = "a" -> go 1 step left (CCW) = 1 + 1 = 2
    # or 4 steps right = 4 + 1 = 5. Min is 2.
    assert Solution().findRotateSteps("edcba", "a") == 2


if __name__ == "__main__":
    import pytest
    pytest.main([__file__, "-v"])
