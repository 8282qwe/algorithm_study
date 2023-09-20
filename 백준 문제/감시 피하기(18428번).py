from collections import deque
import copy

n = int(input())

data = []
#방향 설정 상,하,좌,우
dx = [0,0,-1,1]
dy = [-1,1,0,0]

t_list = []
result = True
for i in range(n):
    data.append(list(map(str, input().split())))
    for j in range(n):
        if data[i][j] == 'T':
            t_list.append((i,j))

def wall(count):
    global result

    if count == 3:
        test_map = copy.deepcopy(data)
        result = True
        for teacher in t_list:
            for k in range(4):
                dfs(k,teacher[0],teacher[1],test_map)
        if result:
            print("YES")
            exit(0)
        return

    for i in range(n):
        for j in range(n):
            if data[i][j] == 'X':
                data[i][j] = 'O'
                count += 1
                wall(count)
                count -= 1
                data[i][j] = 'X'


def dfs(k,x,y,test_map):
    global result

    nx = x + dx[k]
    ny = y + dy[k]

    if 0 <= nx < n and 0 <= ny < n:
        if test_map[nx][ny] == 'S':
            result = False
        if test_map[nx][ny] == 'X':
            test_map[nx][ny] = 'T'
            dfs(k,nx,ny,test_map)
        if test_map[nx][ny] == 'T':
            dfs(k,nx,ny,test_map)


wall(0)
print("NO")