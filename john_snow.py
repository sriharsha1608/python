testcase = int(input( ))

while(testcase>0):

	j_angry = bool(input( ))
	print(j_angry)
	s_angry = bool(input( ))
	print(s_angry)
	
	if (j_angry!=s_angry):
		print('False')
	else:
		print('True')

	testcase-=1	