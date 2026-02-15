import sys
import re
I = sys.stdin.readline

N = I().strip()
num = list(map(int, re.split('[+-]', N)))
oper = re.findall(r'[+-]', N)
result = num[0]
now_minus = False
tm = 0
for i in range(len(num)):
    if i == 0:
        continue
    if oper[i-1] == '-':
        if now_minus:
            result -= tm
            tm = num[i]
        else:
            now_minus = True
            tm += num[i]
    else:
        if now_minus:
            tm += num[i]
        else:
            result += num[i]
result -= tm
print(result)