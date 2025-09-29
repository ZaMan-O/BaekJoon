import sys
I = sys.stdin.readline

M = int(I().strip())
arr = [False] * 20
for _ in range(M):
    str = I().split()
    if str[0] == "add":
        x = int(str[1])
        arr[x-1] = True
    elif str[0] == "remove":
        x = int(str[1])
        arr[x-1] = False
    elif str[0] == "check":
        x = int(str[1])
        print(1 if arr[x-1] else 0)
    elif str[0] == "toggle":
        x = int(str[1])
        arr[x-1] = False if arr[x-1] else True
    elif str[0] == "all":
        for i in range(20):
            arr[i] = True
    elif str[0] == "empty":
        for i in range(20):
            arr[i] = False