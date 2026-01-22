import sys
I = sys.stdin.readline

dp = [_ for _ in range(101)]
dp[0] = 1
dp[1] = 1
dp[2] = 1
dp[3] = 2
dp[4] = 2
for i in range(5,101):
    dp[i] = dp[i-1] + dp[i-5]

T = int(I().strip())
for _ in range(T):
    print(dp[int(I().strip()) - 1])