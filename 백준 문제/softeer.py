import sys

input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())

node_line = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    node_line[a].append(b)

s, e = map(int, input().split())

def bfs(start,end):
    visited = [False] * (n + 1)
    queue = deque()
    visited[start] = True
    flag = False
    for i in node_line[start]:
        queue.append(i)

    while queue:
        num = queue.popleft()
        visited[num] = True
        if num == end:
            flag = True
        else:
            for i in node_line[num]:
                if not visited[i]:
                    queue.append(i)

    return flag


result = 0
for i in range(1, n+1):
    if bfs(s,i) and bfs(i,e):
        print(i)
        result += 1
print(result)