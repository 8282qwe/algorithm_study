import sys

t1 = list(sys.stdin.readline().rstrip())
t2 = list(sys.stdin.readline().rstrip())

def search(text):
    if text == t1:
        print(1)
        sys.exit()
    if len(text) == 0:
        return
    if text[-1] == 'A':
        search(text[:-1])
    if text[0] == 'B':
        search(text[1:][::-1])



search(t2)
print(0)