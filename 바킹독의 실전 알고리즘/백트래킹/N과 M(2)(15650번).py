import sys
input = sys.stdin.readline

n,m = map(int,input().rstrip().split())
s = []

def dfs(q):
    if len(s) == m:
        print(' '.join(map(str,s)))

    for i in range(q+1,n+1):
        if i not in s:
            s.append(i)
            dfs(i)
            s.pop()
dfs(0)