import sys
from collections import deque
I = sys.stdin.readline

N,M = map(int, I().split())
school = []
friends = 0
doyeon = [0,0]
visited = [[False] * M for _ in range(N)]
for i in range(N):
    school.append(I().strip())
for i in range(N):
    for ii in range(M):
        if school[i][ii] == 'X':
            visited[i][ii] = True
            continue
        if school[i][ii] == 'I':
            doyeon[0] = ii
            doyeon[1] = i

queue = deque()
queue.append(doyeon)
visited[doyeon[1]][doyeon[0]] = True
while queue:
    x,y = queue.popleft()
    if school[y][x] == 'P':
        friends += 1
    if x+1 < M and not visited[y][x+1]:
        visited[y][x+1] = True
        queue.append([x+1,y])
    if y-1 >= 0 and not visited[y-1][x]:
        visited[y-1][x] = True
        queue.append([x,y-1])
    if x-1 >= 0 and not visited[y][x-1]:
        visited[y][x-1] = True
        queue.append([x-1,y])
    if y+1 < N and not visited[y+1][x]:
        visited[y+1][x] = True
        queue.append([x,y+1])
if friends == 0:
    print('TT')
else:
    print(friends)