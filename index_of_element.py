t=int(input( ))
while(t>0):
	n=int(input( ))
	s1=input( )
	a=s1.split( )
	s2=input( )
	b=s2.split( )
	for i in range(len(a)):
		if a[i]!=b[i]:
			print(i)
			break
	t-=1		