"""
2999. Count the Number of Powerful Integers

Pattern: Digit DP
Approach: Count numbers in [1, finish] minus [1, start-1] that end with suffix s
    and have all digits <= limit. Standard digit DP with suffix constraint.
Time Complexity: O(n * 10) where n = number of digits
Space Complexity: O(n)
"""

def numberOfPowerfulInt(start, finish, limit, s):
    def count(num):
        """Count powerful integers in [1, num]"""
        num_str = str(num)
        n = len(num_str)
        sn = len(s)

        if n < sn:
            return 0

        prefix_len = n - sn  # number of "free" digits before suffix

        # Check if number formed by just the suffix <= num
        # We need to count numbers of form [d1 d2 ... d_{prefix_len}][s]
        # where each d_i <= limit, and the whole number <= num

        # Process digit by digit, tracking if we're still tight with num
        result = 0
        tight = True

        for i in range(prefix_len):
            d = int(num_str[i])
            if tight:
                # Digits we can freely place: 0 to min(d-1, limit)
                free_max = min(d - 1, limit)
                if free_max >= 0:
                    # Each of these gives (limit+1)^(remaining free positions) combinations
                    remaining = prefix_len - i - 1
                    result += (free_max + 1) * ((limit + 1) ** remaining)

                if d > limit:
                    tight = False  # can't match this digit, no more tight paths
            # If not tight, all remaining free digits handled above via prior iterations

        if not tight:
            return result

        # All prefix digits matched (tight). Check if suffix <= num's suffix
        num_suffix = num_str[prefix_len:]
        if num_suffix >= s:
            result += 1

        return result

    return count(finish) - count(start - 1)


def test():
    assert numberOfPowerfulInt(1, 6000, 4, "124") == 5
    assert numberOfPowerfulInt(15, 215, 6, "10") == 2
    assert numberOfPowerfulInt(1000, 2000, 4, "3000") == 0
    print("All tests passed!")

test()
