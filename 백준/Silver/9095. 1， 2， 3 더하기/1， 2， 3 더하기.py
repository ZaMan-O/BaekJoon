import sys
I = sys.stdin.readline

list = [_ for _ in range(11)]
list[0] = 1
list[1] = 2
list[2] = 4
for i in range(3, 11):
    list[i] = list[i-1] + list[i-2] + list[i-3]

T = int(I().strip())
for i in range(T):
    print(list[int(I().strip())-1])