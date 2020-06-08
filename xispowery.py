t=int(input( ))
while(t>0):
    n=input( )
    g=n.split( )
    b=int(g[0])
    c=int(g[1])
    flag=' '
    if(b>1):
        while(c>1):
            if (c%b==0):
                c=int(c/b)
            else:
                flag='0'
                break
        if(c==1):
            flag='1'
        elif(c==0):
            flag='0'
    elif (b==1):
        if c/b==1:
            flag='1'
        else:
            flag='0'
    elif(b==0):
        flag='0'
	    
    print(flag)
    t-=1			