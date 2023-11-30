import sys
input = sys.stdin.readline

n = int(input())
numList = list(map(int, input().rstrip().split()))
numList.sort()
ans = 0

for i in range(n):
    buf = numList[:i] + numList[i+1:]
    start,end = 0, n-2
    while start < end:
        t = buf[start] + buf[end]
        if t == numList[i]:
            ans += 1
            break
        if t < numList[i]:
            start += 1
        else:
            end -= 1
print(ans)

