import sys
input = sys.stdin.readline

n,c = map(int, input().rstrip().split())
board = []
for _ in range(n): board.append(int(input().rstrip()))
board.sort()

start,end = 1,board[-1]-board[0]
res = 0

while start <= end:
    mid = (start + end) // 2
    value = board[0]
    count = 1
    for i in range(1,n):
        if board[i] >= value+mid:
            count += 1
            value = board[i]
    if count >= c:
        start = mid + 1
        res = mid
    else:
        end = mid - 1

print(res)