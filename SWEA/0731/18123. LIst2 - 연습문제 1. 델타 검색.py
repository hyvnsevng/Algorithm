import sys

sys.stdin = open('ex1_input.txt')

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):
    N = int(input())

    matrix = [list(map(int, input().split())) for x in range(N)]

    dr = [1, 0, -1, 0]
    dc = [0, 1, 0, -1]

    total = 0

    for i in range(5):
        for j in range(5):
            for k in range(4):
                ni = i+dr[k]
                nj = j+dc[k]
                if 0 <= ni <= 4 and 0 <= nj <=4:
                    total += abs(matrix[i][j] - matrix[ni][nj])

    print(f'#{tc} {total}')