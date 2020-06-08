testcase = int(input( ))

while(testcase>0):

	i=int(input( ))

	if(i<0):
		while(i<=0):
			print(i,end=' ')
			i+=1

	elif(i>0):
		while(i>0):
			print(i,end=' ')

			i-=1
	else:
		print('already zero ')

	testcase-=1	
