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
	def check(self,sttr):
		a=['[','{','(']
		b=[']','}',')']
		c=[]
		d=[]
		flag=' '

		for i in sttr:
			for j in a:
				if i==j:
					c.append(i)

		for i in sttr:
			for k in b:
				if i==k:
					d.append(i)

		if len(c)==len(d):
			flag='balanced'
		else:
			flag='not balanced'
		return flag
		
sstack=stack()
sstack.push(2)
sstack.push(3)
print(sstack.pop())
sstack.printstack()
print(sstack.check('[)'))

'correct sol: in para.py'


								


