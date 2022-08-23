class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        reqMap = { i: [] for i in range(numCourses)}
        
        for crs, pre in prerequisites:
            reqMap[crs].append(pre)

        visitedSet = set()
        def dfs(course):
            if course in visitedSet:
                return False
            if reqMap[course] == []:
                return True

            visitedSet.add(course)
            for pre in reqMap[course]:
                if not dfs(pre): return False
            visitedSet.remove(course)
            reqMap[course] = []
            return True

        for crs in range(numCourses):
            if not dfs(crs): return False
        return True