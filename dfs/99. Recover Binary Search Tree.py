# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        #inorder traversal the tree, if we found current element greater than later element, we need to swap it
        #later if we found a element is less than previous, swap it with the the invalid element found before
        
        stack = []
        x = y = prev = None
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if prev and root.val < prev.val:
                if not x:
                    x = prev
                #two invalids might be connected together
                y = root
            prev = root
            root = root.right
        x.val, y.val = y.val, x.val
        
        return root
        

# Runtime: 99 ms, faster than 35.71% of Python3 online submissions for Recover Binary Search Tree.
# Memory Usage: 14.8 MB, less than 23.78% of Python3 online submissions for Recover Binary Search Tree.