import sys
import math
I = sys.stdin.readline

T = int(I().strip())

for i in range(T):
    n = int(I().strip())
    d = dict()
    total = 1
    for ii in range(n):
        _, M = I().split()
        if not M in d:
            d[M] = 1
        else:
            d[M] += 1
    for _, v in d.items():
        total *= v + 1
    print(total - 1)