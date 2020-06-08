class Node:
	def __init__(self,data):
		self.data=data
		self.next=None

class stack:
	def __init__(self):
		self.head=None

	def push(self,new_data):
		new_node=Node(new_data)
		new_node.next=self.head
		self.head=new_node

	def pop(self):
		temp=self.head
		prev=temp.data
		temp=temp.next
		self.head=temp
		return prev

	def printstack(self):
		temp=self.head
		while(temp):
			print(temp.data)
			temp=temp.next		

sstack=stack()
sstack.push(1)
sstack.push(2)
sstack.push(3)
sstack.pop()
sstack.pop()
sstack.printstack()


