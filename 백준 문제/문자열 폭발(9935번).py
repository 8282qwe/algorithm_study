import sys
input = sys.stdin.readline

target = input().rstrip()

exp = input().rstrip()
exp_len = len(exp)

stack = []

for i in range(len(target)):
    stack.append(target[i])
    if "".join(stack[-exp_len:]) == exp:
        for _ in range(exp_len):
            stack.pop()

if len(stack) == 0:
    print("FRULA")
else:
    print("".join(stack))