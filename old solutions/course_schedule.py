'''
There are a total of n courses you have to take, labeled from 0 to n-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

Example 1:

Input: 2, [[1,0]] 
Output: true
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: 2, [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0, and to take course 0 you should
             also have finished course 1. So it is impossible.
Note:

The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
You may assume that there are no duplicate edges in the input prerequisites.
'''
        # create adjacency matrix
        # one pass in O(n)
        adjacency = {}
        for pair in prerequisites:
            # if (pair[1] == pair[0]
            # or (pair[1] in adjacency and pair[0] == adjacency[pair[1]])
            # or (pair[0] in adjacency and pair[1] == adjacency[pair[0]])): 
            #     return False
            adjacency[pair[0]] = pair[1]
        # if len(adjacency) >= numCourses: return False
        # return True


    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        self.graph = {}
        for pair in prerequisites:
            a = pair[0]
            b = pair[1]

            self.graph.setdefault(a, [])
            self.graph[a].append(b)
        return not self.isCyclic(numCourses)

    def isCyclicUtil(self, v, visited, recStack): 
  
        # Mark current node as visited and  
        # adds to recursion stack 
        visited[v] = True
        recStack[v] = True
  
        # Recur for all neighbours 
        # if any neighbour is visited and in  
        # recStack then graph is cyclic 
        if v not in self.graph:
            recStack[v] = False

            return False
        else:
            for neighbour in self.graph[v]: 
                if visited[neighbour] == False: 
                    if self.isCyclicUtil(neighbour, visited, recStack) == True: 
                        return True
                elif recStack[neighbour] == True: 
                    return True
      
            # The node needs to be popped from  
            # recursion stack before function ends 
            recStack[v] = False
            return False
  

    # Returns true if graph is cyclic else false 
    def isCyclic(self, numCourses): 
        visited = [False] * numCourses
        recStack = [False] * numCourses
        for node in self.graph.keys(): 
            if visited[node] == False: 
                if self.isCyclicUtil(node,visited,recStack) == True: 
                    return True
        return False
