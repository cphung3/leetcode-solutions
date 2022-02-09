# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        depths = []
        node = root
        def recurse(node, depths):
            if not node:
                return 0
            left = node.left
            l = recurse(left, depths)
            right = node.right
            r = recurse(right, depths)
            depths.append(abs(l - r))
            return 1 + max(l, r)
        a = recurse(node, depths)
        if len(depths):
            return (max(depths) - min(depths)) < 2
        else: 
            return False

# Runtime: 56 ms, faster than 71.38% of Python3 online submissions for Balanced Binary Tree.
# Memory Usage: 18.8 MB, less than 50.50% of Python3 online submissions for Balanced Binary Tree.