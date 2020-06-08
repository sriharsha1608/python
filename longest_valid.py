t=int(input( ))
a=['(']
b=[')']
while(t>0):
	s=input( )
	c=s.split( )
	d=[]
	e=[]
	for i in range(len(s)):
		if s[i]=='(':
			d.append(s[i])
		else:
			e.append(s[i])
	print(d)
	print(e)
	f=len(d)
	g=len(e)

	if f>g:
		print(g*2)
	else:
		print(f*2)

	t-=1	
