"""
3534. Path Existence Queries in a Graph II
https://leetcode.com/problems/path-existence-queries-in-a-graph-ii/

Pattern: 19 - Linear DP (Binary lifting)

---
APPROACH: Sort nodes by value, build binary lifting jump table.
- Edge between i,j iff |nums[i] - nums[j]| <= maxDiff.
- Sort nodes by value. jump[i][0] = farthest reachable index from i in one hop.
- Binary lift: jump[i][k] = jump[jump[i][k-1]][k-1].
- For each query, convert to sorted indices and find min jumps.

Time: O((n + q) * log n)  Space: O(n * log n)
---
"""

from typing import List
import math


class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:
        sorted_pairs = sorted((num, i) for i, num in enumerate(nums))
        sorted_nums = [num for num, _ in sorted_pairs]
        index_map = {orig_idx: sorted_idx for sorted_idx, (_, orig_idx) in enumerate(sorted_pairs)}

        max_level = n.bit_length() + 1
        jump = [[0] * max_level for _ in range(n)]

        right = 0
        for i in range(n):
            right = max(right, i)
            while right + 1 < n and sorted_nums[right + 1] - sorted_nums[i] <= maxDiff:
                right += 1
            jump[i][0] = right

        for level in range(1, max_level):
            for i in range(n):
                jump[i][level] = jump[jump[i][level - 1]][level - 1]

        def min_jumps(start, end, level):
            if start == end:
                return 0
            if jump[start][0] >= end:
                return 1
            if jump[start][level] < end:
                return math.inf
            j = level
            for j in range(level, -1, -1):
                if jump[start][j] < end:
                    break
            return (1 << j) + min_jumps(jump[start][j], end, j)

        def min_dist(u, v):
            u_idx = index_map[u]
            v_idx = index_map[v]
            start = min(u_idx, v_idx)
            end = max(u_idx, v_idx)
            res = min_jumps(start, end, max_level - 1)
            return res if res < math.inf else -1

        return [min_dist(u, v) for u, v in queries]


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    # nodes: 0->1, 1->8, 2->3, 3->4, 4->2. sorted: [1,2,3,4,8] = nodes [0,4,2,3,1]
    # maxDiff=3. From sorted: 1 can reach up to 4 (diff 3). 2 can reach 4. 3 can reach 4.
    # Query (0,3): node0=val1, node3=val4. sorted: 0->0, 3->3. jump[0][0]= farthest <=1+3=4, idx 3. 1 hop.
    # Query (2,4): node2=val3, node4=val2. sorted: 2->2, 4->1. start=1, end=2. jump[1][0]>=2? yes. 1 hop.
    # Query (0,1): node0=val1, node1=val8. sorted: 0->0, 1->4. start=0, end=4.
    #   jump[0][0]=3 (can reach val4). jump[3][0]= farthest from val4: 4+3=7, val8=8>7. So jump[3][0]=3.
    #   Can't reach idx 4. Answer = -1.

    r = sol.pathExistenceQueries(5, [1, 8, 3, 4, 2], 3, [[0, 3], [2, 4], [0, 1]])
    assert r == [1, 1, -1], f"Got {r}"

    print("Solution: all tests passed")
