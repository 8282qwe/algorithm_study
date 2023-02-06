from collections import deque

f,s,g,u,d = map(int, input().split())

MAX = 1000001
result = [0] * MAX

def bfs(start):
    q = deque()
    q.append(start)
    result[start] = 1

    while q:
        x = q.popleft()

        if x == g:
            return result[g] - 1

        for next_x in (x+u,x-d):
            if 1 <= next_x <= f and not result[next_x]:
                result[next_x] = result[x] + 1
                q.append(next_x)
    return "use the stairs"
print(bfs(s))