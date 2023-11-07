import sys

n = int(sys.stdin.readline().rstrip())
roof = [0 for _ in range(1001)]
maximum = [0,0]

for _ in range(n):
    l, h = map(int, sys.stdin.readline().rstrip().split())

    if maximum[1] < h:
        maximum[0],maximum[1] = l,h
    roof[l] = h

curr = 0
size = 0
for i in range(maximum[0]+1):
    curr = max(roof[i],curr)
    size += curr

curr = 0
for i in range(1000,maximum[0],-1):
    curr = max(roof[i],curr)
    size += curr

print(size)



