"""
3352. Count K-Reducible Numbers Less Than N (Hard)

Pattern: 13_digit_dp
- A number x is k-reducible if repeatedly replacing x with popcount(x) reaches 1
  in at most k steps. Given binary string n, count numbers in [1, n-1] that are k-reducible.

Approach:
- First, precompute steps[c] = number of steps to reduce c to 1 (for c = 1..len(n)).
  steps[1] = 0, steps[c] = 1 + steps[popcount(c)].
- Use digit DP on binary string n to count numbers < n with exactly c set bits,
  for each c where steps[c] < k (since the number itself needs 1 + steps[popcount] steps
  total... actually steps[c] counts from c, so a number with c bits needs 1 + steps[c]
  steps if c > 1, or 0 if the number is 1).
  Wait: the number x has popcount = c. One step: x -> c. Then steps[c] more steps.
  Total = 1 + steps[c]. We need total <= k, so steps[c] <= k - 1, i.e., steps[c] < k.
  But if x = 1, it's already 1 (0 steps), always valid.

- Digit DP: count numbers in [1, n-1] with exactly c set bits, for each valid c.

Complexity:
- Time:  O(len(n)^2) for digit DP
- Space: O(len(n)^2)
"""

MOD = 10**9 + 7


class Solution:
    def countKReducibleNumbers(self, s: str, k: int) -> int:
        n = len(s)

        # Precompute steps to reduce to 1
        max_bits = n + 1
        steps = [0] * (max_bits)
        # steps[1] = 0 (already 1)
        for c in range(2, max_bits):
            steps[c] = 1 + steps[bin(c).count('1')]

        # Valid bit counts: steps[c] + 1 <= k for c >= 2, or c == 1 (0 steps)
        # Actually for number x with popcount c:
        # If c == 1: x is a power of 2 or x=1, one step to reach 1 (x->1), so needs 1 step
        # Hmm wait: k-reducible means at most k operations. x=1 needs 0. x with popcount=1
        # and x != 1: x->1 in 1 step. x with popcount=c>1: x->c (1 step) then steps[c] more.
        # Total for popcount c: if c == 1, need 1 step (unless x=1, need 0).
        # steps[c] = steps to go from c to 1. For c=1, steps[1]=0.
        # Total for x: 1 + steps[popcount(x)] if x > 1, 0 if x == 1.
        # k-reducible: total <= k. So 1 + steps[popcount(x)] <= k, i.e. steps[popcount(x)] <= k-1.
        # For x=1: always valid (0 <= k, and k >= 1).

        valid_counts = set()
        for c in range(1, max_bits):
            if steps[c] <= k - 1:
                valid_counts.add(c)

        # Digit DP: count numbers with exactly c set bits that are < s (as binary)
        # dp[pos][count][tight]
        # We'll compute for each valid c separately, or all at once.
        # All at once: dp[tight][bits_so_far]
        # At each position, if tight, digit <= s[pos], else 0 or 1.

        ans = 0

        # dp[bits] = count of numbers, with tight constraint
        # Two arrays: tight and free
        tight = [0] * (n + 1)  # tight[bits] = count with exactly bits set bits, still tight
        free = [0] * (n + 1)   # free[bits] = count with exactly bits set bits, no longer tight

        tight[0] = 1  # start: 0 bits set, tight

        for i in range(n):
            new_tight = [0] * (n + 1)
            new_free = [0] * (n + 1)

            d = int(s[i])

            for b in range(n + 1):
                # From tight[b]
                if tight[b]:
                    if d == 1:
                        # Place 0: becomes free
                        new_free[b] = (new_free[b] + tight[b]) % MOD
                        # Place 1: stays tight
                        if b + 1 <= n:
                            new_tight[b + 1] = (new_tight[b + 1] + tight[b]) % MOD
                    else:  # d == 0
                        # Place 0: stays tight
                        new_tight[b] = (new_tight[b] + tight[b]) % MOD
                        # Can't place 1 (would exceed)

                # From free[b]
                if free[b]:
                    # Place 0
                    new_free[b] = (new_free[b] + free[b]) % MOD
                    # Place 1
                    if b + 1 <= n:
                        new_free[b + 1] = (new_free[b + 1] + free[b]) % MOD

            tight = new_tight
            free = new_free

        # Numbers < s: all free states + tight states (but tight = s itself, exclude)
        # We want numbers in [1, s-1]
        for c in valid_counts:
            if c <= n:
                ans = (ans + free[c]) % MOD
                # tight[c] represents exactly s, exclude it

        return ans


# ---------- Tests ----------
def test():
    sol = Solution()

    # Example 1
    assert sol.countKReducibleNumbers("111", 1) == 3  # 1,2,4 (popcount=1, 1 step)...
    # Numbers < 7 (binary 111) that are 1-reducible: needs at most 1 op.
    # 1: 0 ops. 2(10): 1 op. 3(11)->2->1: 2 ops. 4(100): 1 op. 5(101)->2->1: 2 ops. 6(110)->2->1: 2 ops.
    # So 1,2,4 -> 3 numbers. Correct!

    # Example 2: "110" = 6, numbers 1..5 all reach 1 in at most 2 steps
    assert sol.countKReducibleNumbers("110", 2) == 5

    # Example 3
    assert sol.countKReducibleNumbers("1", 1) == 0  # No numbers in [1,0]

    print("All tests passed!")


if __name__ == "__main__":
    test()
