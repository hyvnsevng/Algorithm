import sys

sys.stdin = open('input.txt')

# Testcase 수
T = 10
# Testcase 만큼 반복
for testcase in range(1, T+1):
    tc = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]

    goal = ladder[99].index(2)

    row, col = 99, goal

    while row >= 0:
        ladder[row][col] = 2
        if col < 99 and ladder[row][col+1] == 1:
            col += 1
        elif col > 0 and ladder[row][col-1] == 1:
            col -= 1
        else:
            row -= 1

        # print(row, col)

    print(f'#{tc} {col}')

