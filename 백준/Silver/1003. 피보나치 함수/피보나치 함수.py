import sys
I = sys.stdin.readline
T = int(I().strip())
list = []
for i in range(41):
    if i == 0:
        list.append([1,0])
    elif i == 1:
        list.append([0,1])
    else:
        list.append([list[i-2][0] + list[i-1][0], list[i-2][1] + list[i-1][1]])
for _ in range(T):
    N = int(I().strip())
    print(list[N][0], list[N][1])