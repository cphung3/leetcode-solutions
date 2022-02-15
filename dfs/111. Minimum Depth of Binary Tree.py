# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        node = root
        def recurse(node, level):
            if not node:
                return float('inf')
            
            level += 1
            l = recurse(node.left, level)
            r = recurse(node.right, level)
            if l == float('inf') and r == float('inf'):
                return level

            return min(l, r)
        ans = recurse(node, 0)
        return ans

# Runtime: 1288 ms, faster than 5.05% of Python3 online submissions for Minimum Depth of Binary Tree.
# Memory Usage: 55.1 MB, less than 15.72% of Python3 online submissions for Minimum Depth of Binary Tree.

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        depth = 0
        queue = [root]
        
        while queue:
            queueLen = len(queue)
            depth += 1
            
            for i in range(queueLen):
                node = queue.pop(0)
                if not node.left and not node.right:
                    return depth
                
                if node.left:
                    queue.append(node.left)
                    
                if node.right:
                    queue.append(node.right)

# Runtime: 492 ms, faster than 88.30% of Python3 online submissions for Minimum Depth of Binary Tree.
# Memory Usage: 49.4 MB, less than 64.55% of Python3 online submissions for Minimum Depth of Binary Tree.