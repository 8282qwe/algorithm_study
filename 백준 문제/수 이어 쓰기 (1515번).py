N = input()

start = 1
idx = 0

while idx < len(N):
    temp = str(start)

    for i in range(len(temp)):
        if idx >= len(N):
            break
        if temp[i] == N[idx]:
            idx += 1
    start += 1

print(start-1)