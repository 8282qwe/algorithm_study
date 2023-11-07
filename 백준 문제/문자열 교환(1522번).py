import sys

text = sys.stdin.readline().rstrip()

a = text.count("a")

text += text[:a-1]

minVal = float("inf")

for i in range(len(text) - (a-1)):
    minVal = min(minVal,text[i:i+a].count('b'))

print(minVal)