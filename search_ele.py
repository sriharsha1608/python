#code
t=int(input( ))
while(t>0):
    n=int(input())
    s=input()
    a=s.split()
    b=int(input())
    flag=0
    for i in range(len(a)):
        if int(a[i])==b:
            flag=i
            break
        else:
            flag=-1
    print(flag)
    t-=1