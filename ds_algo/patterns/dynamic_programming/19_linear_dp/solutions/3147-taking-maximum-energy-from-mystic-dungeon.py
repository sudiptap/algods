"""
3147. Taking Maximum Energy From the Mystic Dungeon

Pattern: Linear DP
Approach: Starting at position i, you collect energy[i], energy[i+k], energy[i+2k], ...
    This is a suffix sum with stride k. Compute from the end: for each starting
    position i, the total energy is energy[i] + dp[i+k]. Answer is max over all i.
Time Complexity: O(n)
Space Complexity: O(n)
"""

def maximumEnergy(energy, k):
    n = len(energy)
    dp = [0] * n
    # Process from end
    for i in range(n - 1, -1, -1):
        dp[i] = energy[i] + (dp[i + k] if i + k < n else 0)

    return max(dp)


def test():
    assert maximumEnergy([5, 2, -10, -5, 1], 3) == 3
    assert maximumEnergy([-2, -3, -1], 2) == -1
    assert maximumEnergy([10], 1) == 10
    print("All tests passed!")

test()
