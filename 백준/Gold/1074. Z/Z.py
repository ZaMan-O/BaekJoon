N, r, c = map(int, input().split())
p = pow(2,N-1)
tmp = p
an = 0
while True:
    mid = p
    if r < mid:
        if c >= mid:
            an += p * p
            c -= p
    else:
        if c < mid:
            an += p * p * 2
            r -= p
        else:
            an += p * p * 3
            c -= p
            r -= p
    if p == 1:
        break
    p //= 2
print(an)