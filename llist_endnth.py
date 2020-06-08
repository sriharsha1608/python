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

	def getcount(self):
		temp=self.head
		count=0
		while(temp):
			count=count+1
			temp=temp.next
		return count
	
	def endnth(self,key):
		ke=self.getcount()-key+1
		counts=0
		temp=self.head
		flag=''
		while(temp):
			counts=counts+1
			if(counts==ke):
				flag=temp.data
			temp=temp.next
		return flag

llist=Linkedlist()	
llist.push(1)
llist.push(2)
llist.push(3)
print(llist.endnth(2))			
