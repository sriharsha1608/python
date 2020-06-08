import numpy as np
testcase=int(input( ))
while(testcase>0):
	n=int(input( ))
	a=np.array([ ])
	b=input( )
	c=b.split(' ')
	flag=-1

	for i in c:
		a=np.append(a,int(i))
	l_sum=0
	r_sum=0	

	for j in range(n):
		r_sum=0
		l_sum=0	
		for k in range(0,j):
			l_sum=l_sum+a[k]

		for k in range(j+1,n):
			r_sum=r_sum+a[k]

		if (l_sum==r_sum):
			flag=int(a[j])
		
	print(flag)	
	
	testcase-=1			