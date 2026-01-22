import sys
I = sys.stdin.readline

N, M = map(int, I().split())
list = list(map(int, I().split()))
total = [_ for _ in range(N + 1)]

for i in range(N):
    if i == 0:
        total[1] = list[0]
    else:
        total[i+1] = total[i] + list[i]

for _ in range(M):
    i,j = map(int, I().split())
    print(total[j] - total[i-1])