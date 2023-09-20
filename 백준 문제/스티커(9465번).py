import sys
input = sys.stdin.readline

T = int(input())
res = [] * T

def find_max(n):
    dp[0][0] = board[0][0]
    dp[1][0] = board[1][0]
    dp[0][1] = dp[1][0] + board[0][1]
    dp[1][1] = dp[0][0] + board[1][1]
    for j in range(n):
        for i in range(2):
            if i == 0:
                dp[i][j] = max(dp[i+1][j-1],dp[i+1][j-2]) + board[i][j]
            else:
                dp[i][j] = max(dp[i-1][j-1],dp[i-1][j-2]) + board[i][j]
    return max(dp[0][-1],dp[1][-1])

for _ in range(T):
    n = int(input())
    board = []
    dp = [[0] * n for _ in range(2)]
    for _ in range(2):
        board.append(list(map(int, input().split())))
    res.append(find_max(n))

for i in res:
    print(i)