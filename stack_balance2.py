fclass Node:
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
		
		c=[]
		d=[]
		e=[]
		f=[]
		g=[]
		h=[]
		flag=' '

		for i in sttr:
			if i=='[':
				c.append(i)
			elif i=='{':
				d.append(i)
			elif i=='(':
				e.append(i)
			elif i==']':
				f.append(i)
			elif i=='}':
				g.append(i)
			elif i==')':
				h.append(i)

		if len(c)==len(f):
			a=True
		else:
			a=False

		if 	len(d)==len(g):
			b=True
		else:
			b=False

		if len(e)==len(h):
			j=True
		else:
			j=False


		if a & b & j==True:
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