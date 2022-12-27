from collections import deque

n,m = map(int, input().split())

graph = []

for i in range(n):
    graph.append(list(map(int, input())))

dx = [0,0,-1,1]
dy = [-1,1,0,0]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))

    while queue:
        x, y = queue.popleft()

        for j in range(4):
            mx = x+dx[j]
            my = y+dy[j]

            if mx < 0 or mx >= n or my < 0 or my >= m:
                continue

            if graph[mx][my] == 0:
                continue

            if graph[mx][my] == 1:
                graph[mx][my] = graph[x][y] + 1
                queue.append((mx,my))

    return graph[n-1][m-1]

print(bfs(0,0))