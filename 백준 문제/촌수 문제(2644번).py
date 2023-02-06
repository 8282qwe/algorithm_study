import queue

n = int(input())
p1, p2 = map(int, input().split())
m = int(input())

family = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]
for _ in range(m):
    x,y = map(int, input().split())
    family[x].append(y)
    family[y].append(x)

result = -1
def dfs(v, num):
    global result
    num += 1
    visited[v] = True

    if v == p2:
        result = num

    for i in family[v]:
        if not visited[i]:
            dfs(i, num)

dfs(p1, 0)
if result == -1:
    print(result)
else:
    print(result - 1)