from sys import stdin

N = int(stdin.readline().strip())

dp = [0] * 1001

dp[1] = 1
dp[2] = 2
dp[3] = 1

for i in range(4,N+1):
    dp[i] = min(dp[i-1],dp[i-3]) + 1

if dp[N] % 2 == 1:
    print("SK")
else:
    print("CY")