import sys
input = sys.stdin.readline
from collections import deque

n,m = map(int, input().rstrip().split())

board = []
distf = [[0] * m for _ in range(n)]
distj = [[0] * m for _ in range(n)]
qf = deque([])
qj = deque([])

for i in range(n):
    buf = list(input().rstrip())
    board.append(buf)
    for idx,j in enumerate(buf):
        if j == 'F':
            qf.append((i,idx))
            distf[i][idx] = 1
        if j == 'J':
            qj.append((i,idx))
            distj[i][idx] = 1

move = [(-1,0),(1,0),(0,-1),(0,1)]

while qf:
    curX,curY = qf.popleft()
    for i,j in move:
        nx = curX + i
        ny = curY + j
        if 0 <= nx < n and 0 <= ny < m:
            if board[nx][ny] != '#' and not distf[nx][ny]:
                distf[nx][ny] = distf[curX][curY] + 1
                qf.append((nx,ny))

dist = int(1e9)

while qj:
    curX,curY = qj.popleft()
    for i,j in move:
        nx = curX + i
        ny = curY + j
        if 0 <= nx < n and 0 <= ny < m:
            if board[nx][ny] != '#' and not distj[nx][ny]:
                distj[nx][ny] = distj[curX][curY] + 1
                qj.append((nx,ny))
        else:
            dist = min(dist,distj[curX][curY])
if dist == int(1e9):
    print("IMPOSSIBLE")
else:
    print(dist)