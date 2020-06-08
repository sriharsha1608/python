class Node:
	def __init__(self,data):
		self.data=data
		self.next=None

class Queue:
	def __init__(self):
		self.head=None

	def push(self,new_data):
		new_node=Node(new_data)
		new_node.next=self.head
		self.head=new_node

	def append(self,new_data):
		temp=self.head
		new_node=Node(new_data)
		if(temp is None):
			temp=new_node
			return
		while(temp.next is None):
			temp.next=new_node
		
	
	def dequeue(self):
		temp=self.head
		if(temp is not None):
			temp=temp.next
			self.head=temp

	def printqueue(self):
		temp=self.head
		while(temp):
			print(temp.data)
			temp=temp.next		

que=Queue()
que.append(1)
que.append(2)
que.dequeue()
que.printqueue()


