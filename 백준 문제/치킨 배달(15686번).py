import sys
from itertools import combinations
input = sys.stdin.readline
INF = int(1e9)
board = []

n,m = map(int, input().split())

for _ in range(n):
    board.append(list(map(int, input().split())))

chickens = []
houses = []

for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            houses.append((i,j))
        elif board[i][j] == 2:
            chickens.append((i,j))

res = INF

chickens_com = list(combinations(chickens,m))

def check_load(ch_list):
    buf = 0
    for i in houses:
        buf += min_load(i,ch_list)
    return buf

def min_load(a, b):
    c = INF
    for i in b:
        c = min(c, abs(a[0]-i[0])+abs(a[1]-i[1]))
    return c

for i in chickens_com:
    res = min(res, check_load(i))
print(res)