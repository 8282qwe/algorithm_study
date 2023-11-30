import sys
input = sys.stdin.readline

n = int(input())

lof = [int(input()) for _ in range(n)]
lof.sort(reverse=True)

for idx,i in enumerate(lof,1):
    lof[idx-1] = idx*i

print(max(lof))