
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def reverseList(self, head: ListNode) -> ListNode:
	# Initialize three pointers prev as NULL, curr as head and next as NULL.
	# Iterate trough the linked list. In loop, do following.
	# // Before changing next of current,
	# // store next node
	# next = curr->next
	# // Now change next of current
	# // This is where actual reversing happens
	# curr->next = prev

	# // Move prev and curr one step forward
	# prev = curr
	# curr = next

	prev = None
	curr = head
	nxt = None

	while curr != None:
		nxt = curr.next
		curr.next = prev
		prev = curr
		curr = nxt

	head = prev
	return head




	# node_keys = []
	# start = head

	# if head == None or head.next == None: return head
	# while True:
	# 	node_keys.append(head.next)
	# 	head = head.next
	# 	if head == None: break

	# last = len(node_keys)-1
	# cur_key = start
	# for i in range(len(node_keys)):
	# 	cur_head = node_keys[i]
	# 	if cur_head == None: break
	# 	cur_head.val = node_keys[last]
	# 	if last == 0: cur_head.next = None
	# 	else:  cur_head.next = node_keys[last-1]
	# 	last -= 1

	# return node_keys[0]