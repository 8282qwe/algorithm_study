import sys

input = sys.stdin.readline
answer = 0
answerList = []
n = list(input().rstrip())

for i in n:
    if ord("A") <= ord(i) <= ord("Z"):
        answerList.append(i)
    else:
        answer += ord(i)-48
print(''.join(sorted(answerList))+str(answer))