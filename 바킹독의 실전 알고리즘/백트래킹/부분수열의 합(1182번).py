import sys
input = sys.stdin.readline

n,s = map(int, input().rstrip().split())
numList = list(map(int, input().rstrip().split()))
cnt = 0
numSum = 0
def dfs(a):
    global cnt
    global numSum
    if numSum == s:
        cnt += 1

    for i in range(a,n):
        numSum += numList[i]
        dfs(i+1)
        numSum -= numList[i]
dfs(0)
if s == 0: cnt -= 1
print(cnt)