import sys
input = sys.stdin.readline

def find_parent(parent,x):
    if parent[x] != x:
        return find_parent(parent,parent[x])
    return x
#경로 압축 버전
def find_parent_new(parent,x):
    if parent[x] != x:
        parent[x] = find_parent_new(parent,parent[x])
    return parent[x]
def union_parent(parent,a,b,):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

v,e = map(int,input().split())
parent = [i for i in range(v+1)]

for i in range(e):
    a,b = map(int, input().split())
    union_parent(parent,a,b)

print("각 원소가 속한 집합 : ",end = ' ')
for i in range(1,v+1):
    print(find_parent(parent,i),end=' ')
print()
print("부모 테이블: ",end=' ')
print(*parent[1:])
