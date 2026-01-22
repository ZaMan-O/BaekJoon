import sys
I = sys.stdin.readline

list = [_ for _ in range(1000)]
list[0] = 1
list[1] = 2
for i in range(2,1000):
    list[i] = list[i-2] + list[i-1]
print(list[int(I().strip())-1] % 10007)