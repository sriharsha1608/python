t=int(input( ))
while(t>0):
    a,b,c=input().split()
    d=(int(a)**int(b))%int(c)
    print(d)
    t-=1