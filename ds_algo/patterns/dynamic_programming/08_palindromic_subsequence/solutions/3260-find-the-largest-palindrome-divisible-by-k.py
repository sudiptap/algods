"""
3260. Find the Largest Almost-Good Palindrome Divisible by K

Pattern: Palindromic Subsequence
Approach: Digit DP to build a palindrome of length n divisible by k. Build from
    outside in, choosing digits greedily (largest first). Track remainder mod k.
    For each position pair (i, n-1-i), try digits 9 down to 0, and track the
    contribution to the remainder.
Time Complexity: O(n * k * 10)
Space Complexity: O(n * k)
"""

def largestPalindrome(n, k):
    # Build palindrome digit by digit from outside in
    # For position i and its mirror n-1-i, both get digit d
    # Contribution to number mod k: d * (10^i + 10^(n-1-i)) mod k
    # If n is odd and i == n//2, contribution is d * 10^i mod k

    pows = [1] * n
    for i in range(1, n):
        pows[i] = (pows[i-1] * 10) % k

    result = ['0'] * n
    rem = 0  # current remainder

    half = (n + 1) // 2
    for pos in range(half):
        mirror = n - 1 - pos
        for d in range(9, -1, -1):
            if pos == mirror:  # middle of odd-length
                contrib = (d * pows[pos]) % k
            else:
                contrib = (d * (pows[pos] + pows[mirror])) % k
            new_rem = (rem + contrib) % k

            # Check if remaining positions can fix the remainder
            # Remaining positions: pos+1 to half-1
            # Each can contribute 0-9 * their factor
            # We need (k - new_rem) % k to be achievable
            # Greedy: if there are remaining positions, any remainder is achievable
            # (since we can set digits 0-9 freely, and gcd considerations)
            # Actually not always true. But for most k values, with enough
            # remaining positions, it works. We use backtracking-like greedy.

            remaining_positions = half - pos - 1
            if remaining_positions > 0 or new_rem == 0:
                if remaining_positions > 0 or (remaining_positions == 0 and new_rem == 0):
                    result[pos] = str(d)
                    result[mirror] = str(d)
                    rem = new_rem
                    break

    # If remainder != 0, we need to fix it. This shouldn't happen with proper greedy.
    # But to be safe, let's do a pass from inside out adjusting digits.
    # Actually, let me use proper DP/backtracking.

    # Better approach: use DP
    result2 = [0] * n

    def solve():
        # dp approach: for each position from outside in, track remainder
        # At each step, try largest digit first
        # Use memoization on (position, remainder)
        from functools import lru_cache

        @lru_cache(maxsize=None)
        def dp(pos, rem):
            """Returns True if we can complete from position pos with current remainder rem."""
            if pos >= half:
                return rem == 0

            mirror = n - 1 - pos
            for d in range(9, -1, -1):
                if pos == 0 and d == 0 and n > 1:
                    continue  # no leading zeros (but palindrome of length > 1 needs d >= 1)
                if pos == mirror:
                    contrib = (d * pows[pos]) % k
                else:
                    contrib = (d * (pows[pos] + pows[mirror])) % k
                new_rem = (rem + contrib) % k
                if dp(pos + 1, new_rem):
                    return True
            return False

        def reconstruct(pos, rem):
            if pos >= half:
                return
            mirror = n - 1 - pos
            for d in range(9, -1, -1):
                if pos == 0 and d == 0 and n > 1:
                    continue
                if pos == mirror:
                    contrib = (d * pows[pos]) % k
                else:
                    contrib = (d * (pows[pos] + pows[mirror])) % k
                new_rem = (rem + contrib) % k
                if dp(pos + 1, new_rem):
                    result2[pos] = d
                    result2[mirror] = d
                    reconstruct(pos + 1, new_rem)
                    return

        if dp(0, 0):
            reconstruct(0, 0)
            return ''.join(map(str, result2))
        return ""

    return solve()


def test():
    assert largestPalindrome(3, 5) == "595"
    assert largestPalindrome(1, 4) == "8"
    assert largestPalindrome(5, 6) == "89898"
    assert largestPalindrome(2, 1) == "99"
    print("All tests passed!")

test()
