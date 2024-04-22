import sys
input = sys.stdin.readline

numList = list(map(int, input().rstrip()))
sum = numList.pop(0)

for i in numList:
    if i <= 1 or sum <= 1:
        sum+=i
    else:
        sum*=i
print(sum)

