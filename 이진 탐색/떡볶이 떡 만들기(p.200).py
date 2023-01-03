def binary_search(array, target, start, end):
    if start > end:
        return None
    sliced = 0
    mid = (start + end) // 2
    for i in array:
        if (i-mid) < 0: continue
        sliced += (i-mid)

    if sliced == target:
        return mid
    elif sliced > target:
        return binary_search(array, target, mid + 1, end)
    else:
        return binary_search(array, target, start, mid - 1)


n,m = map(int, input().split())

array = list(map(int, input().split()))
array.sort()

result = binary_search(array, m, 0, array[-1])
print(result)
