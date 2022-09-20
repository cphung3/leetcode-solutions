class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        pacCoords = [(0, c) for c in range(cols)] + [(r, 0) for r in range(rows)]
        atlCoords = [(rows-1, c) for c in range(cols)] + [(r, cols-1) for r in range(rows)]
        visitedPac = set()
        visitedAtl = set()
        validPac = set()
        validAtl = set()
        def explore(coord, validSet, dirs, visited):
            r, c = coord[0], coord[1]
            for d in dirs:
                newCoord = coord[0] + d[0], coord[1] + d[1]
                nr, nc = newCoord[0], newCoord[1]
                if nr >= rows or nr < 0:
                    continue
                if nc >= cols or nc < 0:
                    continue
                # print(newCoord, nr, nc, r, c)
                if newCoord in visited:
                    continue
                if heights[nr][nc] >= heights[r][c]:
                    validSet.add(newCoord)
                    visited.add(newCoord)
                    explore(newCoord, validSet, dirs, visited)

                    
                    
        dirs = [(1, 0), (0, 1),(-1, 0), (0, -1)]

        for pac in pacCoords:
            validPac.add(pac)
            explore(pac, validPac, dirs, visitedPac)
        
        for atl in atlCoords:
            validAtl.add(atl)
            explore(atl, validAtl, dirs, visitedAtl)
        
        # print(validAtl, validPac)
        return validAtl.intersection(validPac)

