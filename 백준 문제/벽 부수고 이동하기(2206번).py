import sys

input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, list(input().rstrip()))))
visited = [[[0 for _ in range(m)] for _ in range(n)] for _ in range(2)]
visited[0][0][0] = 1  # 시작위치
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
queue = deque([(0, 0, 0)])  # 맨앞:높이차원:0  벽안부심:1 벽부심 , i , j
while queue:
    broken, i, j = queue.popleft()
    if i == n - 1 and j == m - 1:
        print(visited[broken][i][j])
        sys.exit()
    for d in range(4):
        ni = i + di[d]
        nj = j + dj[d]
        if 0 <= ni < n and 0 <= nj < m:
            if not broken and arr[ni][nj] == 1:  # 다음이 벽(1)인데 부신적 없으면
                visited[1][ni][nj] = visited[0][i][j] + 1
                queue.append((1, ni, nj))
            elif not arr[ni][nj] and not visited[broken][ni][nj]:  # 다음 벽 아니면서 방문한적 없는 칸이면
                visited[broken][ni][nj] = visited[broken][i][j] + 1
                queue.append((broken, ni, nj))
else:
    print(-1)
