t=int(input( ))
while(t>0):
	a,b=input( ).split( )
	s=input( )
	c=s.count(b)
	if c==0:
		print('-1')
	else:
		print(c)
	t-=1