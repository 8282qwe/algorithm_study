from collections import deque

n, k = map(int, input().split())

data = []
virus = []

for i in range(n):
    data.append(list(map(int,input().split())))
    for j in range(n):
        if data[i][j] != 0:
            virus.append((data[i][j],i,j,0))
virus.sort()
s,x,y = map(int, input().split())

q = deque(virus)

while q:
    virus_number, nx, ny, time = q.popleft()

    if time >= s:
        break

    for dx, dy in (nx + 1, ny), (nx - 1, ny), (nx, ny + 1), (nx, ny - 1):
        if 0 <= dx < n and 0 <= dy < n:
            if data[dx][dy] == 0:
                data[dx][dy] = virus_number
                q.append((virus_number, dx, dy,time+1))

print(data[x-1][y-1])
