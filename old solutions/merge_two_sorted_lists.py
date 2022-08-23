# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        vals = []
        pointer_1 = l1
        pointer_2 = l2
        if not pointer_1:
            return l2
        elif not pointer_2:
            return l1

        while pointer_1 or pointer_2:
            if not pointer_1:
                vals.append(pointer_2)
                pointer_2 = pointer_2.next
            elif not pointer_2:
                vals.append(pointer_1)
                pointer_1 = pointer_1.next

            if pointer_1 and pointer_2:
                if pointer_1.val < pointer_2.val:
                    vals.append(pointer_1)
                    pointer_1 = pointer_1.next

                else:
                    vals.append(pointer_2)
                    pointer_2 = pointer_2.next
            elif pointer_1:
                vals.append(pointer_1)
                pointer_1 = pointer_1.next
            elif pointer_2:
                vals.append(pointer_2)
                pointer_2 = pointer_2.next

        newList = vals[0]
        first = newList
        for node in vals[1:]:
            newList.next = node
            newList = newList.next

        return first


            
    #           newList.val = pointer_1.val
    #           if pointer_1.next:
    #               pointer_1 = pointer_1.next

    #       else: 
                # newList.val = pointer_2.val

    #       if pointer_1.next and pointer_2.next:
          #       pointer_1 = pointer_1.next
          #       pointer_2 = pointer_2.next

