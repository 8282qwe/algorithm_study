from collections import deque

n, m = map(int,input().split())

board = []
for i in range(n):
    x = list(map(int,input()))
    board.append(x)

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))

    while queue:
        x,y = queue.popleft()
        for i in range(4):
            mx = x + dx[i]
            my = y + dy[i]
            if mx < 0 or mx >= n or my < 0 or my >= m:
                continue
            if board[mx][my] == 0:
                continue

            if board[mx][my] == 1:
                board[mx][my] = board[x][y] + 1
                queue.append((mx,my))
    return board[n-1][m-1]

print(bfs(0,0))