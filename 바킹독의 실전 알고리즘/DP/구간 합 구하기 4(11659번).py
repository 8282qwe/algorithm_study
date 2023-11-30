import sys
input = sys.stdin.readline

n,m = map(int, input().rstrip().split())
numList = list(map(int, input().rstrip().split()))
dp = [0] * n
dp[0] = numList[0]

for i in range(1,n):
    dp[i] = dp[i-1] + numList[i]

for _ in range(m):
    i,j = map(int,input().rstrip().split())
    i -= 2
    if i < 0:
        print(dp[j-1])
    else:
        print(dp[j-1] - dp[i])
