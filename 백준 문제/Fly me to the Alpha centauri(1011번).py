n = int(input())

distance = []
for _ in range(n):
    x, y = map(int, input().split())
    distance.append(y-x)

for i in distance:
    n = 0
    while i >= n*(n+1):
        n+=1
    if i <= n**2:
        print(2*n-1)
    else:
        print(2*n)