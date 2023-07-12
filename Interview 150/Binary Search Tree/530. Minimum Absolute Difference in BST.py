# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.high = float('inf')
        self.low = 0
        self.diff = self.high - self.low

    def getMinimumDifference(self, root) -> int:
        if root:
            # First recur on left child
            self.getMinimumDifference(root.left)
    
            # Then print the data of node
            # print(root.val, end=" ")
            newDiffHigh = abs(root.val - self.low)
            newDiffLow = abs(self.high - root.val)

            if newDiffHigh < self.diff:
                self.high = root.val
            elif newDiffLow < self.diff:
                self.low = root.val
            print(newDiffHigh, newDiffLow, root.val)

            # Now recur on right child
            self.getMinimumDifference(root.right)
        return self.high - self.low
    
a = [1,0,48,None,None,12,49]
# b = [0,1,2,4,5,7,9]
# c = [0,2,3,68,80,90]
# d = [0,1000]
# e = []

tests = [a]

for i in tests:
    a = Solution().getMinimumDifference(i)
    print(a)  
    print()