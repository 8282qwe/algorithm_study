N = int(input())

board = list(map(int, input().split()))
board.insert(0,None)

M = int(input())

for _ in range(M):
    gender, number = map(int, input().split())

    if gender == 1:
        inc = 1
        while number <= N:
            board[number] = (board[number] + 1) % 2
            inc += 1
            number *= inc

    elif gender == 2:
        board[number] = (board[number] + 1) % 2

        left = number - 1
        right = number + 1
        while left >= 1 and right <= 8:
            if board[left] == board[right]:
                board[left] = (board[left] + 1) % 2
                board[right] = (board[right] + 1) % 2
                left -= 1
                right += 1
            else:
                break

for i in range(1,N+1):
    print(board[i], end=' ')
    if i % 20 == 0:
        print()

