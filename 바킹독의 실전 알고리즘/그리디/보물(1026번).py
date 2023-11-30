import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int,input().rstrip().split()))
b = list(map(int,input().rstrip().split()))

a.sort()
b.sort(reverse=True)
print(sum([i*j for i,j in zip(a,b)]))