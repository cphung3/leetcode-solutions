# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
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
        highest = ret[0]
        for res in ret[1:]:
            if res <= highest:
                return False
            highest = res
        # print(ret)
        return True

# Runtime: 54 ms, faster than 33.06% of Python3 online submissions for Validate Binary Search Tree.
# Memory Usage: 17.1 MB, less than 13.43% of Python3 online submissions for Validate Binary Search Tree.