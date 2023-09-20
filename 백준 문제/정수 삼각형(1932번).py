data= []

n = int(input())

for _ in range(n):
    data.append(list(map(int, input().split())))


for i in range(1,n):
    for j in range(len(data[i])):
        if j == 0:
            data[i][j] += data[i-1][j]
        elif j == len(data[i])-1:
            data[i][j] += data[i-1][j-1]
        else:
            data[i][j] += max(data[i-1][j-1],data[i-1][j])

print(max(data[-1]))