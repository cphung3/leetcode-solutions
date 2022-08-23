class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None



def maxDepth(self, root: TreeNode) -> int:
    def recurse(root, height):
        if root == None: return 0
        if not root.left and not root.right:
            return height
        else:
            left_height = recurse(root.left, height+1)
            right_height = recurse(root.right, height+1)
            max_height = max(left_height, right_height)
            return max_height
    return recurse(root, 1)