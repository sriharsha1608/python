t=int(input())
while(t>0):
	n=int(input())
	s=input( )
	a=s.split( )
	be=[]
	co=[]
	for i in a:
		if int(i)==0:
			be.append(int(i))
		elif int(i)==1:
			co.append(int(i))
		elif int(i)%2==0:
			be.append(int(i))
		else:
			co.append(int(i))

	
	co.sort()
	be.sort()
	
	c=co[::-1]
	for i in be:
		c.append(i)

	#print(c)	

	temp=''
	for i in range(len(c)):
		temp=temp+str(c[i])
		temp=temp+' '
	print(temp)	
	t-=1
			

