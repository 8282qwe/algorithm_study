v,e = map(int, input().split())

INF = int(1e9)
roads = [[INF] * v for _ in range(v)]


for _ in range(e):
    a,b,c = map(int, input().split())
    roads[a-1][b-1] = c

for k in range(v):
    for i in range(v):
        for j in range(v):
            roads[i][j] = min(roads[i][j], roads[i][k]+roads[k][j])

answer = INF
for i in range(v):
    answer = min(answer, roads[i][i])

if answer == INF:
    print(-1)
else:
    print(answer)