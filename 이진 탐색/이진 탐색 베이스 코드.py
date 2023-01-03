def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if array[mid] == target:
        return array[mid]
    elif array[mid] > target:
        binary_search(array, target, start, mid - 1)
    else:
        binary_search(array, target, mid + 1, end)

