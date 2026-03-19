"""
3165. Maximum Sum of Subsequence With Non-Adjacent Elements

Pattern: Kadane's Pattern
Approach: Segment tree where each node stores 4 values: max sum given whether
    leftmost and rightmost elements of that segment are included or not.
    For each query, point-update and read the root's max.
Time Complexity: O(n + q * log(n))
Space Complexity: O(n)
"""

def maximumSumSubsequence(nums, queries):
    MOD = 10**9 + 7
    n = len(nums)
    seg = [None] * (4 * n)

    def make_node(val):
        v = max(val, 0)
        return (0, v, v, v)  # (ff, ft, tf, tt)

    def merge(L, R):
        # (ff, ft, tf, tt): first=left boundary taken?, second=right boundary taken?
        # Junction: L's right end and R's left end are adjacent => can't both be taken
        # L_right=free: L[0](ff), L[2](tf). L_right=taken: L[1](ft), L[3](tt)
        # R_left=free: R[0](ff), R[1](ft). R_left=taken: R[2](tf), R[3](tt)
        rff = max(L[0] + max(R[0], R[2]), L[1] + R[0])
        rft = max(L[0] + max(R[1], R[3]), L[1] + R[1])
        rtf = max(L[2] + max(R[0], R[2]), L[3] + R[0])
        rtt = max(L[2] + max(R[1], R[3]), L[3] + R[1])
        return (rff, rft, rtf, rtt)

    def build(node, lo, hi):
        if lo == hi:
            seg[node] = make_node(nums[lo])
            return
        mid = (lo + hi) // 2
        build(2*node, lo, mid)
        build(2*node+1, mid+1, hi)
        seg[node] = merge(seg[2*node], seg[2*node+1])

    def update(node, lo, hi, idx, val):
        if lo == hi:
            seg[node] = make_node(val)
            return
        mid = (lo + hi) // 2
        if idx <= mid:
            update(2*node, lo, mid, idx, val)
        else:
            update(2*node+1, mid+1, hi, idx, val)
        seg[node] = merge(seg[2*node], seg[2*node+1])

    build(1, 0, n - 1)
    ans = 0
    for pos, val in queries:
        update(1, 0, n - 1, pos, val)
        ans = (ans + max(seg[1])) % MOD
    return ans


def test():
    # [3,5,9] -> [3,-2,9]: max non-adj=12 -> [-3,-2,9]: max non-adj=9 -> 12+9=21
    assert maximumSumSubsequence([3, 5, 9], [[1, -2], [0, -3]]) == 21
    assert maximumSumSubsequence([0, -1], [[0, -5]]) == 0
    print("All tests passed!")

test()
