import sys
from collections import deque
I = sys.stdin.readline
pos = [(1,0), (0,-1), (-1,0), (0,1)]

N = int(I().strip())
visited = [[False] * N for _ in range(N)]
queue = deque()
house = []
th = 0
ha = []
for _ in range(N):
    house.append(I().strip())
for i in range(N):
    for ii in range(N):
        if not visited[i][ii] and house[i][ii] == '1':
            total = 0
            queue.append([ii,i])
            visited[i][ii] = True
            while queue:
                x,y = queue.popleft()
                total += 1
                for dx, dy in pos:
                    nx, ny = x+dx, y+dy
                    if nx in range(N) and ny in range(N) and house[ny][nx] == '1' and not visited[ny][nx]:
                        visited[ny][nx] = True
                        queue.append([nx,ny])
            th += 1
            ha.append(total)
print(th)
ha.sort()
for i in ha:
    print(i)