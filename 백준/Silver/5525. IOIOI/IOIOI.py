import sys
from collections import deque
I = sys.stdin.readline
i = 0

N = int(I().strip())
M = int(I().strip())
S = I().strip()
P = []
while i < M-2:
    if S[i] == 'I' and S[i+1] == 'O' and S[i+2] == 'I':
        i += 3
        l = 1
        while True:
            if i+1 < M and S[i] == 'O' and S[i+1] == 'I':
                l += 1
                i += 2
            else:
                break
        if l >= N:
            P.append(l)
    else:
        i += 1
total = 0
for i in P:
    total += i - N + 1
print(total)