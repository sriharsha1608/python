import math
n=int(input( ))

for i in range (2,n):
	t=0
	s=0
	for j in range(2,int(math.sqrt(i))+1):
		s=s+1
		if i%j!=0:
			t=t+1
	if s==t:
		print(i)		