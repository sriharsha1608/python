import numpy as np
testcase=int(input())
while(testcase>0):
    n=int(input( ))
    a=np.zeros(n)
    for i in range(n):
        b=input( )
        a[i]=b
    count=0
    for j in a:
        count=count+j
    print(count)
    testcase-=1