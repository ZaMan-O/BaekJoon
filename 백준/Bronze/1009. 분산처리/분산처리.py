import sys
I = sys.stdin.readline

T = int(I().strip())
for _ in range(T):
    a,b = map(int, I().split())
    now = 1
    b = b % 4
    if b == 0:
        b = 4
    for _ in range(b):
        now = now * a % 10
        if now == 0:
            now = 10
    print(now)