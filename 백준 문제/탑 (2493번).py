import sys

n = int(sys.stdin.readline().rstrip())

s1 = [(idx+1,num) for idx,num in enumerate(list(map(int, sys.stdin.readline().rstrip().split())))]
s2 = []
signal = [0 for _ in range(n)]

buf = s1.pop(-1)
while s1:

    if s1[-1][1] > buf[1]:
        signal[buf[0]-1] = s1[-1][0]
        if s2:
            buf = s2.pop(-1)
        else:
            buf = s1.pop(-1)
    elif s1[-1][1] < buf[1]:
        s2.append(buf)
        buf = s1.pop(-1)

print(*signal)