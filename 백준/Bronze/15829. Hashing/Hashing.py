import sys
input = sys.stdin.readline

length = int(input().strip())
s = input().strip()

length = int(length)
total = 0

for i in range(length):
    now = ord(s[i]) - 96
    total += now * pow(31, i)
    total %= 1234567891
print(total)