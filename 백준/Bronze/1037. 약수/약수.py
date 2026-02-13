import sys
I = sys.stdin.readline

M = int(I().strip())
A = list(map(int, I().split()))
print(min(A) * max(A))