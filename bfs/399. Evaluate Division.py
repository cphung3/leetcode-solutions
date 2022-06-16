class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        edges = self.createAdjacencyList(equations, values)
        all_paths = []
        # print(edges)
        for q in queries: 
            start = q[0]
            end = q[1]
            if start in edges:
                path = self.shortest_path(edges, start, end)
            else:
                path = []
            # print(start, end, path)
            all_paths.append(path)
        
        res = []
        for path in all_paths:
            value = 1
            if path:
                for idx in range(1, len(path)):
                    start = path[idx-1]
                    end = path[idx]
                    value *= edges[start][end]
            else:
                value *= -1
            res.append(value)
        return res

        
    def createAdjacencyList(self, equations, values):
        edges = {}
        for idx, edge in enumerate(equations):
            edges.setdefault(edge[0], {})
            edges.setdefault(edge[1], {})
            edges[edge[0]][edge[1]] = values[idx]
            edges[edge[1]][edge[0]] = 1 / values[idx]
        return edges

    def shortest_path(self, graph, node1, node2):
        path_list = [[node1]]
        path_index = 0
        # To keep track of previously visited nodes
        previous_nodes = [node1]
        if node1 == node2:
            return path_list[0]

        while path_index < len(path_list):

            current_path = path_list[path_index]
            last_node = current_path[-1]
            next_nodes = graph[last_node].keys()
            # Search goal node
            if node2 in next_nodes:
                current_path.append(node2)
                return current_path
            # Add new paths
            for next_node in next_nodes:
                if not next_node in previous_nodes:
                    new_path = current_path[:]
                    new_path.append(next_node)
                    path_list.append(new_path)
                    # To avoid backtracking
                    previous_nodes.append(next_node)
            # Continue to next path in list
            path_index += 1
        # No path is found
        return []