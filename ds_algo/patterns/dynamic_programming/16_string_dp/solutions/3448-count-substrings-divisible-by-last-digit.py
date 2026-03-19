"""
3448. Count Substrings Divisible By Last Digit
https://leetcode.com/problems/count-substrings-divisible-by-last-digit/

Pattern: 16 - String DP

---
APPROACH: For each ending digit d (1-9), maintain count of prefix remainders mod d.
- For each position j, the substring s[i..j] has value V. We need V % s[j] == 0.
- Let d = int(s[j]). If d == 0, skip (can't divide by 0).
- The numeric value of s[i..j] mod d depends on prefix sums mod d.
- V(i,j) = (prefix(j) - prefix(i-1) * 10^(j-i+1)) mod d.
- For each d in 1..9, track counts of prefix values mod d.
- Special cases for d=1 (always divisible), d=2,5 (only last digit matters),
  d=3,9 (digit sum), etc.

Actually simpler approach per digit d:
- For each d from 1-9, maintain cnt[r] = number of prefixes with (prefix_val mod d) == r.
- At position j with digit d_j = int(s[j]):
  If d_j != 0: need prefix(j) mod d_j == prefix(i-1)*10^(j-i+1) mod d_j
  This is complex. Use the standard approach:

For each ending position j with last digit d = int(s[j]) != 0:
- We need the number formed by s[i..j] to be divisible by d.
- Maintain for each possible divisor d (1-9), an array cnt[d][r] counting how many
  starting positions give remainder r when computing the substring value mod d.

Efficient approach: For each d from 1-9, maintain running prefix mod d with appropriate
power-of-10 adjustments.

Time: O(9 * n)  Space: O(9 * 9) = O(1)
---
"""


class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        ans = 0

        # For each divisor d from 1 to 9, maintain:
        # As we process position j, we track the number s[i..j] mod d for all i <= j.
        # s[i..j] mod d = (s[i..j-1] * 10 + s[j]) mod d  -- but this builds from left.
        # Actually, we build from left: val[i..j] = val[i..j-1]*10 + digit[j].
        # If we fix i and extend j, val mod d changes.
        # But we want to count over all i for each j.

        # Better: prefix number P(j) = s[0..j] as a number.
        # val(i,j) = P(j) - P(i-1) * 10^(j-i+1).
        # val(i,j) mod d = (P(j) - P(i-1)*10^(j-i+1)) mod d.
        # We need this == 0 and d = digit(j).

        # For each d, maintain cnt[r] = #{positions i where P(i)*10^(-i-1) mod d == r}
        # (using modular inverse of powers of 10).

        # For d in {1,2,3,4,5,6,7,8,9}:
        # 10 and d share factors for d=2,4,5,8. gcd(10,d)!=1 for those.
        # When gcd(10,d)!=1, modular inverse doesn't exist. Need different handling.

        # Simpler O(n*9) approach:
        # For each d from 1-9, maintain for each i: running value of s[i..j] mod d.
        # But that's O(n^2) total.

        # Actually, for d from 1-9, we only need d values of remainder (0..d-1).
        # Use: for a given d, suffix_mod[j] = number formed by s[j..current_end] mod d.
        # As we move current_end, suffix_mod values change.

        # Let me use the approach: for each j, for each d = digit(j):
        #   count how many i <= j satisfy val(i,j) % d == 0.

        # For d = 1: always true. Count = j+1 (if digit != 0).
        # For d = 2: val(i,j) % 2 = digit(j) % 2. Always 0 if digit is even. Count = j+1 or 0.
        # For d = 5: similar, digit must be 0 or 5. If 5, count = j+1.
        # For d = 3,9: digit sum mod d. Use prefix digit sums.
        # For d = 4: last two digits determine mod 4. val(i,j) mod 4 = s[j-1..j] mod 4 if j-i+1>=2, else s[j] mod 4.
        # For d = 6: need mod 2 and mod 3 both 0.
        # For d = 7: need actual prefix tracking.
        # For d = 8: last 3 digits.

        # General approach that works for all: for each d, maintain cnt[d][r].
        # P(j) mod d = (P(j-1)*10 + digit(j)) mod d.
        # val(i,j) mod d = 0 means P(j) mod d = P(i-1)*10^(j-i+1) mod d.
        # Let's define Q(i) = P(i) * inv(10)^(i+1) mod d (when gcd(10,d)=1).
        # Then val(i,j)=0 <=> Q(j) = Q(i-1) mod d. Count Q values.

        # For d where gcd(10,d)=1: d in {1,3,7,9}.
        # For d in {2,4,5,6,8}: handle specially.

        # Let's implement a general solution.

        # For each d, maintain cnt array of size d.
        # cnt[d] = [0]*d for d = 1..9

        # Method: for each d, compute prefix_mod and the power-adjusted prefix.

        # I'll use the following clean approach:
        # For each d from 1-9:
        #   Maintain running remainder rem[i] = value of s[0..i] mod d, computed incrementally.
        #   Also maintain pow10[i] = 10^(i+1) mod d.
        #   val(i,j) = P(j) - P(i-1)*10^(j-i+1) mod d = P(j) mod d - P(i-1)*pow10^(j-i+1) mod d.
        #   We need P(j) mod d == P(i-1)*10^(j-i+1) mod d.
        #   Let's define adjusted[i] = P(i) * modular_inverse(10^(i+1), d) mod d.
        #   If inv exists: val(i,j)=0 iff adjusted[j] == adjusted[i-1].
        #   For d with gcd(10,d)!=1, this doesn't work directly.

        # For simplicity and correctness, I'll use a slightly different approach:
        # For each position j with d = digit[j] > 0:
        #   Maintain a running array run_mod[d] where we track, for each start i,
        #   the value s[i..j] mod d. But instead of tracking all starts, we track
        #   the count of each remainder.
        #   When extending from j-1 to j: each existing substring s[i..j-1] with remainder r
        #   becomes s[i..j] with remainder (r*10 + digit[j]) % d.
        #   Plus the new single-char substring s[j..j] with value digit[j] % d.
        #   Count those with remainder 0.

        # This is O(n * sum(d for d=1..9)) = O(n * 45) = O(n).

        # We need to maintain cnt[d][r] for each d = 1..9.
        # cnt[d][r] = number of active substrings ending at current position with remainder r mod d.

        # When moving to position j:
        #   For each d from 1-9:
        #     new_cnt[d][(r*10 + digit[j]) % d] += cnt[d][r] for all r
        #     new_cnt[d][digit[j] % d] += 1  (single char substring)
        #   If d == digit[j] and d > 0:
        #     ans += new_cnt[d][0]

        cnt = [[0] * d for d in range(10)]  # cnt[0] unused

        for j in range(n):
            dj = int(s[j])
            # Update all cnt arrays
            for d in range(1, 10):
                new_cnt = [0] * d
                for r in range(d):
                    new_cnt[(r * 10 + dj) % d] += cnt[d][r]
                new_cnt[dj % d] += 1
                cnt[d] = new_cnt

            # Count substrings ending at j divisible by last digit
            if dj > 0:
                ans += cnt[dj][0]

        return ans


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.countSubstrings("12936") == 11
    assert sol.countSubstrings("5701283") == 18
    assert sol.countSubstrings("1") == 1

    print("Solution: all tests passed")
