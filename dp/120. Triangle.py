class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        visited = set()
        queue = []
        def bfs(visited, graph, coords):
            visited.append(coords)
            queue.append(coords)

            index = 0
            while queue:
                s = queue.pop(0)
                print (s, end = " ") 

                neighbors = [(coords[0]+1,coords[1]), (coords[0]+1,coords[1]+1)]
                for neigh in neighbors:
                    if neigh not in visited:
                        visited.append(neigh)
                        queue.append(neigh)
        bfs(visited, triangle, (0,0))