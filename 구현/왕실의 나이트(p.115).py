
data = input()

now_row = int(data[1]) - 1
now_col = int(ord(data[0])) - 97

mov = [(2,1), (2, -1),(-2,1),(-2,-1),(1,2),(-1,2),(1,-2),(-1,-2)]

result = 0

for i in mov:
    next_col = now_col + i[1]
    next_row = now_row + i[0]

    if next_col >= 0 and next_col < 8 and next_row >= 0 and next_row < 8:
        result += 1

print(result)