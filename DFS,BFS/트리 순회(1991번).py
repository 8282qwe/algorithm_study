import sys
input = sys.stdin.readline

diction = {}
n = int(input())

for _ in range(n):
    i,j,k = map(str,input().rstrip().split())

    if i not in diction:
        diction[i] = [j,k]

def pre(i):
    print(i,end="")

    for j in diction[i]:
        if j != ".":
            pre(j)

pre("A")
print()
def mid(i):
    if diction[i][0] != '.':
        mid(diction[i][0])
    print(i,end='')
    if diction[i][1] != '.':
        mid(diction[i][1])

mid("A")
print()

def suf(i):
    if diction[i][0] != '.':
        suf(diction[i][0])
    if diction[i][1] != '.':
        suf(diction[i][1])
    print(i,end="")

suf("A")
print()