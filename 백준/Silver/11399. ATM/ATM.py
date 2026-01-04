import sys
I = sys.stdin.readline
N = int(I().strip())
List = list(map(int, I().split()))
List.sort()
total = 0
pre = 0
for i in List:
    total += pre + i
    pre += i
print(total)