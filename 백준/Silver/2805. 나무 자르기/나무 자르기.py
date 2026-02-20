import sys
I = sys.stdin.readline

N,M = map(int, I().split())
woods = list(map(int, I().split()))
first, last = 1, max(woods)
while first <= last:
    mid = (first + last) // 2
    total = 0
    for i in woods:
        if i > mid:
            total += i - mid
    if total >= M:
        first = mid + 1
    else:
        last = mid - 1
print(last)