N=int(input())
amount = 0
for _ in range(N):
    s=input().strip()
    d=dict()
    for i in range(len(s)):
        if i - d.get(s[i], i) > 1:
            break
        else:
            if i == len(s)-1:
                amount += 1
                break
            d[s[i]] = i
print(amount)