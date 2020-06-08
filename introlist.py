
testcase = int(input( ))
while(testcase>0):
	a=input()
	list_a=a.split(' ')
	list_b=[ ]
	for x in list_a:
		list_b.append(int(x))

	list_b

	if list_b[0] or list_b[len(list_b)-1] == 0:
		print('Yes')
	else:
		print('No')

	testcase-=1	

