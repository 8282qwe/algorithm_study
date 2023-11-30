import sys
input = sys.stdin.readline

n = int(input())
n_list = list(map(int, input().rstrip().split()))
n_list.sort()

m = int(input())
m_list = list(map(int, input().rstrip().split()))
def lower_idx(t,n):
    st,en = 0,n
    while st < en:
        mid = (st+en) // 2
        if n_list[mid] >= t: en = mid
        else: st = mid+1
    return st
def upper_idx(t,n):
    st,en = 0,n
    while st < en:
        mid = (st+en) // 2
        if n_list[mid] > t: en = mid
        else: st = mid+1
    return st

for i in m_list:
    print(upper_idx(i,n)-lower_idx(i,n))