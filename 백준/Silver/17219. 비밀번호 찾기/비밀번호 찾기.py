import sys
I = sys.stdin.readline
N, M = map(int, I().split())
d = {k:v for k,v in [I().split() for _ in range(N)]}
for _ in range(M):
    print(d[I().strip()])