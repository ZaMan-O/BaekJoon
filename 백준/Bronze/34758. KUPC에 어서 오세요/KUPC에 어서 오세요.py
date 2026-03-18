import sys
I = sys.stdin.readline

cx, cy = map(int, I().split())
N = int(I().strip())
pos = []
for _ in range(N):
    x,y = map(int, I().split())
    if x == cx or y == cy:
        print(0)
    else:
        print(1)