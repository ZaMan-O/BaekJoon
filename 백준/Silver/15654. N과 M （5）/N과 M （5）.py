import sys
I = sys.stdin.readline

def dfs(cnt, ls):
    if cnt == M:
        for i in ls:
            print(arr[i], end=" ")
        print("", end="\n")
        return
    for i in range(length):
        if i in ls:
            continue
        else:
            ls2 = []
            for ii in ls:
                ls2.append(ii)
            ls2.append(i)
            dfs(cnt+1,ls2)

N, M = map(int, I().split())
arr = list(map(int, I().split()))
length = len(arr)
arr.sort()
for i in range(length):
    dfs(1,[i])