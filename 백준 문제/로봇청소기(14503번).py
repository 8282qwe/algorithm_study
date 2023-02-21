n,m = map(int, input().split())

#(c,r)
r,c,d = map(int, input().split())

board = []

dx = [-1,0,1,0]
dy = [0,1,0,-1]
#후진 (v+2) % 4
count = 0

for _ in range(n):
    x = list(map(int, input().split()))
    board.append(x)

def dfs(x, y, d):
    global count

    if board[x][y] == 0:
        board[x][y] = 2
        count += 1
    for _ in range(4):
        md = (d+3) % 4
        if board[x+dx[md]][y+dy[md]] == 0:
            dfs(x+dx[md],y+dy[md],md)
            return
        d = md
    md = (d+2) % 4
    if board[x+dx[md]][y+dy[md]] == 1:
        return
    dfs(x+dx[md],y+dy[md],d)

dfs(r,c,d)
print(count)
