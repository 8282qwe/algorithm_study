from collections import deque

n, l, r = map(int, input().split())

data = []
unions = -1

for _ in range(n):
    data.append(list(map(int, input().split())))

def bfs(x,y):
    global unions

    q = deque()
    q.append((x,y))

    p = []
    p.append((x,y))

    total = data[x][y]

    while q:
        x, y = q.popleft()
        visited[x][y] = True

        for nx,ny in ((x+1,y),(x-1,y),(x,y+1),(x,y-1)):
            if nx >= n or nx < 0 or 0 > ny or ny >= n:
                continue

            if l <= abs(data[x][y] - data[nx][ny]) <= r and not visited[nx][ny]:
                q.append((nx,ny))
                p.append((nx,ny))
                visited[nx][ny] = True
                total += data[nx][ny]
                unions += 1

    total /= len(p)

    for i,j in p:
        data[i][j] = int(total)

years = 0
while unions != 0:
    unions = 0
    visited = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                bfs(i,j)
    years += 1

print(years-1)