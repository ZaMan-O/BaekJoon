import sys
I = sys.stdin.readline
N, K = map(int, I().split())
C = [int(I().strip()) for _ in range(N)]
highest = -1
for i in C:
    if i > K:
        break
    highest += 1
best = C[highest] * (K // C[highest])
amount = 0
while True:
    amount = 0
    tmp = K % best
    amount += K // C[highest]
    for ii in range(highest - 1, -1, -1):
        amount += tmp // C[ii]
        tmp = tmp % C[ii]
    if tmp == 0:
        break
    else:
        if best == C[highest]:
            highest -= 1
        best -= C[highest]
print(amount)