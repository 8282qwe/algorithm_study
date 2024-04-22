import sys
sys.setrecursionlimit(10 ** 6)

cnt = 0
def dfs(string, word):
    global cnt
    words = ['A', 'E', 'I', 'O', 'U']
    cnt += 1
    print("".join(string))

    if "".join(string) == word:
        return True

    if len(string) >= 5:
        return False

    for w in words:
        string.append(w)
        flag = dfs(string, word)
        if flag:
            break
        string.pop()

dfs([],"I")
print(cnt)