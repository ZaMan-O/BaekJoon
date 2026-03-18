import sys
I = sys.stdin.readline

H,S = map(int, I().split())
if H <= 2:
    print(1)
elif H <= 4:
    print(2 + S)
else:
    print((H + S * 3 + 1) // 2)