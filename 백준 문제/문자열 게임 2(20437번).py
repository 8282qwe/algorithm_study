from collections import Counter
from itertools import permutations
import sys

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    t = []
    memo = [[] for _ in range(27)]

    text = list(sys.stdin.readline().rstrip())
    k = int(sys.stdin.readline().rstrip())

    for idx, num in enumerate(text):
        buf = ord(num) - ord('a')
        memo[buf].append(idx)

        if len(memo[buf]) >= k:
            t.append(text[memo[buf][-k]:memo[buf][-1]+1])
    if len(t) == 0:
        print(-1)
    else:
        t.sort(key=lambda x: len(x))
        print(len(t[0]),len(t[-1]))