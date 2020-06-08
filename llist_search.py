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

	def search(self,key):
		temp=self.head
		flag=''
		while(temp):
			if(temp.data==key):
				flag='yes'
			else:
				flag="No"
			temp=temp.next
		return(flag)	
			


llist=Linkedlist()
llist.push(1)
llist.push(2)
print(llist.search(3))
								