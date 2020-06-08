import numpy as np
testcase=int(input( ))
while(testcase>0):
	n=int(input( ))
	m=int(input( ))
	a=np.array([ ])
	b=np.array([ ])
	c=input( )
	d=c.split(' ')
	e=input( )
	f=e.split(' ')
	for i in d:
		a=np.append(a,int(i))
	for j in f:
		b=np.append(b,int(j))

	for k in b:
		a=np.append(a,int(k))

	a=np.sort(a)

	print(a)
	testcase-=1			