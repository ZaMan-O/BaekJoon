import sys
I = sys.stdin.readline

tc = int(I().strip())
arr = [0] * 10001
for i in range(tc):
    arr[int(I().strip())] += 1

for i in range(1,10001):
    for ii in range(arr[i]):
        print(i)