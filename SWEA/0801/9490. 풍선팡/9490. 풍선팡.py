import sys

sys.stdin = open('input1.txt')

# Testcase 수
T = int(input())

# Testcase 만큼 반복
for tc in range(1, T+1):
    N, M = map(int, input().split())

    balloons = [list(map(int, input().split())) for _ in range(N)]

    # print(balloons)

    drow = [1, 0, -1, 0]
    dcol = [0, 1, 0, -1]

    max_total = 0
    for row in range(N):
        for col in range(M):
            cur = balloons[row][col]
            total = cur
            for d in range(4):
                dr = drow[d]
                dc = dcol[d]
                i = 0
                for i in range(cur):
                    if 0 <= row + dr < N and 0 <= col + dc < M:
                        total += balloons[row+dr][col+dc]
                        dr += drow[d]
                        dc += dcol[d]
                    else:
                        break


            if total > max_total:
                max_total = total


    print(f'#{tc} {max_total}')



