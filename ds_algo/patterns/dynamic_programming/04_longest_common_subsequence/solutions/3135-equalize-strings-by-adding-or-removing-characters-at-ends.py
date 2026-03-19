"""
3135. Equalize Strings by Adding or Removing Characters at Ends

Pattern: Longest Common Subsequence
Approach: LCS variant. The minimum operations to make two strings equal by adding
    or removing characters is len(s1) + len(s2) - 2 * LCS(s1, s2).
    Actually this problem is about longest common substring (contiguous), not subsequence.
    Find longest common substring, answer = len(s1) + len(s2) - 2 * LCS_contiguous.
Time Complexity: O(n * m)
Space Complexity: O(min(n, m))
"""

def minOperations(initial, target):
    n, m = len(initial), len(target)
    # Longest common substring
    best = 0
    prev = [0] * (m + 1)
    for i in range(1, n + 1):
        curr = [0] * (m + 1)
        for j in range(1, m + 1):
            if initial[i - 1] == target[j - 1]:
                curr[j] = prev[j - 1] + 1
                best = max(best, curr[j])
        prev = curr

    return n + m - 2 * best


def test():
    # "abcde" len=5, "cdef" len=4, longest common substring = "cde" (len 3)
    # ops = 5 + 4 - 2*3 = 3
    assert minOperations("abcde", "cdef") == 3
    assert minOperations("abc", "abc") == 0
    assert minOperations("a", "b") == 2
    print("All tests passed!")

test()
