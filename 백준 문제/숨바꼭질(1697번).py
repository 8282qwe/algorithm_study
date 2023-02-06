from collections import deque

n, k = map(int, input().split())

def bfs(x):
    queue = deque()
    queue.append(x)
    result = [0] * 100001

    while queue:
        mx = queue.popleft()

        if mx == k:
            return result[mx]

        for next_x in (mx-1,mx+1,mx*2):
            if 0 <= next_x < 100001 and not result[next_x]:
                result[next_x] = result[mx] + 1
                queue.append(next_x)


print(bfs(n))