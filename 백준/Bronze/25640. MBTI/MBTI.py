import sys
I = sys.stdin.readline

str = I().strip()
n = int(I().strip())
total = 0
for _ in range(n):
    str2 = I().strip()
    if str == str2:
        total += 1
print(total)