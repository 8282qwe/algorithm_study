import sys
input = sys.stdin.readline

scores = list(map(int, input().rstrip()))

print("LUCKY" if sum(scores[0:len(scores)//2]) == sum(scores[len(scores)//2:]) else "READY")