i=int(input())
while(i>0):

	str=input()
	for j in range(0,len(str),2):
		print (str[j], end = '')
	i-=1
