n = int(input())

dp = [1 for _ in range(n)]

data = list(map(int, input().split()))

for i in range(n):
    for j in range(i):
        if data[i] < data[j]:
            dp[i] = max(dp[i],dp[j]+1)

print(len(data) - max(dp))