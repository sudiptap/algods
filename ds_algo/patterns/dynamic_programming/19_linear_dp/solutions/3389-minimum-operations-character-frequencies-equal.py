"""
3389. Minimum Operations Character Frequencies Equal (Hard)

Pattern: 19_linear_dp
- Given string s, make all character frequencies equal using: insert, delete, or
  change a character. Minimum operations.

Approach:
- Count frequencies of each character. We want all used characters to have same freq f.
- Try every possible target frequency f (0 to n). For each f, compute cost:
  - For each char with freq c: if c > f, delete c-f; if c < f, we can change from
    chars being deleted or insert new ones.
- Actually: some characters will be deleted entirely (freq -> 0), some kept at freq f.
  Characters with freq > f: excess = c - f can be changed to help others or deleted.
  Characters with freq < f: deficit = f - c, need insertions or changes from excess.
- Better: try all target freq f. For each f, and for each character, cost is
  min(c, |c - f|) ... no, cost to make freq c become f = |c - f| changes+deletes+inserts.
  But we can also set some chars to 0 (cheaper if c < f).
- For each char, either keep at freq f (cost |c-f|) or remove entirely (cost c, but
  removed chars can become other chars via change).
- Optimal: sort freqs, try each f. For chars kept: those with c >= f delete excess,
  those with c < f need additions. Changes from excess can fill deficit.

Complexity:
- Time:  O(26 * n) trying all frequencies
- Space: O(26)
"""


class Solution:
    def makeStringGood(self, s: str) -> int:
        from collections import Counter
        freq = Counter(s)
        counts = sorted(freq.values(), reverse=True)
        n = len(s)
        num_chars = len(counts)

        # Try each target frequency f from 0 to max(counts)
        # For each f, decide which chars to keep at f and which to eliminate
        best = n  # worst case: delete everything

        max_f = max(counts) if counts else 0

        for f in range(max_f + 1):
            # For each character, either keep at f (cost |c - f|) or remove (cost c)
            # But changes allow converting excess to deficit.
            # If we keep k characters at frequency f: total target = k * f.
            # Current total = n. Excess chars = n - k*f need to be deleted/changed.
            # Actually, let's think differently:
            # For each char, keeping costs: max(0, c - f) deletions + max(0, f - c) insertions
            # But deletions from one char can be changes to fill insertions of another.
            # So total cost = max(total_deletions, total_insertions) if we convert excess.
            # No: each deletion can become a change (1 op) instead of delete + insert (2 ops).
            # Cost = changes + remaining_deletes + remaining_inserts
            #       = min(deletes, inserts) + |deletes - inserts|
            #       = max(deletes, inserts)

            # But we also can choose to remove some chars entirely (set to 0) instead of f.
            # For a char with count c: keep at f costs |c-f|, remove costs c.
            # Choose remove if c < |c-f|, i.e., c < f - c, i.e., 2c < f, i.e., c < f/2.
            # But removed chars' counts go to "excess" pool too.

            # Try: for each subset of chars to keep (too expensive for 26 chars directly)
            # Greedy: sort chars. For target f, keep chars where cost(keep) <= cost(remove).
            # keep cost = |c - f|, remove cost = c. Keep if |c-f| <= c.
            # If c <= f: keep cost = f - c, remove cost = c. Keep if f - c <= c => f <= 2c => c >= f/2.
            # If c > f: keep cost = c - f, remove cost = c. Always keep (c-f < c).

            total_del = 0  # excess from kept chars + removed chars
            total_ins = 0  # deficit for kept chars

            for c in counts:
                if c >= f:
                    total_del += c - f
                elif c >= (f + 1) // 2:  # keep: deficit
                    total_ins += f - c
                else:  # remove: cheaper
                    total_del += c

            # Use changes: each change reduces both a delete and an insert
            changes = min(total_del, total_ins)
            cost = total_del + total_ins  # each change counts once already
            # Wait: delete costs 1, insert costs 1, change costs 1 (replaces 1 delete + 1 insert)
            # So cost = changes * 1 + (total_del - changes) * 1 + (total_ins - changes) * 1
            # = total_del + total_ins - changes = max(total_del, total_ins)
            cost = max(total_del, total_ins)
            best = min(best, cost)

        return best


# ---------- Tests ----------
def test():
    sol = Solution()

    # Example 1
    assert sol.makeStringGood("acab") == 1  # change c to b -> "abab" freq a=2, b=2

    # Example 2
    assert sol.makeStringGood("wddw") == 0  # already w=2, d=2

    # Example 3
    assert sol.makeStringGood("aaabc") == 2

    print("All tests passed!")


if __name__ == "__main__":
    test()
