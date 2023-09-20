n,m = map(int,input().split())

INF = int(1e9)
students = [[0] * n for _ in range(n)]

for _ in range(m):
    a,b = map(int, input().split())
    students[a-1][b-1] = 1

for k in range(n):
    for i in range(n):
        for j in range(n):
            if students[i][k] == 1 and students[k][j] == 1:
                students[i][j] = 1

answer = 0
for i in range(n):
    check = 0
    for j in range(n):
        # i에서 j로 간다는 건 i가 j보다 작음
        # j에서 i로 온다는 건 j가 i보다 작음
        check += students[i][j] + students[j][i]
    # N - 1이라는 것은 자신을 제외한 모든 노드와 비교를 하였다는 것
    if check == n - 1:
        answer +=1
print(answer)