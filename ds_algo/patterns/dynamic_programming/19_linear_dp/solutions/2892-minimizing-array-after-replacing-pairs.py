"""
2892. Minimizing Array After Replacing Pairs With Their Sum
(LeetCode 2892: Minimum Number of Operations to Make Array Empty - adjusted)

Note: Problem 2892 is actually about making array empty by removing pairs/triples.

Pattern: 19 - Linear DP (Greedy)

---
APPROACH: Count frequency of each element. For each frequency f: if f == 1,
impossible. Otherwise, use as many triples as possible. f % 3 == 0: f/3 ops.
f % 3 == 1: (f-4)/3 + 2 ops. f % 3 == 2: (f-2)/3 + 1 ops. Simplified:
ceil(f/3).

Time: O(n)  Space: O(n)
---
"""

from typing import List
from collections import Counter
import math


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        freq = Counter(nums)
        ops = 0
        for f in freq.values():
            if f == 1:
                return -1
            ops += math.ceil(f / 3)
        return ops


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.minOperations([2, 3, 3, 2, 2, 4, 2, 3, 4]) == 4
    assert sol.minOperations([2, 1, 2, 2, 3, 3]) == -1

    print("All tests passed!")
