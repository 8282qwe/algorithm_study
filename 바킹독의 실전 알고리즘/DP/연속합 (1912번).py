import sys
input = sys.stdin.readline

n = int(input())
num_list = list(map(int, input().rstrip().split()))

dp = [num_list[0]]

for i in num_list[1:]:
    dp.append(max(dp[-1]+i,i))
print(max(dp))