import sys
from collections import deque
I = sys.stdin.readline

N, M, V = map(int, I().split())
graph = [[] for _ in range(N)]
visited = [False for _ in range(N)]
dfs_result = []
bfs_result = []
for _ in range(M):
    A, B = map(int, I().split())
    graph[A-1].append(B-1)
    graph[B-1].append(A-1)
stack = deque()
stack.append(V-1)
while stack:
    node = stack.pop()
    if not visited[node]:
        dfs_result.append(node + 1)
        visited[node] = True
        for i in sorted(graph[node], reverse=True):
            stack.append(i)
print(*dfs_result)
for i in range(N):
    visited[i] = False
queue = deque()
queue.append(V-1)
while queue:
    node = queue.popleft()
    if not visited[node]:
        bfs_result.append(node + 1)
        visited[node] = True
        for i in sorted(graph[node]):
            queue.append(i)
print(*bfs_result)