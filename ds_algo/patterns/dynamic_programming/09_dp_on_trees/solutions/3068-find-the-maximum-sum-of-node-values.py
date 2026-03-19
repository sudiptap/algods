"""
3068. Find the Maximum Sum of Node Values

Pattern: DP on Trees
Approach: XOR greedy. Each edge operation XORs both endpoints with k. Key insight:
    any even number of nodes can be XORed (since each edge op XORs 2 nodes).
    For each node, compute gain = (val ^ k) - val. Sort gains descending.
    Greedily take pairs of positive gains.
Time Complexity: O(n log n)
Space Complexity: O(n)
"""

def maximumValueSum(nums, k, edges):
    gains = [(n ^ k) - n for n in nums]
    gains.sort(reverse=True)
    total = sum(nums)

    i = 0
    while i + 1 < len(gains):
        pair_gain = gains[i] + gains[i + 1]
        if pair_gain > 0:
            total += pair_gain
            i += 2
        else:
            break

    return total


def test():
    assert maximumValueSum([1, 2, 1], 3, [[0, 1], [0, 2]]) == 6
    assert maximumValueSum([2, 3], 7, [[0, 1]]) == 9
    assert maximumValueSum([7, 7, 7, 7, 7, 7], 3, [[0,1],[0,2],[0,3],[0,4],[0,5]]) == 42
    print("All tests passed!")

test()
