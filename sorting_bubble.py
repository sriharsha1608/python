'bubble sort'

a=[64,34,25,12,22,11,90,13]
for i in range(len(a)):

	for j in range(0,len(a)-1-i):
		if a[j]>a[j+1]:
			a[j],a[j+1]=a[j+1],a[j]

print(a)			