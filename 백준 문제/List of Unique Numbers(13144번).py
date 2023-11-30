import sys
input = sys.stdin.readline

n = int(input())
numList = list(map(int,input().rstrip().split()))
segment = {i:False for i in range(1,100001)}
cnt = 0
start,end = 0,0
while start <= end and end < n:
    if not segment[numList[end]]:
        segment[numList[end]] = True
        end += 1
        cnt += end - start
    else:
        while segment[numList[end]]:
            segment[numList[start]] = False
            start += 1
print(cnt)