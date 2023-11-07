n,m = map(int, input().split())

rank = [input().split(" ") for _ in range(n)]
rank.sort(key = lambda x: int(x[1]))

def bs(a):
    start, end = 0, len(rank) - 1
    res = 0

    while start <= end:
        mid = (start + end) // 2
        if a <= int(rank[mid][1]):
            end = mid - 1
            res = mid
        else:
            start = mid + 1

    return res

for _ in range(m):
    ranking = bs(int(input()))
    print(rank[ranking][0])