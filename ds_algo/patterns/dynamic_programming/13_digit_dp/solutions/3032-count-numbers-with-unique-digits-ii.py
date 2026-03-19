"""
3032. Count Numbers With Unique Digits II

Pattern: Digit DP
Approach: Simple counting. Count numbers in [a, b] where all digits are unique.
    Since constraints are small (a, b <= 1000), iterate and check each number.
Time Complexity: O((b - a) * d) where d = number of digits
Space Complexity: O(1)
"""

def numberCount(a, b):
    count = 0
    for num in range(a, b + 1):
        digits = str(num)
        if len(set(digits)) == len(digits):
            count += 1
    return count


def test():
    assert numberCount(1, 20) == 19  # only 11 has repeated digits
    assert numberCount(1, 5) == 5
    assert numberCount(1, 100) == 90  # 11,22,...,99 = 9 numbers with repeats
    print("All tests passed!")

test()
