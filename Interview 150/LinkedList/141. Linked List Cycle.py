# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Solution
# We just need to follow the strategy above - make a slower pointer and a faster pointer. Then we loop and loop again:

# if the fast pointer catch up with slow pointer, then it's a circular linked list
# if the fast pointer get to the end, then it's not a circular linked list

class Solution:
    def hasCycle(self, head):
        fast = slow = head
        while slow and slow.next:
            fast, slow = fast.next, slow.next.next
            if slow == fast:
                return True
        return False