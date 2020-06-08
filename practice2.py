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

	def deletenode(self,key):
		
		temp=self.head
		if(temp.data==key):
			temp=temp.next
			self.head=temp

		while(temp):
			if(temp.data==key):
				prev.next=temp.next
				break
			prev=temp
			temp=temp.next



	def printlist(self):
		temp=self.head
		while(temp):
			print(temp.data)
			temp=temp.next		

llist=Linkedlist()
llist.push(3)
llist.push(2)
llist.push(1)

llist.deletenode(1)
llist.printlist()
