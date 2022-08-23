
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        nodes = {}

        counter = 1
        nodes[counter] = head
        cur_head = head

        if head is None: return head

        while cur_head.next != None:
            counter += 1
            cur_head = cur_head.next
            nodes[counter] = cur_head

        size = len(nodes)
        n_last = size - n 

        if n_last == 0:
            start = head.next
        else:
            start = head

        for i in range(n_last, size):
            if i == 0:
                continue

            if i == n_last: 
                try:
                    nodes[i].next = nodes[i+2]
                except:
                    nodes[i].next = None
            elif i == n_last + 1:
                continue
            else:
                nodes[i].next = nodes[i+1]

        return start 