"""
2977. Minimum Cost to Convert String II

Pattern: String DP
Approach: Build a trie from original/changed strings. Run Dijkstra on the trie nodes
    to find shortest conversion costs. Then DP on the source string: dp[i] = min cost
    to convert source[0..i-1] to target[0..i-1].
Time Complexity: O(L * n + T^2 * log T) where L = total string lengths, T = trie size
Space Complexity: O(T^2 + n)
"""
import heapq
from collections import defaultdict

def minimumCost(source, target, original, changed, cost):
    n = len(source)

    # Map each unique string to an ID
    str_to_id = {}
    idx = 0
    for s in original + changed:
        if s not in str_to_id:
            str_to_id[s] = idx
            idx += 1

    # Build shortest path between string IDs
    dist = defaultdict(lambda: defaultdict(lambda: float('inf')))
    for i in range(len(original)):
        u, v, c = str_to_id[original[i]], str_to_id[changed[i]], cost[i]
        dist[u][v] = min(dist[u][v], c)

    # Floyd-Warshall (or Dijkstra from each node)
    nodes = list(range(idx))
    for k in nodes:
        for i in nodes:
            if dist[i][k] == float('inf'):
                continue
            for j in nodes:
                if dist[k][j] == float('inf'):
                    continue
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    # Group strings by length for efficient matching
    len_to_pairs = defaultdict(list)  # length -> list of (orig_id, changed_id, cost)
    all_lengths = set()
    for s in str_to_id:
        all_lengths.add(len(s))

    # DP on source string
    dp = [float('inf')] * (n + 1)
    dp[0] = 0

    for i in range(n):
        if dp[i] == float('inf'):
            continue
        if source[i] == target[i]:
            dp[i + 1] = min(dp[i + 1], dp[i])

        for l in all_lengths:
            if i + l > n:
                continue
            s_sub = source[i:i + l]
            t_sub = target[i:i + l]
            if s_sub == t_sub:
                dp[i + l] = min(dp[i + l], dp[i])
            elif s_sub in str_to_id and t_sub in str_to_id:
                u, v = str_to_id[s_sub], str_to_id[t_sub]
                if dist[u][v] < float('inf'):
                    dp[i + l] = min(dp[i + l], dp[i] + dist[u][v])

    return dp[n] if dp[n] != float('inf') else -1


def test():
    assert minimumCost("abcd", "acbe", ["a","b","c","c","e","d"],
                       ["b","c","b","e","b","e"], [2,5,5,1,2,20]) == 28
    assert minimumCost("abcdefgh", "acdeeghh", ["bcd","fgh","thh"],
                       ["cde","thh","ghh"], [1,3,5]) == 9
    assert minimumCost("abcdefgh", "addddddd", ["bcd","defgh"],
                       ["ddd","ddddd"], [100,1578]) == -1
    print("All tests passed!")

test()
