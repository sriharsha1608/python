
t=int(input( ))
while(t>0):
    n=int(input( ))
    a=input( )
    temp1=''
    for i in range(len(a)):
    	if a[i]==' ':
    		temp1=temp1
    	else:
    		temp1=temp1+a[i]

    #e=a.remove( )

    #print(e)
    b=int(input( ))
    d=temp1[b:]+temp1[:b]
    c=len(d)
    temp=''
    for i in range(c):
    	temp=temp+d[i]
    	temp=temp+' '
    print(temp)	

    t-=1