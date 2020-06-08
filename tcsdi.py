a,b=input( ).split(' ')
#b=a.split(' ')
c=a
d=b
e=int(c)
f=int(d)
g=[]
for i in range(e,f+1):
	h=str(i)
	j=set(h)
	l=list(j)
	if len(h)==len(l):
		g.append(i)

print(len(g))

