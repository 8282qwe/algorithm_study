sequence1 = str(input())
sequence2 = str(input())

dp = [[0] * (len(sequence1)+1) for _ in range(len(sequence2)+1)]

for i in range(len(sequence2)+1):
    for j in range(len(sequence1)+1):
        if i == 0 or j == 0:
            dp[i][j] = 0
        elif sequence1[j-1] == sequence2[i-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j],dp[i][j-1])

print(dp[-1][-1])