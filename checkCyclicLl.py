
class ListNode:

	
	def __init__(self, data):
		self.data = data
		self.next = None


class LinkedList:

	
	def __init__(self):
		self.head = None

	
	def add(self, new_data):
		new_node = ListNode(new_data)
		new_node.next = self.head
		self.head = new_node


	def isCyclic(self):
		s = set()
		temp = self.head
		while (temp):
			if (temp in s):
				return True
			s.add(temp)
			temp = temp.next

		return False


llist = LinkedList()
llist.add(3)
llist.add(2)
llist.add(0)
llist.add(-4)


llist.head.next.next.next.next = llist.head

if(llist.isCyclic()):
	print("True")
else:
	print("False")


