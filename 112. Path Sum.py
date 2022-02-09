# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        node = root
        def recurse(node, target):
            if not node:
                return False
                # return target == 0 and root is not None
            
            newSum = target - node.val 
            
            l = recurse(node.left, newSum)
            r = recurse(node.right, newSum)
            if node.left is None and node.right is None:
                # print('ns', newSum)
                return newSum == 0 and root is not None

            return l or r
        ans = recurse(node, targetSum)
        # print(ans)
        # print()
        return ans

# Runtime: 49 ms, faster than 57.02% of Python3 online submissions for Path Sum.
# Memory Usage: 15.3 MB, less than 10.19% of Python3 online submissions for Path Sum.