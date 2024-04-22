import sys
input = sys.stdin.readline

n = int(input())

score_list = [int(input())for i in range(n)]
cnt = 0
for i in range(n-2,-1,-1):
    if score_list[i+1] <= score_list[i]:
        cnt += score_list[i]-score_list[i+1]+1
        score_list[i] = score_list[i+1] - 1
print(cnt)