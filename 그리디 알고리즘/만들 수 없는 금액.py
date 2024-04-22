import sys
input = sys.stdin.readline

n = int(input())
coins = list(map(int,input().rstrip()))
coins.sort()

target = 1
for i in coins:
    if i > target:
        break
    target+=i

print(target)