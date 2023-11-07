import sys

p,m = map(int, sys.stdin.readline().rstrip().split(' '))
lock = []
users = []

for _ in range(p):
    flag = True
    user = sys.stdin.readline().rstrip().split(' ')
    #level = user[0], id = user[1]

    for i,j in enumerate(lock):
        if j-10 <= int(user[0]) <= j+10 and len(users[i]) < m:
            users[i].append(user)
            flag = False
            break

    if flag:
        lock.append(int(user[0]))
        users.append([user])

for i in users:
    if len(i) == m:
        print("Started!")
    else:
        print("Waiting!")

    i.sort(key=lambda x: x[1])
    for level,id in i:
        print(level,id)
