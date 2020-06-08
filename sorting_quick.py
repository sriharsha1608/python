'Quick Sort'

def partition(a,low,high):

	i=low-1
	pivot=a[high]

	for j in range(low,high):
		if a[j]<=pivot:
			i=i+1
			a[i],a[j]=a[j],a[i]

	a[i+1],a[high]=a[high],a[i+1]
	return (i+1)

def quicksort(a,low,high):
	if low<high:

		pi=partition(a,low,high)

		quicksort(a,low,pi-1)
		quicksort(a,pi+1,high)
	return a	

a=[10, 7, 8, 9, 1, 5]
print(quicksort(a,0,5))		

'''for i in range(6,-1,-1):
	print(i)	'''	