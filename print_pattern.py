t=int(input( ))
while(t>0):
    n=int(input())
    a=[ ]
    b=n-5
    a.append(int(n))
    a.append(b)
    while(b!=n):
        if b==n:
            break
        elif b>0:
            b=b-5
            a.append(b)
        elif b<=0:
            break

    while(b!=n):
        b=b+5
        a.append(b)        
            
    c=len(a)
    #print(c)
    #print(a)
    temp=''
    for i in range(c):
        temp=temp+str(a[i])
        temp=temp+' '
    print(temp)
    t-=1   

    