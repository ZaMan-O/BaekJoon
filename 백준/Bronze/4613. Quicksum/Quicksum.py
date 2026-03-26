while True:
    S=input()
    if S=='#':
        break
    total=0
    for i in range(len(S)):
        if S[i]==' ':
            continue
        total+=(ord(S[i])-64)*(i+1)
    print(total)