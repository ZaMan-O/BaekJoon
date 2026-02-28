import sys
from collections import deque
I = sys.stdin.readline

visited = [False] * 100001
N, K = map(int, I().split())
queue = deque()

queue.append([N, 0])
visited[N] = True
while queue:
    X, t = queue.popleft()
    if X == K:
        print(t)
        break
    for i in [X*2, X+1, X-1]:
        if 0 <= i <= 100000 and not visited[i]:
            queue.append([i,t+1])
            visited[i] = True