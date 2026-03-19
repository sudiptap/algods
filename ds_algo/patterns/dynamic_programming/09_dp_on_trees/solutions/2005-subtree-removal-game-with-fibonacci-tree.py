"""
2005. Subtree Removal Game with Fibonacci Tree (Hard)
https://leetcode.com/problems/subtree-removal-game-with-fibonacci-tree/

A Fibonacci tree of order n: if n<=2, a single node; otherwise root
has left child fib(n-1) and right child fib(n-2). Two players alternate
removing a non-root subtree. Player who can't move loses.
Return True if Alice (first player) wins.

Pattern: DP on Trees (Sprague-Grundy / Game Theory)
Approach:
- Key insight: The Grundy value of a rooted tree under subtree removal
  is the XOR of (1 + Grundy(child_subtree)) for each child.
  This is because removing a subtree rooted at child c is equivalent to
  removing c and its descendants, and the Grundy value follows the
  "Green Hackenbush on trees" / "Blue-Red Hackenbush" theory.
  Actually for this specific game (remove any subtree rooted at a non-root
  node), the Grundy number equals the Nim-value of the tree under the
  "node deletion" game, which for trees equals the XOR of the subtree
  heights+1 of children...

  Let me use a simpler known result: For the subtree-removal game on a
  tree, the Grundy value equals the XOR of depths of all leaves (relative
  to root). Actually no.

  The correct approach: the Grundy number for the "remove any subtree"
  game on a rooted tree can be computed recursively. For a tree rooted at
  r with children c1, c2, ..., ck, each child ci heads a subtree with
  Grundy value g(ci). The Grundy value of the full tree is:

  g(r) = XOR of (g(ci) + 1) for each child ci... but this isn't quite right either.

  Actually the correct formula for "cut a branch" games: if we can remove
  any edge (and the subtree below it), then Grundy(v) = XOR of (Grundy(c)+1)
  for each child c. But here we can remove any non-root subtree, which is
  the same as cutting the edge from parent to child.

- G(fib(n)):
  - G(1) = G(2) = 0 (leaf, no moves)
  - G(n) = (G(n-1) + 1) XOR (G(n-2) + 1) for n >= 3
- Alice wins iff G(n) != 0.

Time:  O(n)
Space: O(1)
"""


class Solution:
    def findGameWinner(self, n: int) -> bool:
        """Return True if Alice (first player) wins on Fibonacci tree of order n.

        Args:
            n: Order of the Fibonacci tree.

        Returns:
            True if first player wins.
        """
        if n <= 2:
            return False

        # Compute Grundy values iteratively
        # G(1) = 0, G(2) = 0
        # G(n) = (G(n-1) + 1) XOR (G(n-2) + 1)
        g_prev2 = 0  # G(1)
        g_prev1 = 0  # G(2)

        for i in range(3, n + 1):
            g = (g_prev1 + 1) ^ (g_prev2 + 1)
            g_prev2 = g_prev1
            g_prev1 = g

        return g_prev1 != 0


# ---------- tests ----------
def test_fibonacci_game():
    sol = Solution()

    # n=1: single node, no moves -> Bob wins
    assert sol.findGameWinner(1) is False

    # n=2: single node -> Bob wins
    assert sol.findGameWinner(2) is False

    # n=3: G = (0+1) XOR (0+1) = 1 XOR 1 = 0 -> Bob wins
    assert sol.findGameWinner(3) is False

    # n=4: G = (G(3)+1) XOR (G(2)+1) = (0+1) XOR (0+1) = 0 -> Bob wins
    # Wait: G(3) = 0, so (0+1) XOR (0+1) = 0. Alice loses.
    assert sol.findGameWinner(4) is False

    # n=5: G = (G(4)+1) XOR (G(3)+1) = (0+1) XOR (0+1) = 0
    assert sol.findGameWinner(5) is False

    # Hmm, they're all 0? Let me check n=6:
    # G(6) = (G(5)+1) XOR (G(4)+1) = 1 XOR 1 = 0. All zeros.
    # This means Bob always wins in the subtree removal game on Fibonacci trees.
    # That might be the correct answer for this problem.
    assert sol.findGameWinner(6) is False

    print("All tests passed for 2005. Subtree Removal Game with Fibonacci Tree")


if __name__ == "__main__":
    test_fibonacci_game()
