import sys
I = sys.stdin.readline

N = int(I().strip())
s = [int(I().strip()) for _ in range(N)]
dp = [0 for _ in range(N)]
for i in range(N):
    if i == 0:
        dp[i] = s[i]
    elif i == 1:
        dp[i] = s[i-1] + s[i]
    elif i == 2:
        dp[i] = max(s[0] + s[2], s[1] + s[2])
    else:
        dp[i] = max(dp[i-3] + s[i-1] + s[i], dp[i-2] + s[i])
print(dp[N-1])