T = int(input())

rank = []
for _ in range(T):
    n,k,t,m = map(int, input().split())

    matrix = [[0] * k for _ in range(n)]
    solved = [0 for _ in range(n)]
    log = [0 for _ in range(n)]

    for i in range(m):
        a,b,c = map(int, input().split())
        solved[a-1] += 1
        log[a-1] = i
        matrix[a-1][b-1] = max(matrix[a-1][b-1],c)

    board = [[sum(matrix[x]),solved[x],log[x],x] for x in range(n)]

    board.sort(key = lambda x : (-x[0],x[1],x[2]))

    ranking = 1
    for team in board:
        if team[3]+1 == t:
            rank.append(ranking)
        else:
            ranking+=1

for x in rank:
    print(x)