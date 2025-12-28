import sys
input = sys.stdin.readline

N, B = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]


def divNcon(e):
    if e == 1:
        return A
    if e == 2:
        return square(A)
    half = e // 2
    if e % 2:
        return multiple(square(divNcon(half)))
    else:
        return square(divNcon(half))


def square(matrix):
    arr = [[0] * N for _ in range(N)] 
    for i in range(N):
        for j in range(N):
            for k in range(N):
                arr[i][j] += (matrix[i][k] * matrix[k][j]) % 1000
    return arr


def multiple(matrix):
    arr = [[0] * N for _ in range(N)] 
    for i in range(N):
        for j in range(N):
            for k in range(N):
                arr[i][j] += (matrix[i][k] * A[k][j]) % 1000
    return arr


result = divNcon(B)
for row in result:
    for e in row:
        print(e % 1000, end=' ')
    print()