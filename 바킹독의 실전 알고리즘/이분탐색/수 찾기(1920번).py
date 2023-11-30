import sys
input = sys.stdin.readline

n = int(input())
n_list = list(map(int, input().rstrip().split()))

m = int(input())
m_list = list(map(int, input().rstrip().split()))

n_list.sort()

for i in m_list:
    start,end = 0,n-1
    flag = False
    while start <= end:
        mid = (start + end) // 2
        if n_list[mid] == i:
            flag = True
            break
        elif n_list[mid] < i:
            start = mid + 1
        else:
            end = mid - 1
    if flag:
        print(1)
    else:
        print(0)