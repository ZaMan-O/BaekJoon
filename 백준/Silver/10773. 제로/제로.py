import sys
I = sys.stdin.readline
stack = []
tc = int(I().strip())
sum = 0
for _ in range(tc):
    num = int(I().strip())
    if num == 0:
        stack.pop()
    else:
        stack.append(num)

for num in stack:
    sum += num
print(sum)