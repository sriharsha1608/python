from math import factorial
t=int(input( ))
while(t>0):
    n=int(input())
    s=input( )
    no=factorial(n)/(factorial(n-3)*factorial(3))
    print(int(no))
    t-=1
    