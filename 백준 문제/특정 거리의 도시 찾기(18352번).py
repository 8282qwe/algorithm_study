from collections import deque
import sys

n,m,k,x = map(int, sys.stdin.readline().rstrip().split())


citys = [-1] * (n+1)
citys[x] = 0
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a,b = map(int, sys.stdin.readline().rstrip().split())
    graph[a].append(b)

q = deque([x])
while q:
    start = q.popleft()

    for dis_node in graph[start]:
        if citys[dis_node] == -1:
            citys[dis_node] = citys[start] + 1
            q.append(dis_node)

check = False
for i in range(1, n+1):
    if citys[i] == k:
        print(i)
        check = True

if not check:
    print(-1)