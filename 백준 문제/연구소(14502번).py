n,m = map(int, input().split())

data = []
temp = [[0] * m for _ in range(n)]
dx = [0,0,-1,1]
dy = [-1,1,0,0]
result = 0

for _ in range(n):
    data.append(list(map(int, input().split())))


def virus(x,y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<= nx < n and  0<= ny < m:
            if temp[nx][ny] == 0:
                temp[nx][ny] = 2
                virus(nx,ny)

def get_safety():
    count = 0
    for i in temp:
        for j in i:
            if j == 0:
                count += 1
    return count

def dfs(count):
    global result

    if count == 3:
        for i in range(n):
            for j in range(m):
                temp[i][j] = data[i][j]

        for i in range(n):
            for j in range(m):
                if data[i][j] == 2:
                    virus(i,j)
        result = max(get_safety(),result)
        return

    for i in range(n):
        for j in range(m):
            if data[i][j] == 0:
                data[i][j] = 1
                count += 1
                dfs(count)
                count -= 1
                data[i][j] = 0

dfs(0)
print(result)