"""
466. Count The Repetitions (Hard)
https://leetcode.com/problems/count-the-repetitions/

Pattern: String DP

Define str = [s, n] as string s concatenated n times.
Given s1, n1, s2, n2, find max M such that [s2, M] is a subsequence
of [s1, n1], then return M // n2.

Approach:
    Simulate going through n1 copies of s1 and count how many full s2's
    we complete. After each s1 copy, record (s2_index, s2_count).
    If we see the same s2_index at the start of an s1 copy, we found a
    cycle and can extrapolate the remaining s2 counts.

Time:  O(n1 * len(s1))  or O(len(s1) * len(s2)) with cycle detection
Space: O(len(s2))
"""


class Solution:
    def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:
        """Return max integer M such that [s2, M*n2] is subseq of [s1, n1]."""
        if n1 == 0:
            return 0

        len1, len2 = len(s1), len(s2)
        # memo[j] = after starting s2 at index j and scanning one s1,
        #           what s2 index do we end at, and how many full s2 did we complete
        # But simpler: simulate with cycle detection.

        # s2_idx at the start of each s1 copy -> (s1_copy_index, s2_count_so_far)
        recall = {}
        s2_count = 0
        s2_idx = 0

        for i in range(n1):
            for ch in s1:
                if ch == s2[s2_idx]:
                    s2_idx += 1
                    if s2_idx == len2:
                        s2_idx = 0
                        s2_count += 1

            if s2_idx in recall:
                # Found cycle
                prev_i, prev_count = recall[s2_idx]
                cycle_len = i - prev_i
                cycle_count = s2_count - prev_count
                remaining = n1 - 1 - i
                full_cycles = remaining // cycle_len
                s2_count += full_cycles * cycle_count
                # Simulate the leftover
                leftover = remaining % cycle_len
                for _ in range(leftover):
                    for ch in s1:
                        if ch == s2[s2_idx]:
                            s2_idx += 1
                            if s2_idx == len2:
                                s2_idx = 0
                                s2_count += 1
                return s2_count // n2
            else:
                recall[s2_idx] = (i, s2_count)

        return s2_count // n2


# ───────────────────────── tests ─────────────────────────

def test_example1():
    assert Solution().getMaxRepetitions("acb", 4, "ab", 2) == 2

def test_example2():
    assert Solution().getMaxRepetitions("acb", 1, "acb", 1) == 1

def test_no_match():
    assert Solution().getMaxRepetitions("aaa", 3, "b", 1) == 0

def test_single_char():
    assert Solution().getMaxRepetitions("a", 6, "a", 2) == 3

def test_n1_zero():
    assert Solution().getMaxRepetitions("abc", 0, "ab", 1) == 0

def test_large_n2():
    assert Solution().getMaxRepetitions("ab", 4, "ab", 5) == 0


if __name__ == "__main__":
    import pytest
    pytest.main([__file__, "-v"])
