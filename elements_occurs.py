from math import factorial
t=int(input( ))

def count(N,n):
    c=0
    while(N>0):
        if(N%10==n):
            c+=1
        N=int(N/10) 
    return c    
        
    
while(t>0):
    b=int(input( ))
    a=factorial(b)
    
    print(count(a,0))
    t-=1