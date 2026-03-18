import sys
I = sys.stdin.readline

N = int(I().strip())
L = list(map(int, I().split()))
cr = False
for i in range(1, N//2 + 1):
    cr = True
    for ii in range(i):
        if L[ii] != L[N-i+ii]:
            cr = False
            break
    if cr:
        print("yes")
        break
if not cr:
    print("no")