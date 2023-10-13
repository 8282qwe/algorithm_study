n,m = input().split()

peoples = []
for _ in range(int(n)):
    peoples.append(input())

peoples = set(peoples)

match m:
    case "Y":
        print(len(peoples))
    case "F":
        print(int(len(peoples)/2))
    case "O":
        print(int(len(peoples)/3))

