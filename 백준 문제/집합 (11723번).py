from sys import stdin

M = int(stdin.readline())
S = set()

for _ in range(M):
    comm = stdin.readline().strip()
    if comm == "all":
        S = set(list(range(1,21)))
    elif comm == "empty":
        S = set()

    else:
        com,x = comm.split()
        x = int(x)

        if com == "add":
            S.add(x)
        elif com == "remove":
            if x in S:
                S.remove(x)
        elif com == "check":
            if x in S:
                print(1)
            else:
                print(0)
        elif com == "toggle":
            if x in S:
                S.remove(x)
            else:
                S.add(x)

