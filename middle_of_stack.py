t=int(input( ))
while(t>0):
	s=input( )
	a=s.split()
	a.pop(len(a)//2)
	b=a[::-1]
	temp=''
	for i in range(len(b)):
		temp=temp+str(b[i])
		temp=temp+' '
	print(temp)
	t-=1	