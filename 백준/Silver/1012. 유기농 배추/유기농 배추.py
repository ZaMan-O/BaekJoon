import sys
I = sys.stdin.readline

T = int(I().strip())
for _ in range(T):
    M, N, K = map(int, I().split())
    farm = [[0] * M for _ in range(N)]
    need = 0
    pos = []
    for _ in range(K):
        x, y = map(int, I().split())
        farm[y][x] = 1
        pos.append([x, y])
    for i in range(K):
        if farm[pos[i][1]][pos[i][0]] == 2:
            continue
        need += 1
        s = [pos[i]]
        while(s):
            x, y = s.pop()
            farm[y][x] = 2
            if x+1 < M and farm[y][x+1] == 1:
                s.append([x+1, y])
            if x-1 >= 0 and farm[y][x-1] == 1:
                s.append([x-1, y])
            if y+1 < N and farm[y+1][x] == 1:
                s.append([x, y+1])
            if y-1 >= 0 and farm[y-1][x] == 1:
                s.append([x, y-1])
    print(need)