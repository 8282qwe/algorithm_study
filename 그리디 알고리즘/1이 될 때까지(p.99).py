n, m = map(int, input().split())
result = 0

while True:
    target = (n//m) * m
    result += (n-target)
    n //= m
    result += 1

    if n < m:
        break

result += (n-1)

print(result)