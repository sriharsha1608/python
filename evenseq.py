n=input( )
a=n.split(' ')
#print(a)
list_b=[]
list_c=[]

for i in range(len(a)):
	if int(a[i])%2 == 0:
		list_b.append(int(a[i]))
		#print(list_b)
	else:
		if len(list_b)>=len(list_c):
			list_c=list_b
			del list_b[:]
			

'''if len(list_b)>len(list_c):
	print(list_b)
else:
	print(list_c)'''

print(c)			






			