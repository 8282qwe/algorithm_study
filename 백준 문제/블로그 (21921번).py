N, X = map(int, input().split())

hitmap = list(map(int, input().split()))
hit_max = [sum(hitmap[i:i+X]) for i in range(N-X+1)]

if max(hit_max) == 0:
    print("SAD")
    exit(0)
else:
    print(max(hit_max))
    print(hit_max.count(max(hit_max)))