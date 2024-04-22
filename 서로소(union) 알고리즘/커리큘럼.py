import copy
from collections import deque
import sys
input = sys.stdin.readline

n = int(input())

times = [0 for _ in range(n+1)]
graph = [[] for _ in range(n+1)]
indegree = [0 for _ in range(n+1)]
for i in range(1,n+1):
    data = list(map(int, input().split()))

    times[i] = data[0]

    for j in data[1:-1]:
        indegree[i] += 1
        graph[j].append(i)

def topology_sort():
    result = copy.deepcopy(times)
    q = deque()

    for i in range(1,n+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        node = q.popleft()

        for i in graph[node]:
            result[i] = max(result[i],result[node]+times[i])
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)
    return result

print(*topology_sort()[1:])
