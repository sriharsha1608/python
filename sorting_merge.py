'merge_sort'


def merge_sort(a):
	if len(a)>1:
		mid=len(a)//2
		l=a[0:mid]
		r=a[mid:]
		merge_sort(l)
		merge_sort(r)
		i=j=k=0
		while i<len(l) and j<len(r):
			if l[i]<r[j]:
				a[k]=l[i]
				i+=1
			else:
				a[k]=r[j]
				j+=1
			k+=1
		while i<len(l):
			a[k]=l[i]
			i+=1
			k+=1
		while j<len(r):
			a[k]=r[j]
			j+=1
			k+=1
	return a					

a = [11,13,12,5,6,7]
print(merge_sort(a))					        