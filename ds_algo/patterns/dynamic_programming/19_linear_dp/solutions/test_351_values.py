"""Discover actual values for 351 tests."""

class Solution:
    def numberOfPatterns(self, m, n):
        skip = [[0] * 10 for _ in range(10)]
        skip[1][3] = skip[3][1] = 2
        skip[1][7] = skip[7][1] = 4
        skip[3][9] = skip[9][3] = 6
        skip[7][9] = skip[9][7] = 8
        skip[1][9] = skip[9][1] = 5
        skip[3][7] = skip[7][3] = 5
        skip[2][8] = skip[8][2] = 5
        skip[4][6] = skip[6][4] = 5
        visited = [False] * 10
        def dfs(cur, remaining):
            if remaining == 0:
                return 1
            visited[cur] = True
            count = 0
            for nxt in range(1, 10):
                mid = skip[cur][nxt]
                if not visited[nxt] and (mid == 0 or visited[mid]):
                    count += dfs(nxt, remaining - 1)
            visited[cur] = False
            return count
        total = 0
        for length in range(m, n + 1):
            total += dfs(1, length - 1) * 4
            total += dfs(2, length - 1) * 4
            total += dfs(5, length - 1)
        return total

s = Solution()
for i in range(1, 10):
    print(f"length {i}: {s.numberOfPatterns(i, i)}")
print(f"1-9 total: {s.numberOfPatterns(1, 9)}")
print(f"1-2 total: {s.numberOfPatterns(1, 2)}")
print(f"1-3 total: {s.numberOfPatterns(1, 3)}")
