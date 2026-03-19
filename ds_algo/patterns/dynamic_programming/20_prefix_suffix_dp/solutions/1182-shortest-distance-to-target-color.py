"""
1182. Shortest Distance to Target Color (Medium)

Pattern: 20_prefix_suffix_dp
- Precompute nearest occurrence of each color from left and right.

Approach:
- For each color c in {1, 2, 3}, build two arrays:
  - left[i] = distance to nearest occurrence of color c at or before index i (scanning left to right).
  - right[i] = distance to nearest occurrence of color c at or after index i (scanning right to left).
- For query (index, color), answer = min(left[color][index], right[color][index]).
  If neither exists, return -1.

Complexity:
- Time:  O(n + q) where n = len(colors), q = number of queries
- Space: O(n) for the precomputed arrays
"""

from typing import List


class Solution:
    def shortestDistanceColor(self, colors: List[int], queries: List[List[int]]) -> List[int]:
        n = len(colors)
        INF = float('inf')

        # nearest[c][i] = min distance to color c from index i
        # We'll compute left-pass and right-pass
        left = [[INF] * n for _ in range(4)]  # colors 1,2,3
        right = [[INF] * n for _ in range(4)]

        for c in range(1, 4):
            last = -INF
            for i in range(n):
                if colors[i] == c:
                    last = i
                left[c][i] = i - last  # will be INF-ish if never seen

            last = INF
            for i in range(n - 1, -1, -1):
                if colors[i] == c:
                    last = i
                right[c][i] = last - i

        result = []
        for idx, c in queries:
            d = min(left[c][idx], right[c][idx])
            result.append(d if d < INF else -1)

        return result


# ---------- Tests ----------
def test():
    sol = Solution()

    # Example 1
    colors = [1, 1, 2, 1, 3, 2, 2, 3, 3]
    queries = [[1, 3], [2, 2], [6, 1]]
    assert sol.shortestDistanceColor(colors, queries) == [3, 0, 3]

    # Example 2: color not present
    assert sol.shortestDistanceColor([1, 2], [[0, 3]]) == [-1]

    # Single element
    assert sol.shortestDistanceColor([2], [[0, 2]]) == [0]
    assert sol.shortestDistanceColor([2], [[0, 1]]) == [-1]

    print("All tests passed!")


if __name__ == "__main__":
    test()
