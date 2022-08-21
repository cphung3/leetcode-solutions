class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for i in range(m)] for j in range(n)]
        dp[n-1][m-1] = 1
        
        for i in range(n-1, -1, -1):
            for j in range(m-1, -1, -1):
                if i + 1 < n and j + 1 < m:
                    dp[i][j] = dp[i+1][j] + dp[i][j+1]
                elif i + 1 >= n and j + 1 >= m:
                    pass
                elif i + 1 >= n:
                    dp[i][j] = dp[i][j+1]
                elif j + 1 >= m:
                    dp[i][j] = dp[i+1][j]
        return dp[0][0]

    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n

        for i in range(m-1):
            newRow = [1] * n
            for j in range(n - 2, -1, -1):
                newRow[j] = newRow[j + 1] + row[j]
            row = newRow
        return row[0]

# Runtime: 39 ms, faster than 79.00% of Python3 online submissions for Unique Paths.
# Memory Usage: 13.8 MB, less than 74.78% of Python3 online submissions for Unique Paths.