import sys
input = sys.stdin.readline

n,m = map(int, input().split())
parents = [i for i in range(n+1)]
print(parents)

def find_parent(parent,x):
    if parent[x] != x:
        return find_parent(parent,parent[x])
    return parent[x]

def marge(parent, x, y):
    a = find_parent(parent,x)
    b = find_parent(parent,y)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

for _ in range(m):
    command,a,b = map(int,input().split())
    if command == 0:
        marge(parents,a,b)
    elif command == 1:
        if find_parent(parents,a) == find_parent(parents,b):
            print("Yes")
        else:
            print("No")
