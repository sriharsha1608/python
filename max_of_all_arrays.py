t=int(input( ))
while(t>0):
	a,b=input().split()
	s=input()
	c=s.split()
	d=[]
	for i in range(0,int(a)-int(b)+1):
		e=[]
		for j in range(0,int(b)):

			e.append(int(c[i+j]))
		d.append(max(e))
	temp=''
	for i in range(len(d)):
		temp=temp+str(d[i])
		temp=temp+' '
	print(temp)	
	t-=1
