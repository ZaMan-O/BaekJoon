import sys
I = sys.stdin.readline

str = I().strip()
for i in str:
    c = ord(i)
    if c < 91:
        print(chr(c+32), end='')
    else:
        print(chr(c-32), end='')