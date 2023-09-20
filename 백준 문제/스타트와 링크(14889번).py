import sys
input = sys.stdin.readline

n = int(input())

INF = int(1e9)
mini = INF

peoples = []
visited = [False] * n

for _ in range(n):
    peoples.append(list(map(int, input().split())))

def dfs(L, idx):
    global mini
    if L == n // 2:
        a = 0
        b = 0
        for i in range(n):
            for j in range(n):
                if visited[i] and visited[j]:
                    a += peoples[i][j]
                elif not visited[i] and not visited[j]:
                    b += peoples[i][j]
        mini = min(mini,abs(a-b))
        return
    for i in range(idx, n):
        if not visited[i]:
            visited[i] = True
            dfs(L+1, i+1)
            visited[i] = False
dfs(0,0)
print(mini)