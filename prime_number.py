import math
testcase = int(input( ))

while(testcase>0):

	n=int(input( ))

	for i in range(2,int(math.sqrt(n))+1):

		if (n%i==0):
			print('No')
		else:
			print('Yes')

	testcase-=1		

