import sys
input = sys.stdin.readline

n = input().rstrip().split("-")

for i in range(len(n)):
    buf = n[i].split("+")
    if len(buf) == 1:
        n[i] = str(int(buf[0]))
        continue
    for j in range(len(buf)):
        buf[j] = str(int(buf[j]))
    n[i] = str(eval("+".join(buf)))

print(eval("-".join(n)))