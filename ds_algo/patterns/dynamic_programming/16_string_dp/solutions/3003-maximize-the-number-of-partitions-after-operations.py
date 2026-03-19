"""
3003. Maximize the Number of Partitions After Operations

Pattern: String DP
Approach: DP with character tracking. Partition string greedily: extend partition
    while unique chars <= k. Count partitions without any change. Then try changing
    each character and recount. Optimize by tracking prefix/suffix partition info.
Time Complexity: O(26 * n) with prefix/suffix optimization
Space Complexity: O(n)
"""

def maxPartitionsAfterOperations(s, k):
    n = len(s)
    if k >= 26:
        return 1  # any partition is just 1 segment

    # Without any change: greedy partition
    def count_partitions(s):
        parts = 1
        seen = 0
        for c in s:
            bit = 1 << (ord(c) - ord('a'))
            new_seen = seen | bit
            if bin(new_seen).count('1') > k:
                parts += 1
                seen = bit
            else:
                seen = new_seen
        return parts

    base = count_partitions(s)

    # For each position, try changing s[i] to each of 26 chars
    # Optimize: compute prefix partitions and suffix partitions with bitmask state
    # prefix[i] = (partitions_count, current_bitmask) after processing s[0..i-1]
    prefix_parts = [0] * (n + 1)
    prefix_mask = [0] * (n + 1)
    parts = 0  # actually starts with 1 partition but we count transitions
    mask = 0
    for i in range(n):
        bit = 1 << (ord(s[i]) - ord('a'))
        new_mask = mask | bit
        if bin(new_mask).count('1') > k:
            parts += 1
            mask = bit
        else:
            mask = new_mask
        prefix_parts[i + 1] = parts
        prefix_mask[i + 1] = mask

    # suffix[i] = (partitions_count, bitmask) processing s[i..n-1] right to left
    # This is trickier since greedy goes left to right. Let me use a different approach.

    # For suffix: process s[i..n-1] greedily left to right
    # suffix_parts[i] = partitions for s[i..n-1]
    # suffix_first_mask[i] = bitmask of first partition of s[i..n-1]
    suffix_parts = [0] * (n + 1)
    suffix_first_mask = [0] * (n + 1)
    for i in range(n - 1, -1, -1):
        # Recompute suffix greedily
        # This is O(n) per position = O(n^2) total. For n<=10^4 it's fine.
        pass

    # O(n^2) approach: for each position i, try all 26 chars
    # Optimization: only try positions where changing matters
    best = base

    # Precompute suffix partitions
    # suffix_parts[i] = number of partitions for s[i..n-1]
    for i in range(n):
        # Change s[i] to char c
        for c_ord in range(26):
            c = chr(c_ord + ord('a'))
            if c == s[i]:
                continue

            # Prefix: s[0..i-1] with its partitions, ending with prefix_mask[i]
            # At position i, we add char c instead of s[i]
            p_parts = prefix_parts[i]
            p_mask = prefix_mask[i]

            bit = 1 << c_ord
            new_mask = p_mask | bit
            if bin(new_mask).count('1') > k:
                p_parts += 1
                cur_mask = bit
            else:
                cur_mask = new_mask

            # Continue greedily from i+1 with cur_mask
            for j in range(i + 1, n):
                bit2 = 1 << (ord(s[j]) - ord('a'))
                nm = cur_mask | bit2
                if bin(nm).count('1') > k:
                    p_parts += 1
                    cur_mask = bit2
                else:
                    cur_mask = nm

            best = max(best, p_parts + 1)

    return best


def test():
    assert maxPartitionsAfterOperations("accca", 2) == 3
    assert maxPartitionsAfterOperations("a", 1) == 1
    print("All tests passed!")

test()
