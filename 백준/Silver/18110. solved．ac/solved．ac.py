import sys
I = sys.stdin.readline
tc = int(I().strip())
if tc == 0:
    print(0)
    sys.exit()
stack = []
jul_sa_pyung_gyun = 0
sum = 0

if tc / 20 * 3 - int(tc / 20 * 3) >= 0.5:
    jul_sa_pyung_gyun = int(tc / 20 * 3 + 0.5)
else:
    jul_sa_pyung_gyun = int(tc / 20 * 3)

for i in range(tc):
    stack.append(int(I().strip()))

stack.sort()
tc -= jul_sa_pyung_gyun * 2

for i in range(jul_sa_pyung_gyun, len(stack) - jul_sa_pyung_gyun):
    sum += stack[i]

if sum / tc - int(sum / tc) >= 0.5:
    sum = int(sum / tc + 0.5)
else:
    sum = int(sum / tc)
print(sum)