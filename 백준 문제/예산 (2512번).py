N = int(input())
buget = list(map(int, input().split()))
maxium = int(input())
a = 0
b = max(buget)
m = (a+b)//2
while a <= b:
    all = 0
    for i in buget:
        if i <= m:
            all += i
        else:
            all += m

    if all <= maxium:
        a = m + 1
    else:
        b = m - 1
    m = (a+b) // 2
print(m)