import math
t=int(input( ))
while(t>0):
	n=int(input( ))
	a=[2,3]
	
	for i in range(4,n+1):
		if i>1:
			for j in range(2,int(math.sqrt(i))+1):
				if i%j==0:
					break

			else:
				a.append(i)
	#print(a)
	b=len(a)
	if n==a[b-1]:
		print(0,end=' ')
		print(n)
	else:
		flag = 0
		for i in range(b):
			for j in range(b):
				if ((n-a[i])==a[j]):
					flag = 1
					print(a[i],end=' ')
					print(a[j]) 
					break
			if flag == 1:
				break
		
	t-=1





'''check prime and append in a list find from 
first of that numbers and differ with the same and
check in the append list and give it as output'''  		
