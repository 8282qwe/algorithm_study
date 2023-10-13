N = int(input())

board = []
heart_x = 0
heart_y = 0

for _ in range(N):
    board.append(list(input()))

for i in range(1,N-1):
    for j in range(1,N-1):
        if board[i][j] == "*":
            if board[i-1][j] == "*" and board[i+1][j] == "*" and board[i][j-1] == "*" and board[i][j+1] == "*":
                heart_x = i
                heart_y = j

left_hand = board[heart_x][:heart_y].count("*")
right_hand = board[heart_x][heart_y+1:].count("*")
belt = [board[n][heart_y] for n in range(heart_x+1,N)].count("*")
left_leg = [board[n][heart_y-1] for n in range(heart_x+belt,N)].count("*")
right_leg = [board[n][heart_y+1] for n in range(heart_x+belt,N)].count("*")

print(heart_x+1,heart_y+1)
print(left_hand,right_hand,belt,left_leg,right_leg)