import sys
input = sys.stdin.readline

n = list(map(int, input().rstrip()))
l = len(n)
dp = [0] * (l+1)

if n[0] == 0:
    print(0)
else:
    n = [0] + n
    dp[0] = dp[1] = 1
    # 1 = a, 11=aa,k,111=aaa,ka,ak, 1111=aaaa,aak,aka,kaa,kk
    for i in range(2,l+1):
        value = n[i-1]*10+n[i]
        if 1<= n[i] <= 9:
            dp[i] += dp[i-1]
        if 10 <= value <= 26:
            dp[i] += dp[i-2]
        dp[i] %= 1000000
    print(dp[-1])