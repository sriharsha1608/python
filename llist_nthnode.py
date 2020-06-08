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

	def nthnode(self,key):
		temp=self.head
		count=0
		flag=''
		while(temp):
			count=count+1
			if count==key:
				flag=temp.data
			temp=temp.next
		return(flag)
llist=Linkedlist()
llist.push(3)
llist.push(2)
llist.push(1)
print(llist.nthnode(3))								