from collections import deque
N = int(input())

cards = [x for x in range(1,N+1)]
queue = deque(cards)

while len(queue) > 1:
    queue.popleft()
    queue.append(queue.popleft())

print(queue[0])