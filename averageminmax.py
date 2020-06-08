testcases = int(input( ))
while(testcases>0):
	a=input( )
	ist_a=a.split(' ')
	ist_b=[]
	for x in ist_a:
		ist_b.append(int(x))

	c=min(ist_b)
	d=max(ist_b)

	ist_b.remove(c)
	ist_b.remove(d)
    
	tot = 0
	
	for i in range(0,len(ist_b)):
		tot=tot+ist_b[i]

	print(tot)
	
	avg=(tot/len(ist_b))

	print(avg)

	testcases-=1	

