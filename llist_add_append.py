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

	def insertafter(self,prev_node,new_data):
		if (prev_node is None):
			return
		new_node=Node(new_data)
		new_node.next=prev_node.next
		prev_node.next=new_node

	def append(self,new_data):
		temp=self.head
		new_node=Node(new_data)
		if temp is None:
			new_node=temp
			return

		while(temp.next):
			
			temp=temp.next
		temp.next=new_node
	
	def printlist(self):
		temp=self.head
		while(temp):
			print(temp.data)
			temp=temp.next

llist=Linkedlist()
llist.push(3)
llist.append(2)
llist.printlist()						

