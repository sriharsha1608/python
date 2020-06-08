n=int(input( ))
a=str(n)
o=0
e=0
for i in range(len(a)):
	if i%2==0:
		o=o+int(a[i])
	else:
		e=e+int(a[i])
if o>e:
	print(o-e)
else:
	print(e-o)		
