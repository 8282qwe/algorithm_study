N = int(input())

board = [list(map(int, input().split(' '))) for _ in range(N)]

for i in board:
    rank = 1
    for j in range(N):
        if i[0] < board[j][0] and i[1] < board[j][1]:
            rank+=1
    i.append(rank)

for i in board:
    print(i[2], end=" ")