"""
3213. Construct String with Minimum Cost

Pattern: String DP
Approach: Build a trie from words with their costs. DP on target string: dp[i] =
    min cost to construct target[0..i-1]. For each position, traverse the trie
    matching target[i..] and update dp.
Time Complexity: O(n * L + W) where L = max word length, W = total words length
Space Complexity: O(W + n)
"""

def minimumCost(target, words, costs):
    n = len(target)

    # Build trie
    trie = {}
    for word, cost in zip(words, costs):
        node = trie
        for c in word:
            if c not in node:
                node[c] = {}
            node = node[c]
        node['$'] = min(node.get('$', float('inf')), cost)

    dp = [float('inf')] * (n + 1)
    dp[0] = 0

    for i in range(n):
        if dp[i] == float('inf'):
            continue
        node = trie
        for j in range(i, n):
            c = target[j]
            if c not in node:
                break
            node = node[c]
            if '$' in node:
                dp[j + 1] = min(dp[j + 1], dp[i] + node['$'])

    return dp[n] if dp[n] != float('inf') else -1


def test():
    assert minimumCost("abcdef", ["abdef","abc","d","def","ef"], [100,1,1,10,5]) == 7
    assert minimumCost("aaaa", ["z","zz","zzz"], [1,10,100]) == -1
    print("All tests passed!")

test()
