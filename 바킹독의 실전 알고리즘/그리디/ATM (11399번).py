import sys
input = sys.stdin.readline

n = int(input())

m = list(map(int,input().rstrip().split()))

m.sort()
for i in range(1,n):
    m[i] += m[i-1]
print(sum(m))