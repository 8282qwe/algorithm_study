import sys
input = sys.stdin.readline

def fibo(n):
    if n == 0:
        print('0')
        return 0
    elif n == 1:
        print('1')
        return 1
    else:
        return fibo(n-1) + fibo(n-2)

res = []
t = int(input())
for _ in range(t):
    n = int(input())
    dp = [[0,0]] * 41
    dp[0] = [1,0]
    dp[1] = [0,1]

    for i in range(2,n+1):
        dp[i] = [dp[i-1][0]+dp[i-2][0],dp[i-1][1]+dp[i-2][1]]
    res.append(dp[n])

for i in res:
    print(*i)
#n = 1  1
#n = 2  10
#n = 3 101
#n=4 10110
#n=5 10110101