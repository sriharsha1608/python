from math import factorial
t=int(input( ))

'''def count(N,n):
    c=0
    while(N>0):
        if(N%10==n):
            c+=1
        N=int(N/10) 
    return c    '''
        
    
while(t>0):
    b=int(input( ))
    n=5
    count=0
    while(b/n>=1):
        count=count+int(b/n)
        n=n*5    
    
    print(count)
    t-=1