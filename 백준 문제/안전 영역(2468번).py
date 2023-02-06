from collections import deque

n = int(input())

board = []
max_num = 0

for _ in range(n):
    x = list(map(int,input().split()))
    board.append(x)
    if max(x) > max_num:
        max_num = max(x)

def bfs(a,b,h):
    q = deque()
    q.append((a,b))
    visited[a][b] = True

    while q:
        x,y = q.popleft()

        for (mx,my) in ((x,y-1),(x,y+1),(x-1,y),(x+1,y)):
            if 0 <= mx < n and 0 <= my < n:
                if not visited[mx][my] and board[mx][my] > h:
                    q.append((mx,my))
                    visited[mx][my] = True

max_count = 0
for i in range(0,max_num):
    visited = [[False] * n for _ in range(n)]
    count = 0
    for x in range(n):
        for y in range(n):
            if not visited[x][y] and board[x][y] > i:
                bfs(x,y,i)
                count += 1
    max_count = max(max_count,count)

print(max_count)
