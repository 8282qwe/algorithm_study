i = int(input())

text_list = []

for _ in range(i):
    text = input()
    text_list.append(text)

text_list = list(set(text_list))
text_list.sort()
text_list.sort(key=lambda x: len(x))
for j in text_list:
    print(j)