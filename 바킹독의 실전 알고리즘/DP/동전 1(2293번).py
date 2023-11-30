import sys
input = sys.stdin.readline

n,k = map(int,input().rstrip().split())
dp = [0] * (k+1)
coins = [int(input()) for _ in range(n)]

dp[0] = 1
#1 1
#2 11,2
#3 111,21
#4 1111,112,22
#5 11111,1112,122,5
for i in coins:
    for j in range(i,k+1):
        if j-i >= 0:
            dp[j] += dp[j-i]
print(dp[k])