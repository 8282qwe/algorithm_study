N,M = map(int, input().split())

matrix = []
dp = [[[float('inf')] * 3 for _ in range(M)] for _ in range(N)]

for _ in range(N):
    matrix.append(list(map(int, input().split(" "))))

for i in range(M):
    dp[0][i] = [matrix[0][i] for _ in range(3)]


for i in range(1,N):
    for j in range(M):
        for k in range(3):
            if (j == 0 and k == 2) or (j==M-1 and k == 0):
                continue
            for l in range(3):
                if k == l:
                    continue
                dp[i][j][k] = min(dp[i][j][k],dp[i-1][j-k+1][l] + matrix[i][j])

minimum = float('inf')
for x in dp[N-1]:
    for y in x:
        minimum = min(minimum,y)

print(minimum)