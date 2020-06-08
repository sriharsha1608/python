testcase = int(input( ))

while(testcase>0):
	str = input( )

	cat=str.count('cat')
	hat=str.count('hat')

	if (cat == hat):
		print('true')
	else:
		print('false')

	testcase-=1
		
