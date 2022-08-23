class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = []
        i = 0
        visited = set()
        temp = []
        for row in grid:
            for col in range(len(row)):
                if grid[i][col] == 2:
                    temp.append((i, col))
            i += 1
        steps = 0
        queue.append(temp)
        while queue:
            rotten = queue.pop(0)
            separate = []
            for tile in rotten:
                new_rotten = self.spread(tile[0], tile[1], grid, (len(grid), len(grid[0])), visited)
                for item in new_rotten:
                    separate.append(item)
            if separate:
                queue.append(separate)
                steps += 1

        for row in grid:
            for col in row:
                if col == 1:
                    return -1
        return steps

    def spread(self, i, j, grid, size, visited):
        coords = [(i, j), (i+1, j), (i-1, j), (i,j+1), (i,j-1)]
        ret = []
        for x,y in coords:
            if (x < size[0] and x >= 0) and (y < size[1] and y >= 0):
                if (x,y) not in visited:
                    if grid[x][y] == 1:
                        grid[x][y] = 2
                        visited.add((x,y))
                        ret.append((x,y))
        return ret
