import sys
I = sys.stdin.readline

n = int(I().strip())
arr = list(map(int, I().split()))
jul = [-1] * n
for i in range(n):
    num = arr[i]
    if num == 0:
        jul[i] = i + 1
    else:
        for ii in range(num):
            jul[i-ii] = jul[i-1-ii]
        jul[i-num] = i + 1 
print(*jul)