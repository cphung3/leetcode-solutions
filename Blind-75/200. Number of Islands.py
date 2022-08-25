class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        visitedIslands = set()
        islands = 0

        neighbors = [[1,0], [0,1], [-1,0], [0,-1]]

        def bfs(r, c):
            q = collections.deque()
            visitedIslands.add((r,c))
            q.append((r,c))

            while q:
                row, col = q.popleft()

                for dr, dc in neighbors:
                    rdr = row + dr
                    cdc = col + dc
                    if rdr not in range(rows):
                        continue
                    if cdc not in range(cols):
                        continue
                    if (rdr, cdc) in visitedIslands:
                        continue
                    if (grid[row][col] == '1'):
                        visitedIslands.add((rdr,cdc))
                        q.append((rdr, cdc))


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '0':
                    continue
                if grid[r][c] == '1' and (r,c) not in visitedIslands:
                    bfs(r, c)
                    islands += 1
        return islands

# Runtime: 648 ms, faster than 17.53% of Python3 online submissions for Number of Islands.
# Memory Usage: 29 MB, less than 5.01% of Python3 online submissions for Number of Islands.