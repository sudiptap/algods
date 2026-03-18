"""
691. Stickers to Spell Word (Hard)
https://leetcode.com/problems/stickers-to-spell-word/

Pattern: 11 - Bitmask DP

---
APPROACH: Bitmask DP on target characters.
- Represent which target characters have been covered as a bitmask of
  length len(target).  Bit i set means target[i] is covered.
- dp[mask] = minimum number of stickers to cover exactly the characters
  whose bits are set in mask.
- Base: dp[0] = 0 (nothing covered, 0 stickers used).
- Transition: for each reachable mask, find the lowest uncovered bit.
  Only try stickers that contain that character (avoids redundant orderings).
  Greedily apply the sticker to cover as many uncovered positions as possible,
  producing new_mask.  Update dp[new_mask] = min(dp[new_mask], dp[mask] + 1).
- Answer: dp[(1<<T)-1] (all characters covered).

Time:  O(2^T * S * T)  where T = len(target), S = number of stickers
Space: O(2^T)
---
"""

from collections import Counter


class Solution:
    def minStickers(self, stickers: list[str], target: str) -> int:
        """Return the minimum number of stickers to spell target, or -1 if impossible.

        Args:
            stickers: List of sticker words (each can be used infinitely).
            target: The word to spell.

        Returns:
            Minimum stickers needed, or -1 if impossible.
        """
        t = len(target)
        full = (1 << t) - 1

        # Precompute character counts for each sticker
        sticker_counts = [Counter(s) for s in stickers]

        # dp[mask] = min stickers to cover the characters indicated by set bits
        dp = [-1] * (1 << t)
        dp[0] = 0  # nothing covered yet, 0 stickers used

        for mask in range(full):
            if dp[mask] == -1:
                continue

            # Find the lowest bit NOT set in mask (first uncovered char)
            first_uncovered = -1
            for b in range(t):
                if not (mask & (1 << b)):
                    first_uncovered = b
                    break

            # Only try stickers that contain target[first_uncovered]
            for sc in sticker_counts:
                if target[first_uncovered] not in sc:
                    continue

                new_mask = mask
                remaining = dict(sc)
                for b in range(t):
                    if not (new_mask & (1 << b)):
                        ch = target[b]
                        if remaining.get(ch, 0) > 0:
                            remaining[ch] -= 1
                            new_mask |= (1 << b)

                if dp[new_mask] == -1 or dp[new_mask] > dp[mask] + 1:
                    dp[new_mask] = dp[mask] + 1

        return dp[full]


# ---------- Tests ----------
def test_stickers_to_spell_word():
    sol = Solution()

    # Example 1
    assert sol.minStickers(["with", "example", "science"], "thehat") == 3

    # Example 2: impossible
    assert sol.minStickers(["notice", "possible"], "basicbasic") == -1

    # Single char target, single sticker with that char
    assert sol.minStickers(["a"], "a") == 1

    # Need 2 of same sticker
    assert sol.minStickers(["ab"], "aabb") == 2

    # Already empty target
    assert sol.minStickers(["abc"], "") == 0

    print("All tests passed for 691. Stickers to Spell Word")


if __name__ == "__main__":
    test_stickers_to_spell_word()
