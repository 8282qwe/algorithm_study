import sys
input = sys.stdin.readline

n = int(input())
isUsed1 = [False] * n
isUsed2 = [False] * (2*n-1)
isUsed3 = [False] * (2*n-1)
cnt = 0
def dfs(a):
    global cnt
    if a == n:
        cnt += 1
        return
    for i in range(n):
        if isUsed1[i] or isUsed2[i+a] or isUsed3[a-i+n-1]: continue
        isUsed1[i] = True
        isUsed2[i+a] = True
        isUsed3[a-i+n-1] = True
        dfs(a+1)
        isUsed1[i] = False
        isUsed2[i + a] = False
        isUsed3[a - i + n - 1] = False
dfs(0)
print(cnt)