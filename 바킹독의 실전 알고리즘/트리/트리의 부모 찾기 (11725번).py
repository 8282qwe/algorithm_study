import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

n = int(input())
matrix = [[] for _ in range(n+1)]
p = [None for _ in range(n+1)]

for _ in range(n-1):
    i,j = map(int, input().rstrip().split())
    matrix[i].append(j)
    matrix[j].append(i)

def dfs(a):
    for i in matrix[a]:
        if p[a] == i: continue
        p[i] = a
        dfs(i)
dfs(1)
print(*p[2:])