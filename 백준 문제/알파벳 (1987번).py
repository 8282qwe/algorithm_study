import sys
input = sys.stdin.readline

n,m = map(int,input().rstrip().split())

board = [list(input().rstrip()) for _ in range(n)]

def dfs(a,b):
    global ans
    alphas.add(board[a][b])
    ans = max(ans, len(alphas))

    for nodeA,nodeB in [[a,b-1],[a,b+1],[a-1,b],[a+1,b]]:
        if 0 <= nodeA < n and 0 <= nodeB < m:
            if board[nodeA][nodeB] not in alphas:
                dfs(nodeA,nodeB)
                alphas.remove(board[nodeA][nodeB])

ans = 0
alphas = set()
dfs(0,0)
print(ans)