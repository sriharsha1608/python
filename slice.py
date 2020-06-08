testcase = int(input( ))
while(testcase>0):

	string=input( ).split( )
	sting1=string[0]
	sting2=string[1]

	a=len(sting1)

	print(sting1[0:a//2]+sting2+sting1[a//2:])

	testcase-=1