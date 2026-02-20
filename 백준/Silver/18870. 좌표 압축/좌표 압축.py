import sys
I = sys.stdin.readline

N = int(I().strip())
pos = list(map(int, I().split()))
pos2 = sorted(set(pos))
dic = {pos2[i]:i for i in range(len(pos2))}
for i in pos:
    print(dic[i], end=' ')