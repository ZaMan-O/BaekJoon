a,b=map(int,input().split())
c,d=map(int,input().split())
mx=0
rotate=0
for i in range(4):
    if a/c+b/d > mx:
        rotate=(4-i)%4
        mx=a/c+b/d
    tmp=b
    b=d
    d=c
    c=a
    a=tmp
print(rotate)