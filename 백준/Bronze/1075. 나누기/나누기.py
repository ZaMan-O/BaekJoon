import sys
I = sys.stdin.readline

N = int(I().strip())
F = int(I().strip())
result = 0
N = N - (N % 100)
for i in range(100):
    if (N+i) % F == 0:
        result = i
        break
print("%02d" % result)