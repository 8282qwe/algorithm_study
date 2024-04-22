import sys
input = sys.stdin.readline

t = int(input())

num_list = [int(input()) for _ in range(t)]
max_num = max(num_list)
dp = [0] * (max_num+1)

dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in range(4,max_num+1):
    dp[i] = (dp[i-1] + dp[i-2] + dp[i-3])%1000000009

for i in num_list:
    print(dp[i])