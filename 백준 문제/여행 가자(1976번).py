import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

def find(x):
    if parent[x] != x:
        return find(parent[x])
    return parent[x]
def union(a,b):
    a = find(a)
    b = find(b)
    if a<b:
        parent[b] = a
    else:
        parent[a] = b

road = []
parent = [i for i in range(n+1)]

for i in range(n):
    line = list(map(int, input().rstrip().split()))
    for j in range(n):
        if line[j] == 1:
            union(i+1,j+1)
plan = set(list(map(int,input().rstrip().split())))
plan = list(plan)
check = find(plan[0])
for i in plan:
    if find(i) != check:
        print("NO")
        exit(0)
print("YES")