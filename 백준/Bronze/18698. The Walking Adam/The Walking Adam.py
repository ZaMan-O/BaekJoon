T=int(input())
for _ in range(T):
    S=input()
    total=0
    for i in S:
        if i=='U':
            total+=1
        else:
            break
    print(total)