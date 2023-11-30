import sys
input = sys.stdin.readline

n = int(input())
num = list(map(int, input().rstrip().split()))

dp = [1 for _ in range(n)]
dp[0] = 1
for i in range(1,n):
    for j in range(i):
        if num[i] > num[j]:
            dp[i] = max(dp[j] + 1,dp[i])
print(max(dp))