N = int(input())

x = input()
count = 0
for _ in range(N-1):
    buf = input()
    stand = x
    if len(buf) < len(stand):
        stand, buf = buf, stand

    for y in stand:
        buf = buf.replace(y,"",1)

    if len(buf) <= 1:
        count += 1

print(count)

