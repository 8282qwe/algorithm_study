import sys
input = sys.stdin.readline

graphs = []
find_0 = []
for i in range(9):
    graphs.append(list(map(int,input().rstrip().split())))
    for j in range(9):
        if graphs[i][j] == 0:
            find_0.append((i,j))

def check_row(target,i):
    buf = graphs[target]
    if i in buf:
        return False
    return True

def check_low(target,i):
    buf = [graphs[a][target] for a in range(9)]
    if i in buf:
        return False
    return True

def check_box(target_x,target_y,i):
    target_x = target_x//3*3
    target_y = target_y//3*3
    for a in range(target_x,target_x+3):
        for b in range(target_y,target_y+3):
            if graphs[a][b] == i:
                return False
    return True

def dfs(idx):
    if idx == len(find_0):
        for i in graphs:
            print(*i)
        exit(0)

    for i in range(1,10):
        x,y = find_0[idx]

        if check_row(x,i) and check_low(y,i) and check_box(x,y,i):
            graphs[x][y] = i
            dfs(idx+1)
            graphs[x][y] = 0
dfs(0)
