import sys
from math import ceil

H,W,N,M = map(int, sys.stdin.readline().split())
a = ceil(W/(M+1))
b = ceil(H/(N+1))
print(a*b)

