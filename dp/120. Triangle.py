class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        visited = []
        queue = []
        def bfs(visited, graph, row):
            visited.append(row)
            queue.append(row)

            index = 0
            while queue:
                s = queue.pop(0)
                print (s, end = " ") 

                neighbors = [graph[row+1][index], graph[row+1][index+1]]
                for neigh in neighbors:
                    if neigh not in visited:
                        visited.append(neigh)
                        queue.append(neigh)
        bfs(visited, triangle, 0)