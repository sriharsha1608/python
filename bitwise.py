i=int(input())
while(i>0):

	a=int(input())
	b=int(input())
	c=int(input())

	d = a^a
	e = c^b
	f = a&b
	g = c|(a^a)
	e = ~e

	print(d)
	print(e)
	print(f)
	print(g)
	print(e)

	i-=1
