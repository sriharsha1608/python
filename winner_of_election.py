t=int(input( ))
while(t>0):
	n=int(input( ))
	s=input( )
	a=s.split(' ')
	b=[ ]
	for i in range(n):
		k=s.count(a[i])
		b.append(k)

	max(b)

	for i in range(n):
		if b[i]==max(b):
			print(a[i],end=' ')
			print(b[i])
			break

	t-=1		 	  