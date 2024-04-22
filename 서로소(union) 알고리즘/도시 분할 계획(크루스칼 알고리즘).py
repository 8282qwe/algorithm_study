import sys
input = sys.stdin.readline

n,m = map(int, input().split())
matrix = [[] for _ in range(n+1)]
node = [i for i in range(n+1)]
edages = []
edagesCount = 0
result = 0

for _ in range(m):
    a,b,cost = map(int,input().split())
    matrix[a].append(b)
    edages.append((cost,a,b))

edages.sort()

def find_parent(parent,x):
    if parent[x] != x:
        return find_parent(parent,parent[x])
    return parent[x]

def marge(parent,x,y):
    a = find_parent(parent,x)
    b = find_parent(parent,y)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


for cost,a,b in edages:
    if find_parent(node,a) == find_parent(node,b):
        continue
    if edagesCount == n-2:
        print(result)
        break
    marge(node,a,b)
    edagesCount+=1
    result += cost

