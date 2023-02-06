from collections import deque

n, m, h = map(int, input().split())

all_box = [[] for _ in range(h)]

q = deque()

#h(높이),m(세로),n(가로) 순서
for i in range(h):
    for _ in range(m):
        in_data = list(map(int, input().split()))
        all_box[i].append(in_data)

for i in range(h):
    for j in range(m):
        for k in range(n):
            if all_box[i][j][k] == 1:
                q.append((i,j,k))

def bfs():
    while q:
        z,y,x = q.popleft()

        for (mz,my,mx) in ((z,y,x+1),(z,y,x-1),(z,y+1,x),(z,y-1,x),(z+1,y,x),(z-1,y,x)):
            if 0 <= mz < h and 0 <= my < m and 0 <= mx < n:
                if all_box[mz][my][mx] == 0:
                    all_box[mz][my][mx] = all_box[z][y][x] + 1
                    q.append((mz,my,mx))
bfs()
result = 0

for i in all_box:
    for j in i:
        if 0 in j:
            print(-1)
            exit()
        result = max(max(j),result)
print(result - 1)