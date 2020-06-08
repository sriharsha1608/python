testcase = int(input())
while(testcase>0):
	a=input( )
	ist_a=a.split(' ')
	ist_b=[]
	for x in ist_a:
		ist_b.append(int(x))
	
	for i in range(0,len(ist_b)//2):
		print(ist_b[i],end=' ')

	for j in range(len(ist_b)//2,len(ist_b),3):
		print(ist_b[j],end=' ')

	testcase-=1	 		