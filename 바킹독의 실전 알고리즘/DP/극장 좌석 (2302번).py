import sys
input = sys.stdin.readline

n = int(input())
vip = int(input())
vips = [int(input()) for _ in range(vip)]

sites = 1
dp = [1]+[1]*n
dp[1] = 1

for i in range(2,n+1):
    if i in vips:
        dp[i] = dp[i-1]
        continue
    if i-1 in vips:
        dp[i] = dp[i-2]
        continue
    dp[i] = dp[i-1]+dp[i-2]

print(dp[n])