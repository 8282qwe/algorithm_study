import heapq

queue = []

n = int(input())

for _ in range(n):
    for i in list(map(int, input().split())):
        if len(queue) < n:
            heapq.heappush(queue,i)
        else:
            if queue[0] < i:
                heapq.heappop(queue)
                heapq.heappush(queue,i)

print(queue[0])
