import sys
I = sys.stdin.readline

A, B, V = map(int, I().split())
day = (V - A) // (A - B)
if (V - A) % (A - B):
    day += 1
day += 1
print(day)