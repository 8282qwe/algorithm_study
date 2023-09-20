n = int(input())

m = int(input())

INF = int(1e9)
buses = [[INF]*n for _ in range(n)]

for i in range(n):
    buses[i][i] = 0

for _ in range(m):
    a,b,c = map(int,input().split())
    if c < buses[a-1][b-1]:
        buses[a-1][b-1] = c

for k in range(n):
    for a in range(n):
        for b in range(n):
            buses[a][b] = min(buses[a][b], buses[a][k] + buses[k][b])

for i in buses:
    for j in i:
        if j == INF:
            print("0", end=" ")
        else:
            print(j, end=" ")
    print()

