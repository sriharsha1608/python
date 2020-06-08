t=int(input( ))
while(t>0):
	a,b=input().split()
	s=input( )
	c=s.split()
	if str(int(b)+1) in c:
		print(int(b)+1)
	else:
		print(int(b)-1)
	t-=1		