import sys
input = sys.stdin.readline

n,s = map(int,input().rstrip().split())
numList = list(map(int, input().rstrip().split()))

end = 0
ans = int(1e9)
sumList = 0
for start in range(n):
    while sumList < s and end < n:
        sumList += numList[end]
        end += 1
    if sumList >= s:
        ans = min(ans,end-start)
    sumList -= numList[start]

if ans == int(1e9):
    print("0")
else:
    print(ans)