"""
3811. Number of Alternating XOR Partitions
https://leetcode.com/problems/number-of-alternating-xor-partitions/

Pattern: 19 - Linear DP

---
APPROACH: Prefix XOR with DP on two hash maps
- Partition nums into contiguous blocks b1, b2, ... where
  XOR(b1)=target1, XOR(b2)=target2, XOR(b3)=target1, ...
- Use prefix XOR. XOR of block [l..r] = prefix[r+1] ^ prefix[l].
- cnt1[x]: number of ways a valid partition ending with target1 has
  prefix XOR = x after the last block.
- cnt2[x]: similar for ending with target2.
- For a new block ending at i with prefix XOR = pre:
  - Block matches target1 if pre ^ x = target1 for some previous prefix x,
    and the partition before x ended with target2 (so cnt2[pre^target1]).
  - Block matches target2 if pre ^ x = target2, using cnt1[pre^target2].

Time: O(n)  Space: O(n)
---
"""

from typing import List
from collections import defaultdict


class Solution:
    def alternatingXOR(self, nums: List[int], target1: int, target2: int) -> int:
        MOD = 10**9 + 7
        cnt1 = defaultdict(int)  # ways ending with target1 at prefix value
        cnt2 = defaultdict(int)  # ways ending with target2 at prefix value
        cnt2[0] = 1  # empty partition = "ended with target2" so next block should be target1

        pre = 0
        ans = 0
        for x in nums:
            pre ^= x
            # Try to form a new block ending here with target1
            a = cnt2[pre ^ target1]
            # Try to form a new block ending here with target2
            b = cnt1[pre ^ target2]
            ans = (a + b) % MOD  # current endpoint value
            cnt1[pre] = (cnt1[pre] + a) % MOD
            cnt2[pre] = (cnt2[pre] + b) % MOD

        # Answer: number of valid complete partitions
        # These are partitions that cover the entire array.
        # The last block can end with target1 (odd number of blocks)
        # or target2 (even number of blocks).
        # "ans" after the last element is the total valid partitions.
        # But we need just partitions ending with target1 OR target2?
        # Actually the problem says "alternating starting with target1".
        # A single block is valid if XOR = target1.
        # Two blocks: b1 XOR=target1, b2 XOR=target2.
        # We need the full partition to end properly.
        # The variable "a" tracks new partitions ending with target1.
        # So the answer should be the total a accumulated at the end.

        # Let me reconsider. After processing all elements:
        # cnt1[pre_final] = total ways to partition [0..n-1] ending with target1 block
        # But "ans" was overwritten each step. Let me just return cnt1[pre] for
        # partitions ending with target1 (valid since any odd count of blocks ending
        # with target1 is valid), plus cnt2[pre] for even count ending with target2.
        # Wait: a valid partition alternates t1, t2, t1, t2, ... The problem says
        # "starting with target1". So valid partitions have 1 block (t1), 2 blocks
        # (t1,t2), 3 blocks (t1,t2,t1), etc.
        # Both odd-count (ending t1) and even-count (ending t2) are valid.

        # After all elements, total valid = cnt1[pre] + cnt2[pre] - initial
        # Actually cnt1[pre] = ways to partition entire array ending with t1 block
        # cnt2[pre] = ways ending with t2 block (but we subtract the initial cnt2[0]
        # which was our "seed"). Wait, cnt2[0] = 1 was the seed at prefix=0.
        # After processing, cnt2[pre] at pre=total_xor includes both the seed
        # and accumulated values. But the seed corresponds to the "empty previous
        # partition before the first block".

        # The answer = total valid partitions of the ENTIRE array.
        # A partition ending with t1: cnt1 accumulated at positions where
        # the block ended. The partition covers the full array only if the
        # last block ends at the last element.
        # So ans = a (from last iteration, which is cnt2[pre^t1] at the final pre)
        #        + b (from last iteration, cnt1[pre^t2] at the final pre)
        # Wait no, a+b at the last step gives total new partitions ending at
        # the last element, which is exactly what we want.

        return ans


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.alternatingXOR([2, 3, 1, 4], 1, 5) == 1
    assert sol.alternatingXOR([1, 0, 0], 1, 0) == 3
    assert sol.alternatingXOR([7], 1, 7) == 0
    assert sol.alternatingXOR([7], 7, 1) == 1  # single block [7] XOR=7=target1

    print("all tests passed")
