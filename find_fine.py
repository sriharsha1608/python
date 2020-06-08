t=int(input( ))
while(t>0):
	a,b=input().split()
	s1=input( )
	c=s1.split()
	s2=input( )
	d=s2.split()
	if int(b)%2==0:
		count=0
		for i in range(len(c)):
			if int(c[i])%2!=0:
				count=count+int(d[i])
	else:
		count=0
		for i in range(len(c)):
			if int(c[i])%2==0:
				count=count+int(d[i])

	print(count)
	t-=1						

