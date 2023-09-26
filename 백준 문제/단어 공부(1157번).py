from sys import stdin

a = stdin.readline().strip()
a = a.upper()

dict = {}

for i in a:
    if i in dict:
        dict[i] += 1
    else:
        dict[i] = 1
if len([k for k,v in dict.items() if max(dict.values())==v]) > 1:
    print("?")
else:
    print(max(dict,key=dict.get))

