import sys
input = sys.stdin.readline

def find(x):
    if parents[x] != x:
        parents[x] = find(parents[x])
    return parents[x]

def union(a,b):
    a = find(a)
    b = find(b)
    if a < b:
        parents[b] = a
    else:
        parents[a] = b

t = 0
while True:
    t+=1
    n,m = map(int,input().rstrip().split())
    if n==0 and m == 0:
        break
    parents = [i for i in range(n+1)]
    cycle = set()
    for _ in range(m):
        a,b = map(int,input().rstrip().split())
        if find(a) == find(b):
            cycle.add(a)
            cycle.add(b)

        if parents[a] in cycle or parents[b] in cycle:
            cycle.add(parents[a])
            cycle.add(parents[b])
        union(a,b)

    for i in range(n+1):
        find(i)

    parents = set(parents)
    ans = sum([1 if i not in cycle else 0 for i in parents])-1
    if ans == 0:
        print('Case %d: No trees.' %t)
    elif ans == 1:
        print('Case %d: There is one tree.' %t)
    else:
        print('Case %d: A forest of %d trees.' %(t,ans))
