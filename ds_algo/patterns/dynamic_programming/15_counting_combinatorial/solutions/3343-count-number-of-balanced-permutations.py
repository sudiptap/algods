"""
3343. Count Number of Balanced Permutations (Hard)

Pattern: 15_counting_combinatorial
- A permutation of digits of num is "balanced" if sum of digits at even indices
  equals sum at odd indices. Count balanced permutations.

Approach:
- Total digit sum S must be even (else answer = 0). Target per half = S/2.
- n digits, even_positions = ceil(n/2), odd_positions = floor(n/2).
- dp to choose which digits go to even positions: need exactly even_positions digits
  with sum = S/2.
- Count ways using dp[count][sum], then multiply by even_positions! * odd_positions!
  divided by repeated digit factorials on each side. Easier: count multiset selections.
- Group by digit frequency. dp[j][s] = ways to assign digits 0..cur to even positions
  using j slots and sum s. For digit d with freq f, choose t (0..min(f, remaining))
  to go to even: C(f, t) ways.
- Final answer = dp[even_pos][S/2] * even_pos! * odd_pos! / product(freq[d]!)
  Actually we handle this differently: the dp counts selections, then arrange.

Complexity:
- Time:  O(10 * even_pos * S/2 * max_freq)
- Space: O(even_pos * S/2)
"""

from math import factorial

MOD = 10**9 + 7


class Solution:
    def countBalancedPermutations(self, num: str) -> int:
        digits = [int(c) for c in num]
        n = len(digits)
        S = sum(digits)
        if S % 2:
            return 0

        half = S // 2
        even_pos = (n + 1) // 2  # positions 0,2,4,...
        odd_pos = n // 2

        # Count digit frequencies
        freq = [0] * 10
        for d in digits:
            freq[d] += 1

        # Precompute factorials and inverse factorials
        max_n = n + 1
        fact = [1] * (max_n + 1)
        for i in range(1, max_n + 1):
            fact[i] = fact[i - 1] * i % MOD
        inv_fact = [1] * (max_n + 1)
        inv_fact[max_n] = pow(fact[max_n], MOD - 2, MOD)
        for i in range(max_n - 1, -1, -1):
            inv_fact[i] = inv_fact[i + 1] * (i + 1) % MOD

        def comb(a, b):
            if b < 0 or b > a:
                return 0
            return fact[a] * inv_fact[b] % MOD * inv_fact[a - b] % MOD

        # dp[j][s] = ways to choose j digits for even positions with sum s
        dp = [[0] * (half + 1) for _ in range(even_pos + 1)]
        dp[0][0] = 1

        for d in range(10):
            f = freq[d]
            if f == 0:
                continue
            # Process in reverse to use each digit group once
            new_dp = [[0] * (half + 1) for _ in range(even_pos + 1)]
            for j in range(even_pos + 1):
                for s in range(half + 1):
                    if dp[j][s] == 0:
                        continue
                    # Choose t copies of digit d for even positions
                    for t in range(min(f, even_pos - j) + 1):
                        ns = s + d * t
                        if ns > half:
                            break
                        nj = j + t
                        new_dp[nj][ns] = (new_dp[nj][ns] + dp[j][s] * comb(f, t)) % MOD
            dp = new_dp

        ways = dp[even_pos][half]
        # Multiply by arrangements within even and odd positions
        # ways already accounts for which digits go where (multiset coefficient)
        # Now arrange: even_pos! ways for even positions, odd_pos! for odd
        # But we've overcounted by freq[d]! for each d... no, comb(f,t) already
        # distributes t to even and f-t to odd. Within each group, positions are
        # distinguishable, so multiply by even_pos! * odd_pos! / product of
        # (number of each digit in even)! * (number in odd)!.
        # But comb(f,t) = f!/(t!(f-t)!), so total = product C(f,t) gives us
        # the multinomial split. Then even_pos! / product(t_d!) * odd_pos! / product((f_d-t_d)!)
        # = even_pos! * odd_pos! * product(1/(t_d! * (f_d - t_d)!))
        # = even_pos! * odd_pos! / product(f_d!) * product(C(f_d, t_d))... hmm.
        # Actually: dp already has product of C(f_d, t_d).
        # Final arrangement = dp * even_pos! * odd_pos! / product(f_d!) * product(f_d!)
        # Wait, let me think again.
        # We choose t_d of f_d copies of digit d for even positions: product C(f_d, t_d) ways.
        # Then arrange the even_pos digits among even positions: even_pos! / product(t_d!)
        # And arrange odd_pos digits: odd_pos! / product((f_d - t_d)!)
        # But product C(f_d,t_d) * even_pos!/product(t_d!) * odd_pos!/product((f_d-t_d)!)
        # = product(f_d!/(t_d!(f_d-t_d)!)) * even_pos!/product(t_d!) * odd_pos!/product((f_d-t_d)!)
        # This gets complex. Simpler: dp counts the multinomial coefficient for selection.
        # The total permutations = even_pos! * odd_pos! * product(C(f_d, t_d)) / (product t_d! * product (f_d-t_d)!)... no.

        # Correct formula: total = sum over valid t_d assignments of:
        #   (even_pos! / product(t_d!)) * (odd_pos! / product((f_d-t_d)!))
        # = even_pos! * odd_pos! * sum of product(1/(t_d! * (f_d-t_d)!))
        # = even_pos! * odd_pos! / product(f_d!) * sum of product(C(f_d, t_d))
        # = even_pos! * odd_pos! / product(f_d!) * dp[even_pos][half]

        ans = ways * fact[even_pos] % MOD * fact[odd_pos] % MOD
        for d in range(10):
            ans = ans * inv_fact[freq[d]] % MOD

        return ans


# ---------- Tests ----------
def test():
    sol = Solution()

    # Example 1
    assert sol.countBalancedPermutations("123") == 2

    # Example 2
    assert sol.countBalancedPermutations("112") == 1

    # Example 3
    assert sol.countBalancedPermutations("12345") == 0  # sum=15, odd

    # All same digits
    assert sol.countBalancedPermutations("0000") == 1

    print("All tests passed!")


if __name__ == "__main__":
    test()
