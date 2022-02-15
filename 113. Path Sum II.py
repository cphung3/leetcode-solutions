# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        node = root
        allPaths = []
        def recurse(node, target, allPaths, curPath):
            if not node:
                return []
            
            newSum = target - node.val 
            curPath.append(node.val)
            
            l = recurse(node.left, newSum, allPaths, curPath)
            r = recurse(node.right, newSum, allPaths, curPath)
            if node.left is None and node.right is None:
                if newSum == 0:
                    allPaths.append(curPath.copy())

            curPath.pop()
            return allPaths
        ans = recurse(node, targetSum, allPaths, [])
        return ans

# Runtime: 66 ms, faster than 44.16% of Python3 online submissions for Path Sum II.
# Memory Usage: 15.6 MB, less than 74.97% of Python3 online submissions for Path Sum II.