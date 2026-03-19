"""
3144. Minimum Substring Partition of Equal Character Frequency

Pattern: String DP
Approach: dp[i] = min partitions for s[0..i-1]. For each i, try all j < i and
    check if s[j..i-1] has all characters with equal frequency. Use frequency
    counting to check balanced condition.
Time Complexity: O(n^2 * 26)
Space Complexity: O(n)
"""

def minimumSubstringsInPartition(s):
    n = len(s)
    dp = [float('inf')] * (n + 1)
    dp[0] = 0

    for i in range(1, n + 1):
        freq = [0] * 26
        for j in range(i, 0, -1):
            freq[ord(s[j - 1]) - ord('a')] += 1
            # Check if all non-zero frequencies are equal
            vals = [f for f in freq if f > 0]
            if len(set(vals)) == 1:
                dp[i] = min(dp[i], dp[j - 1] + 1)

    return dp[n]


def test():
    assert minimumSubstringsInPartition("fabccddg") == 3
    assert minimumSubstringsInPartition("abababaccddb") == 2
    assert minimumSubstringsInPartition("aaa") == 1
    print("All tests passed!")

test()
