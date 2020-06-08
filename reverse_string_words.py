t=int(input())
while(t>0):
	s=input()
	b=s.split('.')
	#print(b)
	c=b[::-1]
	#print(b[::-1])
	d=[]
	for i in c:
		d.append(i)
		d.append('.')
	#print(d)
	d.pop()
	str1=' '
	str2 = str1.join(d)
	print(str2)
	t-=1