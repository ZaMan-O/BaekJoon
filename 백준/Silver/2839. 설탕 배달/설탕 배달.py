import sys
I = sys.stdin.readline

sugar = int(I().strip())
can_split = False
five_pojang_num = 0

for i in range(sugar//5, -1, -1):
    if (sugar - i * 5) % 3 == 0:
        can_split = True
        five_pojang_num = i
        break

if can_split == False:
    print(-1)
else:
    print(five_pojang_num + (sugar - i * 5) // 3)