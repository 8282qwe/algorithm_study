import sys
input = sys.stdin.readline

n = int(input())
card_list = [0] + list(map(int,input().rstrip().split()))
dp = [0] * (n+1)

for i in range(1,n+1):
    for j in range(1,i+1):
        dp[i] = max(dp[i-j]+card_list[j],dp[i])
print(dp[i])
