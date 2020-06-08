testcase = int(input( ))
while(testcase>0):
	a=input( )
	ist_a=a.split(' ')
	ist_b=[]
	for x in ist_a:
		ist_b.append(int(x))

	b=[]
	c=[]
	for i in range(0,len(ist_b)):

		if(ist_b[i]%2==0):
			b.append(int(ist_b[i]))
		else:
			c.append(int(ist_b[i]))

	d=len(b)
	e=len(c)

	print(d)
	print(e)

	testcase-=1		