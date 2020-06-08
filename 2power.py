t=int(input( ))
while(t>0):
	n=int(input( ))
	flag=''
	while(n!=1):
		print(n)
		if (n%2==0):
			n=int(n/2)
		else:
			print('No')
			break
	if n == 1:
		print('Yes')
	else:
		print('No')			
	t-=1			
	