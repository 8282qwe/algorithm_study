import sys
from itertools import product

input = sys.stdin.readline

n = int(input())
num_list = [int(input()) for _ in range(n)]
numsum_list = [a+b for a,b in product(num_list,repeat=2)]
numsum_list = list(dict.fromkeys(numsum_list))
numsum_list.sort()

def binary_search(a):
    st,en = 0,len(numsum_list)-1
    while st < en:
        mid = (st+en)//2
        if numsum_list[mid] == a:
            return True
        elif numsum_list[mid] < a: st = mid + 1
        else: en = mid - 1
    return False

for i in range(n-1,-1,-1):
    for j in range(i+1):
        if binary_search(num_list[i]-num_list[j]):
            print(num_list[i])
            exit()