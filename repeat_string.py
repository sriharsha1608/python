testcase = int(input( ))
while(testcase>0):

	string=input( ).split( )
	str1=string[0]
	str2=string[1]

	a=len(str1)
	b=len(str2)

	if (a>b):
		print(str2+str1+str2)
	else:
		print(str1+str2+str1)

	testcase-=1	