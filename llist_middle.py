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

	def	getcount(self):
		temp=self.head
		count=0
		while(temp):
			count=count+1
			temp=temp.next
		return count
	
	def middle(self):
		temp=self.head
		ke=self.getcount()//2
		counts=0
		flag=''
		while(temp):
			if(counts==ke):
				flag=temp.data
			counts=counts+1
			temp=temp.next
		return flag

llist=Linkedlist()
llist.push(9)
llist.push(8)
llist.push(7)
llist.push(6)
llist.push(5)
llist.push(4)
llist.push(3)
llist.push(2)
llist.push(1)
print(llist.middle())									