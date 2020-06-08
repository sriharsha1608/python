'selection sorting'

a=[64,25,12,22,11]
for i in range(len(a)):
	mi_d=i
	for j in range(i+1,len(a)):
		if a[mi_d]>a[j]:
			mi_d=j
	a[i],a[mi_d]=a[mi_d],a[i]
	
print(a)			

