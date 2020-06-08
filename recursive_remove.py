t=int(input( ))
while(t>0):
	s=input()
	a=len(s)
	temp=''
	temp1=''
	
	i=0
	while(i<a):
		# print(s[i])
		# print(i)
		if i==0:
			if s[i]!=s[i+1]:
				temp=temp+s[i]
				i+=1
			else:
				for j in range(i,a):
					if s[i]!=s[j]:
						i=j
						break
		elif i==a-1:
			if s[i]!=s[i-1]:
				temp=temp+s[i]
				i=i+1
			else:
				i=i+1		
		elif 0<i<a:
			if s[i]!=s[i+1]:
				temp=temp+s[i]
				i+=1
			elif s[i]==s[i+1]:
				for j in range(i,a):
					if s[i]!=s[j]:
						i=j
					#print(j)
					#print('i', i)
						break
		#elif s[i]==s[i+1]:
			#for j in range(i,a):
			#	if s[i]!=s[j]:
			#		i=j
					#print(j)
					#print('i', i)
			#		break
			#print('in elif', i)
		#print('outside', i)
		#print(temp)
	print(temp)		
	t-=1
