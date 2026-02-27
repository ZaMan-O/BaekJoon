import sys
I = sys.stdin.readline

ground = []
N, M, B = map(int, I().split())
max_h, min_h = 0, 256
result_t, result_h = 999999999, 0
for _ in range(N):
    h = list(map(int, I().split()))
    ground.append(h)
    max_h = max(max_h, max(h))
    min_h = min(min_h, min(h))

for i in range(min_h, max_h+1):
    destroy = 0
    built = 0
    for ii in ground:
        for iii in ii:
            if iii >= i:
                destroy += iii - i
            else:
                built += i - iii
    if built <= B + destroy:
        if destroy * 2 + built <= result_t:
            result_t = destroy * 2 + built
            result_h = i
print(result_t, result_h)