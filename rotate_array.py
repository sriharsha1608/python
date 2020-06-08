t=int(input( ))
while(t>0):
	a,b=input().split()
	s=input( )
	e=s.split( )
	#print(int(b))
	#print(e)
	c=[]
	d=e[int(b):len(e)]+e[0:int(b)]
	temp=''
	for i in range(len(e)):
		temp=temp+str(d[i])
		temp=temp+' '
	print(temp)	
	t-=1