from collections import deque

n = list(map(int, input()))
m = int(input())
def solution(numbers, target):
    answer = 0
    result = []
    queue = deque()
    queue.append((0, numbers[0]))

    while queue:
        print(queue)
        num, num_val = queue.popleft()

        print(num)
        if num >= len(numbers):
            print(num)
            continue

        num += 1
        queue.append((num, num_val + numbers[num]))
        queue.append((num,num_val-numbers[num]))
    return answer

solution(n,m)