import sys
from collections import Counter

#n = 총 가능 층수(1~n), k = 층 자릿수, p = 반전 갯수 최대수(1~p), x = 실제 층수
n,k,p,x = map(int, sys.stdin.readline().rstrip().split())

binary = {'0': [1,1,1,1,1,1,0],
          '1': [0,1,1,0,0,0,0],
          '2': [1,1,0,1,1,0,1],
          '3': [1,1,1,1,0,0,1],
          '4': [0,1,1,0,0,1,1],
          '5': [1,0,1,1,0,1,1],
          '6': [1,0,1,1,1,1,1],
          '7': [1,1,1,0,0,0,0],
          '8': [1,1,1,1,1,1,1],
          '9': [1,1,1,1,0,1,1] }
x = str(x).zfill(k)
xTransform = [binary[i] for i in x]

possibleNum = 0
for i in range(1,n+1):
    elevator = str(i).zfill(k)
    eleTransform = [binary[i] for i in elevator]

    diffCnt = 0
    for x,e in zip(xTransform,eleTransform):
        diffCnt += Counter([a ^ b for a,b in zip(x,e)])[1]
        if diffCnt > p:
            break
    if 0 < diffCnt <= p:
        possibleNum += 1
print(possibleNum)
