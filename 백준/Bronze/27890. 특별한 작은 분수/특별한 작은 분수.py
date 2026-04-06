import sys
I = sys.stdin.readline

h, t = map(int, I().split())
for i in range(t):
    if h % 2 == 0:
        h = (h//2) ^ 6
    else:
        h = (h*2) ^ 6
print(h)