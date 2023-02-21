from collections import deque

n = int(input())

data = list(map(int, input().split()))

add, sub, mul, div = map(int, input().split())

maximum = -1e9
minimum = 1e9

#BFS로 풀기엔 메모리 초과가 발생할것 같으므로 DFS로 풀이
def dfs(now,i):
    global add, sub, mul, div, maximum, minimum

    if i == n:
        maximum = max(maximum, now)
        minimum = min(minimum, now)

    else:
        if add > 0:
            add -= 1
            dfs(now+data[i],i+1)
            add += 1
        if sub > 0:
            sub -= 1
            dfs(now-data[i],i+1)
            sub += 1
        if mul > 0:
            mul -= 1
            dfs(now*data[i],i+1)
            mul += 1
        if div > 0:
            div -= 1
            dfs(int(now/data[i]),i+1)
            div += 1

dfs(data[0],1)

print(maximum)
print(minimum)