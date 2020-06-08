import numpy as np
a=np.array([1])
n=int(input( ))
fact=1
for j in range(1,n+1):
	fact=fact*j
	a = np.append(a,[fact])
print (a)	