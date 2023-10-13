n,new,p = map(int, input().split())

ranking = []

if n != 0:
    ranking = list(map(int,input().split()))

if len(ranking) == p and ranking[-1] >= new:
    print(-1)
    exit()

ranking.append(new)
ranking.sort(reverse=True)
print(ranking.index(new)+1)