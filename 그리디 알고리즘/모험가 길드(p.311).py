n = int(input())

people = list(map(int,input().split()))

people.sort()
teams = 0
center = people.pop()
while center-1 <= len(people):
    for _ in range(center-1):
        people.pop()
    teams += 1
    if people:
        center = people.pop()
print(teams)