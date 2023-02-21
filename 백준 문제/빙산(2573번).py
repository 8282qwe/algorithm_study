from collections import deque

n, m = map(int, input().split())

graph = []

year = 0

for _ in range(n):
    x = list(map(int, input().split()))
    graph.append(x)

def bfs(x,y):
    q = deque()
    q.append((x,y))
    visited[x][y] = True

    while q:
        x,y = q.popleft()
        visited[x][y] = True

        for (mx,my) in ((x,y-1),(x,y+1),(x-1,y),(x+1,y)):
            if 0<=mx<n and 0<=my<m:
                if not visited[mx][my]:
                    if graph[mx][my] == 0:
                        if graph[x][y] == 0:
                            continue
                        graph[x][y] -= 1
                    else:
                        q.append((mx,my))
                        visited[mx][my] = True
    return True

while True:
    count = 0
    visited = [[False] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if graph[i][j] != 0 and not visited[i][j]:
                if bfs(i,j):
                    count += 1

    if count >= 2:
        print(year)
        break
    elif count == 0:
        print(0)
        break
    else:
        year += 1
