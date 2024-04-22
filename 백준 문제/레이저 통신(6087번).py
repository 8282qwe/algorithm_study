import sys
from heapq import heappush, heappop

input = sys.stdin.readline

INF = int(1e9)

w, h = map(int, input().split())
start = []
board = [list(map(str, input().rstrip())) for _ in range(h)]
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]


def dij():
    dp = [[INF] * (w + 1) for _ in range(h)]
    heap = []
    heappush(heap, (0, start[0][0], start[0][1], 0))
    heappush(heap, (0, start[0][0], start[0][1], 1))
    heappush(heap, (0, start[0][0], start[0][1], 2))
    heappush(heap, (0, start[0][0], start[0][1], 3))

    board[start[0][0]][start[0][1]] = '*'

    while heap:
        value, x, y, direction = heappop(heap)

        if board[x][y] == 'C':
            return value

        if dp[x][y] < value:
            continue

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < h and 0 <= ny < w and board[nx][ny] != "*":
                if direction == i and value <= dp[nx][ny]:
                    dp[nx][ny] = value
                    heappush(heap, (value, nx, ny, direction))

                elif direction != i and value + 1 <= dp[nx][ny]:
                    dp[nx][ny] = value + 1
                    heappush(heap, (value + 1, nx, ny, i))


for i in range(h):
    for j in range(w):
        if board[i][j] == 'C':
            start.append([i, j])

print(dij())
