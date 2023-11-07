import sys

n,m = map(int, sys.stdin.readline().rstrip().split())

buildings = list(map(int, sys.stdin.readline().strip().split()))
res = 0

for i in range(1,m-1):
    leftMax = max(buildings[:i])
    rightMax = max(buildings[i+1:])

    center = min(leftMax,rightMax) - buildings[i]
    if center < 0:
        center = 0
    res += center
print(res)