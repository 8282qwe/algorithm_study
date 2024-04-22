import sys
input = sys.stdin.readline

n = int(input())

num_list = list(map(int,input().rstrip().split()))
area = num_list[0]*4+2

for i in range(1,n):
    if num_list[i-1] >= num_list[i]:
        area -= num_list[i]
    else:
        area -= num_list[i-1]
        area += num_list[i]-num_list[i-1]

    area += num_list[i] * 3 + 2
print(area)