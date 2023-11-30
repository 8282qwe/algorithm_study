import sys
from collections import deque
input = sys.stdin.readline

t = int(input())

def dfs(n):
    answer = []
    q = deque()
    q.append((1,'1'))

    while q:
        now,buf = q.popleft()

        if now >= n:
            if eval(buf.replace(" ",'')) == 0:
                answer.append(buf)
            continue

        for i in [' ','+','-']:
            q.append((now+1,buf+i+str(now+1)))
    return answer

for _ in range(t):
    n = int(input())
    for i in dfs(n):
        print(i)

