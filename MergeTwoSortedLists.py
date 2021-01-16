class ListNode:
	def __init__(self, val = 0, next = None):
		self.val = val
		self.next = next
	
	def make_list(self):
		arr = []
		while self is not None:
			arr.append(self.val)
			self = self.next
		return arr

def mergeTwoLists(l1, l2):
	p1 = ListNode(None,None)
	head = p1
	while True:
		if l1 is None:
			p1.next = l2
			break
		if l2 is None:
			p1.next =l1
			break
		if l1.val < l2.val:
			p1.next = ListNode(l1.val)
			l1 = l1.next
		else:
			p1.next = ListNode(l2.val)
			l2 = l2.next
		p1 = p1.next
	return head.next

if __name__ == "__main__":
	l1 = ListNode(1, ListNode(4, ListNode(6, None)))
	l2 = ListNode(2, ListNode(3, ListNode(10, ListNode(14, None))))
	sortedList = mergeTwoLists(l1, l2)
	print(f"(TEST)\n\tList 1: {l1.make_list()}\n\tList 2: {l2.make_list()}\n\tResult: {sortedList.make_list()}")
