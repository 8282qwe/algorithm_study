import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int, input().rstrip().split())
visited = [False for _ in range(n+1)]
matrix = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().rstrip().split())
    matrix[a].append(b)
    matrix[b].append(a)

def bfs(a):
    q = deque()
    q.append(a)
    visited[a] = True
    while q:
        node = q.popleft()

        for i in matrix[node]:
            if not visited[i]:
                q.append(i)
                visited[i] = True

componets = 0
for i in range(1,n+1):
    if not visited[i]:
        componets+=1
        bfs(i)

print(componets)

