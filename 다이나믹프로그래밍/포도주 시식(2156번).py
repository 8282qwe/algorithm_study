import sys
input = sys.stdin.readline

n = int(input())

num_list = [int(input()) for _ in range(n)]

dp = [0] * n
dp[0] = num_list[0]
if n >= 2:
    dp[1] = num_list[0]+num_list[1]
if n >= 3:
    dp[2] = max(num_list[1] + num_list[2],dp[1],num_list[0]+num_list[2])

for i in range(3,n):
    dp[i] = max(dp[i-1],dp[i-2]+num_list[i],dp[i-3]+num_list[i-1]+num_list[i])

print(max(dp))