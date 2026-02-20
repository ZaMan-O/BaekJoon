import sys
from collections import deque
I = sys.stdin.readline

N,M = map(int, I().split())
graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)
for _ in range(M):
    u,v = map(int, I().split())
    graph[u].append(v)
    graph[v].append(u)
connected = 0
first = 1
all_visited = False
while not all_visited:
    connected += 1
    queue = deque()
    queue.append(first)
    visited[first] = True
    while queue:
        data = queue.popleft()
        for i in graph[data]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)
    for i in range(1, N+1):
        if not visited[i]:
            first = i
            break
        if i == N:
            all_visited = True
print(connected)