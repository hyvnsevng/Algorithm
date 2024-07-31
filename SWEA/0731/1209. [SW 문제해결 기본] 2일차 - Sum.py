import sys

sys.stdin = open('input.txt')

# Testcase 수
T = 10
# Testcase 만큼 반복
for _ in range(10):
    tc = int(input())
    max_sum = 0
    matrix = []
    for _ in range(100):
        temp = 0
        arr = list(map(int, input().split()))
        matrix.append(arr)

    diag_sum1 = 0
    diag_sum2 = 0
    for i in range(100):
        col_sum = 0
        row_sum = 0
        diag_sum1 += matrix[i][i]
        diag_sum2 += matrix[i][99-i]

        for j in range(100):

            row_sum += matrix[i][j]
            col_sum += matrix[j][i]

        if row_sum > max_sum:
            max_sum = row_sum
        if col_sum > max_sum:
            max_sum = col_sum

    if diag_sum1 > max_sum:
        max_sum = diag_sum1
    if diag_sum2 > max_sum:
        max_sum = diag_sum2


    print(f'#{tc} {max_sum}')


