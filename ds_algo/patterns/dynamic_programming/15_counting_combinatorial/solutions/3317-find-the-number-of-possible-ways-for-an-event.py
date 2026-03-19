"""
3317. Find the Number of Possible Ways for an Event (Hard)

Pattern: 15_counting_combinatorial
- n performers, x stages, y scores. Assign performers to stages (at least 1 per used stage),
  then each performer gets a score in [1,y]. Count total ways.

Approach:
- Choose k stages to use (1 <= k <= min(n, x)): C(x, k)
- Distribute n performers into k non-empty groups (Stirling numbers S(n, k)): S(n, k)
- Assign groups to stages (k! permutations, already counted by using ordered stages): k!
  Actually Stirling already gives unordered partition, so multiply by k! -> surjections.
  But we already chose which k stages, so multiply by k! for assignment.
  Wait: C(x,k) * k! * S(n,k) = P(x,k) * S(n,k). But S(n,k)*k! = surjection count.
  So total assignment = C(x,k) * S(n,k) * k!
- Each used stage independently gets a score from [1,y]: y^k.
- Total = sum over k of C(x,k) * S(n,k) * k! * y^k.

Complexity:
- Time:  O(n * x) for Stirling numbers
- Space: O(n * x)
"""

MOD = 10**9 + 7


class Solution:
    def numberOfWays(self, n: int, x: int, y: int) -> int:
        # Precompute Stirling numbers of the second kind S(n, k)
        # S(n, k) = k * S(n-1, k) + S(n-1, k-1)
        max_k = min(n, x)
        S = [[0] * (max_k + 1) for _ in range(n + 1)]
        S[0][0] = 1
        for i in range(1, n + 1):
            for k in range(1, min(i, max_k) + 1):
                S[i][k] = (k * S[i - 1][k] + S[i - 1][k - 1]) % MOD

        # Precompute C(x, k) and k!
        # C(x, k) = x! / (k! * (x-k)!)
        fact = [1] * (max(n, x) + 1)
        for i in range(1, len(fact)):
            fact[i] = fact[i - 1] * i % MOD
        inv_fact = [1] * len(fact)
        inv_fact[-1] = pow(fact[-1], MOD - 2, MOD)
        for i in range(len(inv_fact) - 2, -1, -1):
            inv_fact[i] = inv_fact[i + 1] * (i + 1) % MOD

        def comb(a, b):
            if b < 0 or b > a:
                return 0
            return fact[a] * inv_fact[b] % MOD * inv_fact[a - b] % MOD

        ans = 0
        for k in range(1, max_k + 1):
            y_k = pow(y, k, MOD)
            ways = comb(x, k) * fact[k] % MOD * S[n][k] % MOD * y_k % MOD
            ans = (ans + ways) % MOD

        return ans


# ---------- Tests ----------
def test():
    sol = Solution()

    # Example 1
    assert sol.numberOfWays(1, 1, 1) == 1

    # Example 2
    assert sol.numberOfWays(5, 2, 1) == 32

    # Example 3
    assert sol.numberOfWays(3, 3, 4) == 684

    print("All tests passed!")


if __name__ == "__main__":
    test()
