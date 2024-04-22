import sys
input = sys.stdin.readline

n = int(input())
matrix = [[1,1],[1,0]]

def mult_matrix(arr1,arr2):
    result = [[0,0],[0,0]]
    for i in range(2):
        for j in range(2):
            s = sum([arr1[i][k]*arr2[k][j] for k in range(2)])
            result[i][j] = s % 1000000

    return result

def p(n,arr):
    if n == 1:
        return arr
    if n%2 == 0:
        half = p(n//2,arr)
        return mult_matrix(half,half)
    else:
        return mult_matrix(arr,p(n-1,arr))

print(p(n,matrix)[0][1]%1000000)