import sys
input = sys.stdin.readline

n = int(input())
dp = [0] * (n+1)

for i in range(1,n+1):
    t,p = map(int,input().rstrip().split())
    dp[i] = max(dp[i-1],dp[i])
    if i+t <= n+1:
        dp[i+t-1] = max(dp[i+t-1],dp[i-1]+p)
print(dp[-1])