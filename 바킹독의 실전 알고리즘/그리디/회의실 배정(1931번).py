import sys
input = sys.stdin.readline

n = int(input())
board = [list(map(int, input().rstrip().split())) for _ in range(n)]

board.sort(key=lambda x:(x[1],x[0]))
time = 0
cnt = 0
for i in board:
    if time <= i[0]:
        time = i[1]
        cnt += 1
print(cnt)