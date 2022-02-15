# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        node = root
        def recurse(node, target):
            if not node:
                return None

            rightChild = node.right
            leftChild = node.left

            l = recurse(node.left)
            r = recurse(node.right)
            if node.left is None and node.right is None:
                return node

            if leftChild:
                node.right = leftChild
                leftChild.right = rightChild
                node.left = None
            

            return l or r
        ans = recurse(node, targetSum)
        # print(ans)
        # print()
        return ans