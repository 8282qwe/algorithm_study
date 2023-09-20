import heapq
import sys
input = sys.stdin.readline

INF = int(1e9)

n = int(input())
m = int(input())

citys = [INF] * (n+1)
lines = [[] for _ in range(n+1)]

def dij(start):
    q = []
    heapq.heappush(q,(0,start))
    citys[start] = 0

    while q:
        distance, city = heapq.heappop(q)

        if citys[city] < distance:
            continue

        for i in lines[city]:
            cost = distance + i[1]
            if cost < citys[i[0]]:
                citys[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))

for _ in range(m):
    s, e, c = map(int, input().split())
    lines[s].append((e,c))

start, end = map(int, input().split())

dij(start)

print(citys[end])