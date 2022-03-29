class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        stack = [(0,0)]
        dp = {}
        m, n = len(grid)-1, len(grid[0])-1

        while stack: 
            # get the down and right neighbors
            cur = stack.pop()
            if cur not in dp:
                a, b = cur[0], cur[1]
                val = grid[a][b]
                dp[cur] = val
            else: 
                val = dp[cur]
                

            i, j = cur[0], cur[1]+1
            x, y = cur[0]+1, cur[1]
            right = grid[i][j]
            down = grid[x][y]

            dp[i,j] = right + val
            dp[x,y] = down + val
            
            if right < down:
                stack.append((x, y))
                stack.append((i, j))
            else:
                stack.append((i, j))
                stack.append((x, y))
        print(dp)
        return dp[m,n]