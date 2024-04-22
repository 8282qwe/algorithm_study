import sys
from heapq import heappush,heappop
from collections import Counter
input = sys.stdin.readline

m,n = map(int, input().rstrip().split())

q = []
cnt = 0
board = []
for i in range(n):
    board.append(list(map(int, input().rstrip().split())))
    cnt += Counter(board[-1])[0]
    for j in range(m):
        if board[-1][j] == 1:
            heappush(q,(1,i,j))
while q:
    day,y,x = heappop(q)

    for (i,j) in [(0,1),(0,-1),(1,0),(-1,0)]:
        dx = x+i
        dy = y+j
        if 0 <= dx < m and 0 <= dy < n:
            if board[dy][dx] == 0:
                board[dy][dx] = day+1
                heappush(q,(day+1,dy,dx))
                cnt -= 1

if cnt != 0:
    print(-1)
else:
    print(day-1)