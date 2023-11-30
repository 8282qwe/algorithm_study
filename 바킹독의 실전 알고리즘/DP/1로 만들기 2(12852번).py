import sys
input = sys.stdin.readline

n = int(input())

dp = [0] * 1000001
pre = [0] * 1000001

for i in range(2,n+1):
    dp[i] = dp[i-1] + 1
    pre[i] = i-1
    if i % 2 == 0 and dp[i] > dp[i//2] + 1:
        dp[i] = dp[i//2] + 1
        pre[i] = i//2
    if i % 3 == 0 and dp[i] > dp[i//3] + 1:
        dp[i] = dp[i//3] + 1
        pre[i] = i//3

print(dp[n])
while True:
    print(n, end=' ')
    if n == 1: break
    n = pre[n]