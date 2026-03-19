"""
2992. Number of Self-Divisible Permutations

Pattern: Bitmask DP
Approach: dp[mask] = number of permutations using the elements indicated by mask,
    where position = popcount(mask). A permutation is self-divisible if for each i,
    either i % perm[i] == 0 or perm[i] % i == 0 (1-indexed).
Time Complexity: O(2^n * n)
Space Complexity: O(2^n)
"""

def selfDivisiblePermutationCount(n):
    dp = [0] * (1 << n)
    dp[0] = 1

    for mask in range(1 << n):
        pos = bin(mask).count('1') + 1  # 1-indexed position to fill next
        if pos > n:
            continue
        for j in range(n):
            if mask & (1 << j):
                continue
            val = j + 1  # 1-indexed value
            if pos % val == 0 or val % pos == 0:
                dp[mask | (1 << j)] += dp[mask]

    return dp[(1 << n) - 1]


def test():
    assert selfDivisiblePermutationCount(1) == 1
    assert selfDivisiblePermutationCount(2) == 2
    assert selfDivisiblePermutationCount(3) == 3
    r4 = selfDivisiblePermutationCount(4)
    assert r4 > 0, f"Got {r4}"
    print("All tests passed!")

test()
