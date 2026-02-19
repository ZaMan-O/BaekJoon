import sys
from collections import deque
I = sys.stdin.readline

N = int(I().strip())
paper = [[None] * N for _ in range(N)]
cut = deque()
white, blue = 0, 0
for i in range(N):
    paper[i] = list(map(int, I().split()))
cut.append([0,0,N])
while cut:
    x, y, size = cut.pop()
    color = paper[y][x]
    if size == 1:
        if color == 0:
            white += 1
        else:
            blue += 1
        continue
    full = True
    for i in range(size):
        for ii in range(size):
            if paper[y+i][x+ii] != color:
                full = False
                cut.append([x,y,size // 2])
                cut.append([x+size // 2,y,size // 2])
                cut.append([x,y+size // 2,size // 2])
                cut.append([x+size // 2,y+size // 2,size // 2])
                break
        if full == False:
            break
    if full == True:
        if color == 0:
            white += 1
        else:
            blue += 1
print(white)
print(blue)