"""
3615. Longest Palindromic Path in Graph
https://leetcode.com/problems/longest-palindromic-path-in-graph/

Pattern: 08 - Palindromic Subsequence

---
APPROACH: DFS merging palindromic arms by character (LC 2246 style)
- Root tree at node 0. For each node v, from its children collect the
  longest "palindromic arm" going downward.
- An arm from child u through v: length grows if chars at alternating
  depth levels match. Specifically, dp[u] indexed by char c means: from u
  going down, the longest palindromic arm whose outermost char is c.
- At node v, from child u (char cu): the arm from v through u has length
  1 + dp_child[cv], because after matching cu with something on the other
  side, the next char to match is cv (v's char).
- Two arms from v with same starting char (cu1==cu2) combine into a
  palindrome of length arm1 + 1 + arm2 centered at v.
- For each node, dp[v][c] = max arm through any child starting with char c.

Time: O(n * 26)  Space: O(n)
---
"""

from typing import List
from collections import defaultdict
import sys

sys.setrecursionlimit(300000)


class Solution:
    def longestPalindromicPath(self, parent: List[int], s: str) -> int:
        n = len(parent)
        children = defaultdict(list)
        for i in range(1, n):
            children[parent[i]].append(i)

        self.ans = 1

        def dfs(v):
            # Returns best[c] = longest arm from v starting with char c
            # (going through a child with char c).
            best = [0] * 26
            cv = ord(s[v]) - ord('a')

            for u in children[v]:
                child_best = dfs(u)
                cu = ord(s[u]) - ord('a')

                # Arm from v through u:
                # u has char cu. From u, the sub-arm continuing with char cv
                # has length child_best[cv]. So total arm = 1 + child_best[cv].
                arm_len = 1 + child_best[cv]

                # Single arm from v: v(cv) + arm starting with cu, length arm_len.
                # Path of 1 + arm_len nodes. It's palindromic because the arm
                # construction matched chars palindromically.
                # arm_len = 1 + child_best[cv]:
                #   - child_best[cv] > 0: arm goes u(cu), then deeper matching cv, etc.
                #     Path: cv, cu, cv, (cu, cv, ...) - palindromic.
                #   - child_best[cv] = 0: arm = 1, path = cv, cu. Palindromic only if cv==cu.
                if arm_len > 1 or cu == cv:
                    self.ans = max(self.ans, 1 + arm_len)

                # Pair with existing arm from v with same starting char cu
                if best[cu] > 0:
                    self.ans = max(self.ans, best[cu] + 1 + arm_len)
                best[cu] = max(best[cu], arm_len)

            return best

        dfs(0)
        return self.ans


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    # Tree: 0(a) -> 1(b) -> 2(a). Parent = [-1, 0, 1].
    # Palindrome "aba" = path 0-1-2, length 3.
    # At node 0: child 1 (b). arm from 0 through 1: 1 + child_best_of_1[0('a')].
    # At node 1: child 2 (a). arm from 1 through 2: 1 + child_best_of_2[1('b')] = 1+0 = 1.
    #   best[0('a')] = 1 at node 1. Return best.
    # Back at 0: cu = 1('b'). arm_len = 1 + child_best[0('a')] = 1 + 1 = 2.
    #   best[1('b')] = 2. No pairing. ans stays 1.
    # Hmm, ans=1. The palindrome isn't detected because there's only one child.

    # The issue: palindrome 0-1-2 passes through all 3 nodes on a single path.
    # In a rooted tree at 0, node 0 has one child (1), node 1 has one child (2).
    # There's no "pairing of two arms" at any node. The palindrome is a straight path.

    # For straight-path palindromes, we need: path from v downward that IS a palindrome.
    # arm of length 2 from node 0: chars 'a','b','a' = palindrome!
    # So we should track: longest palindromic downward path from each node.
    # arm_len = 1 + child_best[cv] = 1 + 1 = 2 from node 0.
    # Path length = arm_len + 1? No, arm_len already counts nodes in the arm from child.
    # v + arm of length arm_len = 1 + arm_len total nodes.
    # So palindrome = 1 + 2 = 3! We should update ans with (1 + arm_len) too.

    # Fix: also update self.ans = max(self.ans, 1 + arm_len) for single arms.
    # But is the single arm palindromic? Yes: arm is built by palindromic matching.
    # v(cv) -> u(cu) -> w(cv) reads "cv cu cv" which IS a palindrome.

    # Let me fix the code above.
    # Actually it's already correct in theory but the ans update for single arm is missing.

    # For now test with the known parent array format
    # Path a-b-a: palindrome of length 3
    res = sol.longestPalindromicPath([-1, 0, 1], "aba")
    assert res == 3, f"Got {res}"

    # Star b with two a leaves: palindrome a-b-a, length 3
    res = sol.longestPalindromicPath([-1, 0, 0], "baa")
    assert res == 3, f"Got {res}"

    # Path a-b-c: no palindrome > 1
    res = sol.longestPalindromicPath([-1, 0, 1], "abc")
    assert res == 1, f"Got {res}"

    # a-a: palindrome length 2
    res = sol.longestPalindromicPath([-1, 0], "aa")
    assert res == 2, f"Got {res}"

    # Single node
    res = sol.longestPalindromicPath([-1], "a")
    assert res == 1, f"Got {res}"

    print("All tests passed!")
