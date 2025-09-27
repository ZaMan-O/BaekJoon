import sys
I = sys.stdin.readline
stack = []
correct_list = []
while True:
    str = I().rstrip()
    if str == ".":
        break
    for i in range(len(str)):
        if i == len(str) - 1:
            if len(stack) == 0:
                correct_list.append(True)
            else:
                correct_list.append(False)
            break
        if str[i] == "(":
            stack.append(1)
        elif str[i] == "[":
            stack.append(3)
        elif str[i] == ")":
            if len(stack) == 0:
                correct_list.append(False)
                break
            if stack[-1] != 1:
                correct_list.append(False)
                break
            stack.pop()
        elif str[i] == "]":
            if len(stack) == 0:
                correct_list.append(False)
                break
            if stack[-1] != 3:
                correct_list.append(False)
                break
            stack.pop()
    stack.clear()

for i in range(len(correct_list)):
    if correct_list[i]:
        print("yes")
    else:
        print("no")