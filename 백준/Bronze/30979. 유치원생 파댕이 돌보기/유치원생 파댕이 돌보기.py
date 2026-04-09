T = int(input())
N = int(input())
arr = list(map(int, input().split()))
total = 0
for i in arr:
    total += i
if total < T:
    print('Padaeng_i Cry')
else:
    print('Padaeng_i Happy')