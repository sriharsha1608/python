n=int(input( ))
m=int(input( ))
i=n
while(i>=n):
	if i%n==0:
		a=str(i)
		c=0
		for j in range(len(a)):
			c=c+int(a[j])
		if c==m:
			print(i)
			break
	i=i+1			