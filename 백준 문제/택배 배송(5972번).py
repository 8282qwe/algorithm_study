import sys
import heapq

n,m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n)]

for _ in range(m):
    s,e,c = map(int, sys.stdin.readline().rstrip().split())
    graph[s-1].append((e-1,c))
    graph[e-1].append((s-1,c))

def dij(graph,start):
    distance = {node: float('inf') for node in range(n)}
    distance[start] = 0
    queue = []
    heapq.heappush(queue,(distance[start],start))

    while queue:
        dist, now = heapq.heappop(queue)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(queue,(cost,i[0]))
    print(distance[n-1])
dij(graph,0)

