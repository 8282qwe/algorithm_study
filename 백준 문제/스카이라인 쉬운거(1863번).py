import sys

n = int(sys.stdin.readline().rstrip())
skylines = [int(sys.stdin.readline().rstrip().split()[1]) for _ in range(n)] + [0]

stack = [0]
answer = 0
for i in skylines:
    height = i
    while stack[-1] > i:
        if stack[-1] != height:
            answer += 1
            height = stack[-1]
        stack.pop()
    stack.append(i)
print(answer)
