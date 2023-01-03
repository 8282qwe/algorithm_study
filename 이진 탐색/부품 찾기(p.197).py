def binary_search(array, target, start, end):
    if start > end:
        return None

    mid = (start + end) // 2

    if target == array[mid]:
        return target
    elif target > array[mid]:
        return binary_search(array, target, mid + 1, end)
    else:
        return binary_search(array, target, start, mid - 1)


n = int(input())
have = list(map(int, input().split()))
have.sort()

m = int(input())
want = list(map(int, input().split()))

for i in want:
    result = binary_search(have, i, 0, n-1)
    if result is not None:
        print("yes", end =' ')
    else:
        print("no", end=' ')