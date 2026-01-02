import sys
I = sys.stdin.readline

N = (int)(I().strip())
T = (int)(I().strip())
hand = list(map(int, I().split()))
num = list(map(int, I().split()))
d = []
pos = 0

for i in range(T):
    pos = (pos+num[i]-1) % (N * 2)
    d.append(hand[pos])
print(*d)