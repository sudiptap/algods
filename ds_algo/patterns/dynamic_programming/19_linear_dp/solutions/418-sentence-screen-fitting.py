"""
418. Sentence Screen Fitting (Medium)
https://leetcode.com/problems/sentence-screen-fitting/

Pattern: Linear DP

Given a rows x cols screen and a sentence as a list of non-empty words,
find how many times the sentence can be fitted on the screen.
Words cannot be split across lines. A word's row-position must not
exceed cols. Consecutive words on the same line are separated by a
single space.

Approach:
    Concatenate the sentence into one string "word1 word2 ... wordN "
    (with trailing space). Track a running position in this string.
    For each row, advance position by cols, then:
    - If the char at position is a space, we fit perfectly — advance past it.
    - Otherwise, backtrack to the start of the current word.
    Total fits = position // len(sentence_string).

Time:  O(rows * max_word_len)  — backtrack at most max_word_len per row
Space: O(total sentence length)
"""

from typing import List


class Solution:
    def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:
        """Return how many times sentence fits on a rows x cols screen."""
        s = " ".join(sentence) + " "
        n = len(s)
        pos = 0

        for _ in range(rows):
            pos += cols
            if s[pos % n] == " ":
                pos += 1
            else:
                while pos > 0 and s[(pos - 1) % n] != " ":
                    pos -= 1

        return pos // n


# ───────────────────────── tests ─────────────────────────

def test_example1():
    assert Solution().wordsTyping(["hello", "world"], 2, 8) == 1

def test_example2():
    assert Solution().wordsTyping(["a", "bcd", "e"], 3, 6) == 2

def test_example3():
    assert Solution().wordsTyping(["I", "had", "apple", "pie"], 4, 5) == 1

def test_single_word():
    # "hi " repeats: row of 5 fits "hi hi" -> 2 per row, 2 rows -> 4
    assert Solution().wordsTyping(["hi"], 2, 5) == 4

def test_exact_fit():
    assert Solution().wordsTyping(["ab", "cd"], 1, 5) == 1

def test_large_cols():
    assert Solution().wordsTyping(["a"], 1, 10) == 5


if __name__ == "__main__":
    import pytest
    pytest.main([__file__, "-v"])
