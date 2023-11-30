import sys
input = sys.stdin.readline

n = int(input())
childs = [int(input()) for _ in range(n)]

dp = [1] * n

for i in range(1,n):
    for j in range(i):
        if childs[i] > childs[j]:
            dp[i] = max(dp[i],dp[j]+1)
print(n-max(dp))