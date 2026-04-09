N, X = map(int, input().split())
result = 0
for _ in range(N):
    a,b = map(int, input().split())
    if a + b <= X:
        if a > result:
            result = a
if result == 0:
    print(-1)
else:
    print(result)