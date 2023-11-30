import sys
input = sys.stdin.readline

n = int(input())
board = list(map(int, input().rstrip().split()))

dp = [1] * n
for i in range(1,n):
    for j in range(i):
        if board[j] < board[i]:
            dp[i] = max(dp[i],dp[j]+1)

dpMax = max(dp)
print(dpMax)
dpList = []
for i in range(n-1,-1,-1):
    if dp[i] == dpMax:
        dpMax -= 1
        dpList.append(board[i])
dpList.reverse()
for i in dpList:
    print(i,end=" ")
