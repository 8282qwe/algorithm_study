import sys
import heapq
input = sys.stdin.readline

def dij(board,n):
    infBoard = [[int(1e9)]*n for _ in range(n)]
    q = []
    infBoard[0][0] = board[0][0]
    heapq.heappush(q,[board[0][0],0,0])

    while q:
        rupee, x,y = heapq.heappop(q)

        if infBoard[x][y] < rupee:
            continue
        for i,j in [[x,y-1],[x,y+1],[x-1,y],[x+1,y]]:
            if 0<= i < n and 0 <= j < n:
                nextRupee = rupee+board[i][j]
                if nextRupee < infBoard[i][j]:
                    infBoard[i][j] = nextRupee
                    heapq.heappush(q,[nextRupee,i,j])
    return infBoard[n-1][n-1]

answer = []
while True:
    n = int(input())
    if n == 0:
        break
    board = [list(map(int, input().rstrip().split()))for _ in range(n)]
    answer.append(dij(board,n))

for idx,i in enumerate(answer):
    print("Problem {}: {}".format(idx+1,i))
