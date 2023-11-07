import sys

T = int(sys.stdin.readline().rstrip("\n"))

for _ in range(T):
    N = int(sys.stdin.readline().rstrip("\n"))
    cycle = list(map(int, sys.stdin.readline().rstrip("\n").split()))

    answer = 0
    max_value = 0

    for i in range(len(cycle)-1, -1, -1):
        if cycle[i] > max_value:
            max_value = cycle[i]
        else:
            answer += max_value - cycle[i]

    print(answer)