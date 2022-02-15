# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ret = []
        node = root
        def recurse(node, buildup):
            if not node:
                return None
            
            left = node.left
            if left:
                l = recurse(left, buildup)
                # print('L', left.val)
                # return l
            # print('M', node.val)
            buildup.append(node.val)

            right = node.right
            if right:
                r = recurse(right, buildup)
                # print('R', right.val)
                # return r
            # ret.append(node)
        recurse(node, ret)
        print(ret)
        return ret

# Runtime: 58 ms, faster than 5.56% of Python3 online submissions for Binary Tree Inorder Traversal.
# Memory Usage: 14.2 MB, less than 76.53% of Python3 online submissions for Binary Tree Inorder Traversal.