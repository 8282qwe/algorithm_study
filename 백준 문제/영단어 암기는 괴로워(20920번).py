N,M = map(int, input().split())

dic = {}
for _ in range(N):
    word = input()

    if len(word) < M:
        continue

    if word not in dic:
        dic[word] = 1
    else:
        dic[word] += 1

word_lst = sorted(dic.items(), key = lambda x : (-x[1], -len(x[0]), x[0])) # x[0] = 단어, x[1] = 단어 빈도수
# -x[1] = 자주 나오는 단어 앞에 배치
# -len(x[0]) = 단어 길이 길수록 앞에 배치
# x[0] = 단어 사전 순 정렬

for i in word_lst:
    print(i[0])