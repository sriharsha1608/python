import math
t=int(input( ))
while(t>0):
	n=int(input( ))
	count=5

	for i in range(4,n+1):
		if i>1:
			for j in range(2,int(math.sqrt(i))+1):
				if i%j==0:
					break
		
			else:
				count=count+i

				

	print(count)	
	t-=1		

