N, K = map(int, input().split())

buger = list(input())

cnt = 0
for idx, val in enumerate(buger):
    if val == "P":
        for i in range(idx-K, idx+K+1):
            if 0 <= i < N and buger[i] == "H":
                cnt += 1
                buger[i] = "0"
                break
print(cnt)