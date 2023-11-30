import sys
input = sys.stdin.readline

t = int(input())
num_list = [int(input()) for _ in range(t)]
num_max = max(num_list)
dp = [0,1,1,1,2,2]

for i in range(6,num_max+1):
    dp.append(dp[i-3]+dp[i-2])

for i in num_list:
    print(dp[i])