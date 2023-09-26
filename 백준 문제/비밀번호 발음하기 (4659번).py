import re

while True:
    test = input()
    if test == 'end': break

    p = re.findall('a|e|i|o|u', test)  # p만족하는게 있어야함
    q = re.findall('([a|e|i|o|u]{3})|([^a|e|i|o|u]{3})', test)  # q만족하는게 없어야함
    r = re.findall(r'([a-df-np-z])\1', test)  # r 만족하는 게 없어야함

    if len(p) != 0 and len(q) == 0 and len(r) == 0:
        print(f"<{test}> is acceptable.")
    else:
        print(f"<{test}> is not acceptable.")