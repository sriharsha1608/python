testcase = int(input( ))
print(testcase)
while(testcase>0):
	a=input()
	list_a=a.split(' ')
	print(list_a)
	list_b=[]
	for x in list_a:
		list_b.append(int(x))

	print(list_b)
	print(list_b[0])
	print(list_b[len(list_b)-1])	
	if (list_b[0] == 0) or (list_b[len(list_b)-1] == 0):
		print('Yes')
	else:
		print('No')

	testcase-=1	

