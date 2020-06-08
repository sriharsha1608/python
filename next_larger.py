t=int(input())
while(t>0):
	n=int(input( ))
	s=input( )
	a=s.split( )
	b=[]
	for i in range(len(a)):
		for j in range(i+1,len(a)):
			if int(a[i])<int(a[j]):
				b.append(int(a[j]))
				break
		else:
			b.append(-1)

	temp=''
	for i in range(len(b)):
		temp=temp+str(b[i])
		temp=temp+' '
	print(temp)
	t-=1						
				

			
