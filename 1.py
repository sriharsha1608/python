str1 = 'geeksforgeeks'
str2 = 'mask'

for i in range(len(str2)):
	b = ''
	for j in range(len(str1)):
		if str2[i] == str1[j]:
			b = b
		else:
			b = b + str1[j]
	str1 = b
print(b)			