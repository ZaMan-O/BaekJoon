N,A,B = map(int, input().split())
arr = [1,1]
for i in range(N):
    arr[0] += A
    arr[1] += B
    if arr[1] > arr[0]:
        tmp = arr[1]
        arr[1] = arr[0]
        arr[0] = tmp
    elif arr[0] == arr[1]:
        arr[1] -= 1
print(*arr)