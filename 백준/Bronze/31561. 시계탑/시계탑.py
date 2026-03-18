import sys
I = sys.stdin.readline

M = int(I().strip())
time = 0
if M <= 30:
    time = M / 2
else:
    time = M*1.5 - 30
print("{:.1f}".format(time))