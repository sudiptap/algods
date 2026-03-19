"""
3757. Number of Effective Subsequences
https://leetcode.com/problems/number-of-effective-subsequences/

Pattern: 15 - Counting / Combinatorial

---
APPROACH: Count by bit contributions
- Strength = OR of all elements. A subsequence is "effective" if removing
  it strictly decreases the OR of remaining elements.
- Equivalently: the remaining elements' OR must be < strength, meaning
  at least one bit in strength is NOT covered by remaining elements.
- Complement: count subsequences whose removal does NOT decrease OR
  (i.e., remaining elements still cover all bits), then subtract from total.
- Total subsequences = 2^n - 1 (non-empty).
- For each bit b in strength, find elements that are the ONLY contributor
  of that bit. If bit b has exactly one contributor, that element must
  stay in the remaining set. If bit b has >= 2 contributors, we're safe
  even if we remove some.
- Actually: a subsequence is "ineffective" if after removing it, every bit
  of strength is still covered. The "ineffective" count can be computed by
  identifying for each bit b, the set of elements that contribute bit b,
  and ensuring at least one remains.
- This is inclusion-exclusion on bits. Let's think differently:
  For each bit b in strength, let S_b = set of elements with bit b set.
  An ineffective subsequence = one where for every bit b, at least one
  element of S_b is NOT removed.
  Effective = total - ineffective - empty (but empty is excluded already).

- For each bit b, all |S_b| elements being removed would kill that bit.
  We need: NOT (all of S_b removed) for every b simultaneously.
  Ineffective subsequences: those not removing all of any S_b.

- Key insight: group elements by which bits of strength they contribute.
  Use bitmask of bits of strength each element has.
  For elements with unique bits, they can't all be removed.

- Simpler approach: For each bit position b in strength, classify it as
  "critical" if only 1 element has it, or "non-critical" otherwise.
  Critical elements must remain. The rest can be freely removed.
  But this oversimplifies with overlapping bits.

- Better: Brute-force for small cases, or use the fact that strength
  has at most 20 bits. Use inclusion-exclusion.

Time: O(n * B + 2^B * B) where B = 20 bits
Space: O(2^B)
---
"""

from typing import List
from collections import Counter


class Solution:
    def numberOfEffectiveSubsequences(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        strength = 0
        for x in nums:
            strength |= x

        if strength == 0:
            return 0

        # Identify which bits are in strength
        bits = []
        for b in range(20):
            if strength & (1 << b):
                bits.append(b)
        B = len(bits)

        # For each element, compute its mask relative to strength's bits
        # mask[i] = which of the B bits does nums[i] contribute
        # Count elements by their mask
        mask_count = Counter()
        for x in nums:
            m = 0
            for idx, b in enumerate(bits):
                if x & (1 << b):
                    m |= (1 << idx)
            mask_count[m] += 1

        # Count "ineffective" subsequences: those whose complement (remaining)
        # covers all B bits of strength.
        # A subsequence to remove: S. Remaining: nums \ S.
        # Remaining covers all bits iff for each bit b, at least one element
        # with bit b is NOT in S.
        # Equivalently: S does NOT contain all elements of any critical set.

        # Using inclusion-exclusion on which bits are "killed":
        # Let f(T) = number of subsequences that remove ALL elements contributing
        # to ALL bits in T. This means all elements with ANY bit in T must be removed.
        # f(T) = 2^(count of elements with no bit in T) * 1 (all elements with some bit in T must be removed... wait no).

        # Let me reconsider. For a set of bits T:
        # "All bits in T are killed" means for each b in T, all elements with bit b are removed.
        # The set of elements that must be removed = union of S_b for b in T.
        # Let U(T) = count of elements that have at least one bit in T.
        # These elements MUST all be removed.
        # The remaining elements (without any bit in T) can be freely removed or not.
        # So the number of subsequences that kill all bits in T:
        #   = 2^(n - U(T))  (any subset of the non-T-contributing elements)
        # But we also include the U(T) elements in our subsequence (they're all removed).
        # So the subsequence is: all U(T) elements + any subset of the rest.
        # Number = 2^(n - U(T))

        # By inclusion-exclusion:
        # Number of subsequences that kill AT LEAST ONE bit =
        #   sum_{T != empty, T subset of bits} (-1)^(|T|+1) * 2^(n - U(T))
        # These are the "effective" subsequences (plus maybe empty set adjustments).

        # But we want all NON-EMPTY subsequences that kill at least one bit.
        # The empty subsequence doesn't kill any bit, so it's fine.

        # effective_count = sum over non-empty T subsets of strength-bits:
        #   (-1)^(|T|+1) * 2^(n - U(T))
        # But we need to subtract the empty subsequence if it's counted.
        # When T has some elements, 2^(n-U(T)) includes the empty subset of
        # non-T elements (but the T elements are always included). So the
        # subsequence is never empty (as long as U(T) > 0, which it is since
        # T is non-empty and each bit in strength has at least one contributor).

        # Wait, we need to be more careful. Let me reconsider.
        # S = subsequence to remove. S is effective if OR(nums\S) < strength.
        # We want to count effective non-empty S.
        #
        # killed_bits(S) = bits b such that all elements with bit b are in S.
        # S is effective iff killed_bits(S) is non-empty.
        #
        # By IE: |{S non-empty : killed_bits(S) non-empty}|
        #   = |{S non-empty}| - |{S non-empty : killed_bits(S) = empty}|
        #   = (2^n - 1) - |{S : remaining covers all bits}| + |{empty set}| if empty covers nothing
        #   Hmm, empty set S means remaining = nums, which covers all bits. So empty is "ineffective".
        #   |{S non-empty and ineffective}| = |{S : remaining covers all bits}| - 1 (exclude empty)
        #   effective = (2^n - 1) - (|{S : remaining covers all bits}| - 1)
        #             = 2^n - |{S : remaining covers all bits}|

        # |{S : remaining covers all bits}| by IE on bits NOT covered:
        # = sum over T subset of bits: (-1)^|T| * 2^(n - U(T))
        # where U(T) = count of elements with at least one bit in T.
        # (T = set of bits that are definitely killed by removing all their contributors)

        # Wait, that's the standard IE for "remaining covers all bits":
        # = sum_{T subset of bits} (-1)^|T| * (number of S where all bits in T are killed)
        # = sum_{T} (-1)^|T| * 2^(n - U(T))
        # where U(T) = |elements that have at least one bit in T|

        # Actually no. For a given T, "all bits in T are killed" means
        # every element contributing to any bit in T is in S.
        # Those elements are forced into S. The rest can be chosen freely.
        # Count of such S = 2^(n - U(T)).
        # And the IE for "at least one bit killed" is:
        # sum_{non-empty T} (-1)^(|T|-1) * 2^(n-U(T))

        # So "remaining covers all bits" = sum_{T} (-1)^|T| * 2^(n-U(T))
        # where T ranges over ALL subsets including empty (empty gives 2^n).

        # effective = 2^n - sum_{T} (-1)^|T| * 2^(n-U(T))
        #           = sum_{non-empty T} (-1)^(|T|-1) * 2^(n-U(T))
        #           = sum_{non-empty T} (-1)^(|T|+1) * 2^(n-U(T))

        # Compute U(T) for each T subset of bits.
        # B can be up to 20, so 2^20 = 10^6 subsets. For each, need U(T).
        # U(T) = n - count of elements with no bit in T.

        # Precompute: for each bitmask m, count of elements with that mask.
        # Then for a given T, elements with no bit in T have mask & T == 0.
        # Count of such elements = sum over m with m & T == 0 of mask_count[m].

        # Can precompute this with SOS (Sum over Subsets) DP.
        # Or just iterate since B <= 20.

        # SOS: Let f[T] = count of elements whose mask is a subset of complement(T).
        # f[T] = sum_{m & T == 0} mask_count[m] = sum_{m subset of ~T} mask_count[m]
        # This is the "subset sum" transform of mask_count over the complement.

        # Simpler: precompute cnt[T] = number of elements with mask exactly T.
        # Then f[T] = sum_{S subset of complement_full(T)} cnt[S]
        # where complement_full means complement within the B-bit universe.

        # Use zeta/mobius transform.

        total_masks = 1 << B
        cnt = [0] * total_masks
        for m, c in mask_count.items():
            cnt[m] += c

        # f[T] = count of elements with no overlap with T
        # = sum_{m : m & T == 0} cnt[m]
        # = subset sum of cnt over complement of T

        # Compute via complement: let g[S] = sum_{m subset of S} cnt[m]
        # Then f[T] = g[complement(T)]
        # g can be computed with SOS DP.
        g = cnt[:]
        for b in range(B):
            for mask in range(total_masks):
                if mask & (1 << b):
                    g[mask] += g[mask ^ (1 << b)]

        # f[T] = g[complement(T) & (total_masks - 1)]
        # U(T) = n - f[T]
        # 2^(n-U(T)) = 2^f[T]

        # Precompute powers of 2
        pow2 = [1] * (n + 1)
        for i in range(1, n + 1):
            pow2[i] = pow2[i - 1] * 2 % MOD

        ans = 0
        full = total_masks - 1
        for T in range(1, total_masks):
            popcount = bin(T).count('1')
            comp = full ^ T
            no_overlap = g[comp]
            sign = 1 if popcount % 2 == 1 else -1
            ans = (ans + sign * pow2[no_overlap]) % MOD

        return ans % MOD


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.numberOfEffectiveSubsequences([1, 2, 3]) == 3
    assert sol.numberOfEffectiveSubsequences([7, 4, 6]) == 4
    assert sol.numberOfEffectiveSubsequences([8, 8]) == 1
    assert sol.numberOfEffectiveSubsequences([2, 2, 1]) == 5

    print("all tests passed")
