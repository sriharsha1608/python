'''insertion sort'''

a=[64,34,25,12,22,11,90,13]

for i in range(1,len(a)):
	key=a[i]
	j=i-1
	while j>=0 and key<a[j]:
		a[j],a[j+1]=a[j+1],a[j]
		j-=1
		a[j+1]=key	

print(a)		
