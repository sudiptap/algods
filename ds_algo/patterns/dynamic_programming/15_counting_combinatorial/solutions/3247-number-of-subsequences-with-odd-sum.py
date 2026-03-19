"""
3247. Number of Subsequences with Odd Sum

Pattern: Counting / Combinatorial
Approach: Count odd and even numbers. Any subsequence with odd sum must have an
    odd count of odd numbers. Total subsequences with odd sum = 2^(n-1) when there's
    at least one odd number. Otherwise 0.
Time Complexity: O(n)
Space Complexity: O(1)
"""

def subsequenceCount(nums):
    MOD = 10**9 + 7
    n = len(nums)
    odd_count = sum(1 for x in nums if x % 2 == 1)

    if odd_count == 0:
        return 0

    # With at least one odd number, exactly half of all non-empty subsequences
    # have odd sum = (2^n - 0) / 2 = 2^(n-1)
    # But we need to be more careful. Let even_count = n - odd_count
    # Number of ways to pick odd count of odd numbers from odd_count: 2^(odd_count-1)
    # Number of ways to pick any subset of even numbers: 2^even_count
    # Total = 2^(odd_count-1) * 2^even_count = 2^(n-1)
    return pow(2, n - 1, MOD)


def test():
    assert subsequenceCount([1, 1, 1]) == 4
    assert subsequenceCount([1, 2, 3]) == 4
    assert subsequenceCount([2, 4]) == 0
    print("All tests passed!")

test()
