import sys
I = sys.stdin.readline

tc = int(I().strip())
arr = []
result = []
can_make = True
for _ in range(tc):
    arr.append(int(I().strip()))

stack = []
top = -1
now_num = 0
for num in arr:
    if num < now_num:
        if stack[top] == num:
            stack.pop(top)
            top -= 1
            result.append(0)
        else:
            can_make = False
            break
    else:
        for _ in range(num - now_num):
            now_num += 1
            stack.append(now_num)
            top += 1
            result.append(1)
        result.append(0)
        stack.pop(top)
        top -= 1
    #print(result)
if can_make:
    for i in result:
        if i == 1:
            print("+")
        else:
            print("-")
else:
    print("NO")