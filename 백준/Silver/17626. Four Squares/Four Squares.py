import sys
I = sys.stdin.readline

dp = [_ for _ in range(50001)]
dp[1] = 1
dp[0] = 0
for i in range(2, 50001):
    ii = 1
    m = 4
    while True:
        if pow(ii,2) > i:
            break
        m = min(m, dp[i - pow(ii, 2)])
        ii += 1
    dp[i] = m + 1

n = int(I().strip())
print(dp[n])