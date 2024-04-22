import sys
import heapq

input = sys.stdin.readline

n,m,x = map(int, input().rstrip().split())
matrix = [[] for _ in range(n+1)]
res = [0 for _ in range(n+1)]

for _ in range(m):
    a,b,c = map(int,input().rstrip().split())
    matrix[a].append((b,c))

def dij(a,b):
    q = []
    distance = {i:int(1e9) for i in range(1,n+1)}
    distance[a] = 0
    heapq.heappush(q,(0,a))

    while q:
        now_dist,now_node = heapq.heappop(q)

        if distance[now_node] <now_dist: continue

        for i,j in matrix[now_node]:
            new_dist = now_dist+j
            if distance[i] > new_dist:
                distance[i] = new_dist
                heapq.heappush(q,((new_dist,i)))
    return distance[b]

res1 = [dij(i,x)+dij(x,i) for i in range(1,n+1)]
print(max(res1))