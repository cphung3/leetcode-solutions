# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def recurse(left, right):
            leaf = left == None and right == None
            sym = False
            equal = False
            if left and right:
                equal = left.val == right.val
                sym = recurse(left.left, right.right) and recurse(right.left, left.right)
            return leaf or (sym and equal)

        ans = recurse(root, root)
        return ans

# Runtime: 48 ms, faster than 37.76% of Python3 online submissions for Symmetric Tree.
# Memory Usage: 13.9 MB, less than 97.87% of Python3 online submissions for Symmetric Tree.