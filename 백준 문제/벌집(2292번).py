from sys import stdin

N = int(stdin.readline())
N -= 1
a = 1

while N > 0:
    N -= a*6
    a += 1
print(a)