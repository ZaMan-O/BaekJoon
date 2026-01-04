import sys
I = sys.stdin.readline

M, N = map(int, I().split())
a1, a2 = [], []
for _ in range(M):
    a1.append(I().strip())
for _ in range(N):
    a2.append(I().strip())
d = {e:0 for e in a2}
Amount = 0
List = []
for i in a1:
    if d.get(i) == 0:
        Amount += 1
        List.append(i)
List.sort()
print(Amount)
for i in List:
    print(i)