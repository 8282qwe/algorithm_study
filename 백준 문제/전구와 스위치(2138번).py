import sys

n = int(sys.stdin.readline().rstrip())
lights = list(map(bool, map(int,sys.stdin.readline().rstrip())))
ansLights = list(map(bool, map(int,sys.stdin.readline().rstrip())))

def pressButton(target,answer):
    targetCopy = target[:]
    pressCount = 0
    for i in range(1,n):
        if targetCopy[i-1] == answer[i-1]:
            continue
        else:
            pressCount+=1
            for j in range(i-1,i+2):
                if j < n:
                    targetCopy[j] = not targetCopy[j]
    if targetCopy == answer:
        return pressCount
    else:
        return int(1e9)

buf = pressButton(lights,ansLights)

lights[0] = not lights[0]
lights[1] = not lights[1]
buf = min(buf,pressButton(lights,ansLights)+1)

if buf == int(1e9):
    print(-1)
else:
    print(buf)