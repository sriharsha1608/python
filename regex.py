import re

testcase = int(input( ))

while(testcase>0):

	string=input( )
	pat=r'\d'
	mat=re.findall(pat,string)
	print (mat)

	testcase-=1