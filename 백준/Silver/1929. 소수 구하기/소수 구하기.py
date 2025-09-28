import sys
I = sys.stdin.readline
num_min, num_max = map(int, I().split())

for i in range(num_min, num_max+1):
    if i == 1:
        continue
    if i == 2 or i == 3:
        print(i)
        continue
    for ii in range(2, int(i ** 0.5) + 1):
        if i % ii == 0:
            break
        if ii == int(i ** 0.5):
            print(i)