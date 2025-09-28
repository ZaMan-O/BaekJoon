import sys
I = sys.stdin.readline
tc = int(I().strip())
result = []

for _ in range(tc):
    N, M = map(int, I().split())
    queue = list(map(int, I().split()))
    head = 0
    printed = 0
    WantIndex = True
    while WantIndex:
        if len(queue) == 1:
            WantIndex = False
            printed += 1
            continue
        for i in range(len(queue)):
            if i == 0:
                head = queue[i]
                continue
            if queue[i] > head:
                temp = head
                queue.append(temp)
                queue.pop(0)
                M = len(queue) - 1 if M - 1 < 0 else M - 1
                break
            if i == len(queue) - 1:
                queue.pop(0)
                printed += 1
                if M == 0:
                    WantIndex = False
                M = len(queue) - 1 if M - 1 < 0 else M - 1
    result.append(printed)

for num in result:
    print(num)