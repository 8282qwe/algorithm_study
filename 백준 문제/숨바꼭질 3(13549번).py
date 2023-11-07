import sys
import heapq

n,k = map(int, sys.stdin.readline().rstrip().split())
distance = [int(1e9)] * 100001

def dij(start,end):
    q = []

    if end <= start:
        print(start-end)
        return

    heapq.heappush(q,(0,start))

    while q:
        dist,node = heapq.heappop(q)

        for nx in [node+1,node-1,node*2]:
            if 0 <= nx <= 100000:
                if nx == node * 2 and distance[nx] == int(1e9):
                    distance[nx] = dist
                    heapq.heappush(q,(dist,nx))
                elif distance[nx] == int(1e9):
                    distance[nx] = dist + 1
                    heapq.heappush(q,(dist+1,nx))
    print(distance[end])
dij(n,k)