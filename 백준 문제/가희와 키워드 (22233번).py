import sys

n, m = map(int, sys.stdin.readline().split(' '))

memo = {}
cnt = 0

for _ in range(n):
    memo[sys.stdin.readline().rstrip()] = 1
    cnt += 1

for _ in range(m):
    keyword = list(sys.stdin.readline().rstrip().split(','))
    for i in keyword:
        if i in memo.keys():
            if memo[i] == 1:
                memo[i] = 0
                cnt -= 1
    print(cnt)