import numpy as np
testcase = int(input( ))
while(testcase>0):
	n=int(input( ))
	a=np.arange(n)
	b=np.array([ ])
	for i in range(n-1):
		c=int(input( ))
		b=np.append(b,[c])

	summ=0
	for j in range(len(b)):
		summ=summ+b[j]

	tot=(n*(n+1))/2

	miss=tot-summ

	print(miss)
	testcase-=1


