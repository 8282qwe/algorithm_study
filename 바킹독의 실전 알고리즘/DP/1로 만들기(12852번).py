import sys

n = int(sys.stdin.readline())

dp = [int(1e9)] * (n+1)
dp[1] = 0

for i in range(2,n+1):
    dp[i] = dp[i - 1] + 1
    if i % 3 == 0:
        dp[i] = min(dp[i//3]+1,dp[i])
    if i % 2 == 0:
        dp[i] = min(dp[i // 2] + 1, dp[i])


dpMax = dp[n]-1
print(dp[n])
res = [n]
now = n

for i in range(n, 0, -1):
    if dp[i] == dpMax and (i+1 == now or i*2 == now or i*3 == now):
        now = i
        res.append(i)
        dpMax -= 1
print(*res)