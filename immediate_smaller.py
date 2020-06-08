t=int(input( ))
while(t>0):
	n=int(input( ))
	s=input()
	a=s.split( )
	b=len(a)
	for i in range(b-1):
		if a[i]>a[i+1]:
			print(str(a[i+1]),end=' ')
		else:
			print('-1',end=' ')
	print('-1')
	t-=1		