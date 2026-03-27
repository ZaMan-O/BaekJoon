import sys
I = sys.stdin.readline

def dfs(num, cnt, arr):
    if cnt == M:
        print(*arr)
        return
    for i in range(num, N+1):
        arr2 = []
        for ii in arr:
            arr2.append(ii)
        arr2.append(i)
        dfs(i, cnt+1, arr2)

N, M = map(int, I().split())
for i in range(1, N+1):
    dfs(i, 1, [i])