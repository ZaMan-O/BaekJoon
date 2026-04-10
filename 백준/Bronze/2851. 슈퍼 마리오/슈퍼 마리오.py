total = 0
for i in range(10):
    N=int(input())
    if abs(100-total-N) <= abs(100-total):
        total += N
    else:
        for _ in range(9-i):
            N=int(input())
        break
print(total)