import sys

sys.stdin = open('input.txt')

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):
    N, K = map(int, input().split())

    puzzle = [list(map(int, input().split())) for _ in range(N)]


    ans = 0
    for i in range(N):
        row_streak = 0
        col_streak = 0
        for j in range(N):
            if puzzle[i][j] == 1:
                row_streak += 1
            else:
                if row_streak == K:
                    ans += 1
                row_streak = 0

            if puzzle[j][i] == 1:
                col_streak += 1
            else:
                if col_streak == K:
                    ans += 1
                col_streak = 0
        else:
            if row_streak == K:
                ans += 1
            if col_streak == K:
                ans += 1

    print(ans)

