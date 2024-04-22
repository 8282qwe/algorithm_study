import sys
input = sys.stdin.readline

n,m = map(int, input().split())
balls = [0]*11
answer = 0

for i in list(map(int,input().rstrip())):
    balls[i]+=1

for i in range(1,11):
    n-=balls[i]
    answer += n*balls[i]

print(answer)