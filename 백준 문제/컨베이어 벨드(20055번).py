n,k = map(int,input().split())

board = list(map(int,input().split()))
robot = [False] * n
counter = 0


while board.count(0) < k:
    board.insert(0,board.pop(-1))
    robot.insert(0,robot.pop(-1))
    if robot[n-1]:
        robot[n-1] = False

    for i in range(n-2,0,-1):
        if robot[i]:
            if board[i+1] > 0 and not robot[i+1]:
                robot[i] = False
                robot[i+1] = True
                board[i+1] -= 1
    if robot[n-1]:
        robot[n-1] = False
    if not robot[0] and board[0] > 0:
        robot[0] = True
        board[0] -= 1
    counter += 1
print(counter)