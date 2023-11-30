import sys
input = sys.stdin.readline

n,m = map(int,input().rstrip().split())
s = []

def dfs(q):
    if len(s) == m:
        print(' '.join(map(str,s)))
        return

    for i in range(q,n+1):
        s.append(i)
        dfs(i)
        s.pop()
dfs(1)