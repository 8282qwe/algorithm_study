from collections import deque

stores = []
result = []

def bfs(h_x,h_y):
    q = deque()
    q.append((h_x,h_y))

    while q:
        x,y = q.popleft()
        if abs(x-dist_x) + abs(y-dist_y) <= 1000:
            result.append("happy")
            return

        for i in range(n):
            if not visited[i]:
                store_x, store_y = stores[i]
                if abs(x-store_x) + abs(y-store_y) <= 1000:
                    q.append((store_x,store_y))
                    visited[i] = True
    result.append("sad")
    return

t = int(input())
for _ in range(t):
    n = int(input())
    visited = [False for _ in range(n+1)]
    h_x, h_y = map(int,input().split())
    for _ in range(n):
        store = list(map(int,input().split()))
        stores.append(store)
    dist_x, dist_y = map(int, input().split())
    bfs(h_x,h_y)

for i in result:
    print(i)