import sys
from collections import deque
I = sys.stdin.readline
dr = [(1,0), (0,-1), (-1,0), (0,1)]

maze = []
min_dt = 10000
N, M = map(int, I().split())
visited = [[False] * M for _ in range(N)]
for _ in range(N):
    maze.append(I().strip())
queue = deque()
queue.append([0,0,1])
visited[0][0] = True
while queue:
    x,y,dt = queue.popleft()
    if x == M-1 and y == N-1 and dt < min_dt:
        min_dt = dt
        continue
    for di, dj in dr:
        ni, nj = x + di, y + dj
        if ni in range(M) and nj in range(N) and not visited[nj][ni] and maze[nj][ni] == '1':
            queue.append([ni,nj,dt+1])
            visited[nj][ni] = True
print(min_dt)