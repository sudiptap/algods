"""
3337. Total Characters in String After Transformations II (Hard)

Pattern: 16_string_dp (Matrix exponentiation)
- Like 3335 but with custom transform rules: nums[i] tells how many next chars
  character i transforms into. After t transformations, return total length.

Approach:
- Build 26x26 transition matrix M where M[j][i] = 1 if char i produces char j
  (i.e., for char i, it produces chars (i+1)%26, (i+2)%26, ..., (i+nums[i])%26).
- Count vector v[i] = count of char i in s.
- After t steps: result = M^t * v. Answer = sum of result.
- Use matrix exponentiation for O(26^3 * log t).

Complexity:
- Time:  O(26^3 * log t + n)
- Space: O(26^2)
"""

from typing import List

MOD = 10**9 + 7


class Solution:
    def lengthAfterTransformations(self, s: str, t: int, nums: List[int]) -> int:
        # Build transition matrix
        M = [[0] * 26 for _ in range(26)]
        for i in range(26):
            for d in range(1, nums[i] + 1):
                j = (i + d) % 26
                M[j][i] = 1

        # Matrix exponentiation
        def mat_mul(A, B):
            n = len(A)
            C = [[0] * n for _ in range(n)]
            for i in range(n):
                for k in range(n):
                    if A[i][k] == 0:
                        continue
                    for j in range(n):
                        C[i][j] = (C[i][j] + A[i][k] * B[k][j]) % MOD
            return C

        def mat_pow(M, p):
            n = len(M)
            result = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
            while p:
                if p & 1:
                    result = mat_mul(result, M)
                M = mat_mul(M, M)
                p >>= 1
            return result

        Mt = mat_pow(M, t)

        # Count vector
        v = [0] * 26
        for c in s:
            v[ord(c) - ord('a')] += 1

        # Multiply Mt * v
        ans = 0
        for i in range(26):
            for j in range(26):
                ans = (ans + Mt[i][j] * v[j]) % MOD

        return ans


# ---------- Tests ----------
def test():
    sol = Solution()

    # With nums=[1]*26, each char just shifts (no splitting), length stays same
    assert sol.lengthAfterTransformations("abcyy", 2, [1] * 26) == 5

    # Example 2: nums=[2]*26, each char produces 2 next chars
    # "azbk" t=1: a->{b,c}, z->{a,b}, b->{c,d}, k->{l,m} -> length 8
    assert sol.lengthAfterTransformations("azbk", 1, [2] * 26) == 8

    print("All tests passed!")


if __name__ == "__main__":
    test()
