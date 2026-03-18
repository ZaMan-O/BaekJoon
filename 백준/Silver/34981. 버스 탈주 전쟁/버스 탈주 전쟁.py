import sys
I = sys.stdin.readline

X,Y = map(int, I().split())
T = X*60 + Y
N = int(I().strip())
result = 1440
for _ in range(N):
    a,b,d = map(int, I().split())
    tmp = T - a*60 - b
    if tmp < 0:
        result = min(-tmp, result)
        continue
    time = 0
    if tmp % d == 0:
        time = T
    else:
        time = a*60 + b + (tmp // d + 1) * d
    if time >= 1440:
        result = min(1440 - T + a*60 + b, result)
    else:
        result = min(time - T, result)
result = (T + result) % 1440
print("{:0>2}:{:0>2}".format(result // 60, result % 60))