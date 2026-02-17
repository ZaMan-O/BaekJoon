import sys
I = sys.stdin.readline

K, N = map(int, I().split())
arr = []
for _ in range(K):
    arr.append(int(I().strip()))
first, last = 1, max(arr)
while first <= last:
    mid = (first + last) // 2
    lines = 0
    for i in arr:
        lines += i // mid
    if lines >= N:
        first = mid + 1
    else:
        last = mid - 1
print(last)