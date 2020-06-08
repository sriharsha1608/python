class Node:
	def __init__(self,data):
		self.data=data
		self.next=None
class Linkedlist:
	def __init__(self):
		self.head=None

	def push(self,new_data):
		new_node=Node(new_data)
		new_node.next=self.head
		self.head=new_node

	def counter(self):
		count=0
		temp=self.head
		while(temp):
			count=count+1
			temp=temp.next
		return count
llist=Linkedlist()
llist.push(3)
llist.push(2)
llist.push(1)
print(llist.counter())							