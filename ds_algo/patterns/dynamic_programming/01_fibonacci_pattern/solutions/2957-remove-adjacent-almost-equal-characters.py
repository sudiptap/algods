"""
2957. Remove Adjacent Almost-Equal Characters

Pattern: Fibonacci Pattern
Approach: Greedy skip. Scan left to right. When two adjacent chars are "almost equal"
    (differ by at most 1 in ASCII), we must change one. Greedily change the right one
    and skip the next pair check (since we changed it to something safe).
Time Complexity: O(n)
Space Complexity: O(1)
"""

def removeAlmostEqualCharacters(word):
    ops = 0
    i = 1
    while i < len(word):
        if abs(ord(word[i]) - ord(word[i - 1])) <= 1:
            ops += 1
            i += 2  # skip next comparison since we changed word[i]
        else:
            i += 1
    return ops


def test():
    assert removeAlmostEqualCharacters("aaaaa") == 2
    assert removeAlmostEqualCharacters("abddez") == 2
    assert removeAlmostEqualCharacters("zyxyxyz") == 3
    assert removeAlmostEqualCharacters("a") == 0
    print("All tests passed!")

test()
