# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def inOrder(p, q):
            
            # Set current to root of binary tree
            current_p = p
            current_q = q

            stack_p = [] # initialize stack
            stack_q = [] # initialize stack
            same = True

            while True:
                
                # Reach the left most Node of the current Node
                if current_p is not None and current_q is not None:
                    
                    # Place pointer to a tree node on the stack
                    # before traversing the node's left subtree
                    stack_p.append(current_p)
                    stack_q.append(current_q)
                
                    current_p = current_p.left
                    current_q = current_q.left
        
                
                # BackTrack from the empty subtree and visit the Node
                # at the top of the stack; however, if the stack is
                # empty you are done
                elif(stack_p and stack_q):
                    current_p = stack_p.pop()
                    current_q = stack_q.pop()
                    if current_p.val != current_q.val:
                        same = False
                        break
                    print(current_p.val) # Python 3 printing
                    print(current_q.val) # Python 3 printing

                    # We have visited the node and its left
                    # subtree. Now, it's right subtree's turn
                    current_p = current_p.right
                    current_q = current_q.right
                elif(current_p is None and current_q is None):
                    break
                else:
                    same = False
                    break
            return same
        return inOrder(p, q)
        
# Runtime: 24 ms, faster than 97.05% of Python3 online submissions for Same Tree.
# Memory Usage: 13.9 MB, less than 99.99% of Python3 online submissions for Same Tree.