import sys

input = sys.stdin.readline

n, b = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(n)]


def mult_matrix(arr1, arr2):
    result = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            s = sum(arr1[i][k] * arr2[k][j] for k in range(n))
            result[i][j] = s % 1000
    return result


def p(n, arr):
    if n == 1:
        return matrix
    if n % 2 == 0:
        half = p(n // 2, arr)
        return mult_matrix(half, half)
    else:
        return mult_matrix(arr, p(n - 1, arr))


for i in p(b, matrix):
    print(*[j%1000 for j in i])