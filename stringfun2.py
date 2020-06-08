testcases = int(input( ))
while(testcases>0):

	string=input( )
	b=string.lower( )

	if (b.startswith('gfg')&b.endswith('gfg')):
		print('Yes')
	else:
		print('No')

	testcases-=1	
