import sys

sys.stdin = open('input1.txt')

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):
    N, M = map(int, input().split())

    dr = [1, 0, -1, 0]
    dc = [0, 1, 0, -1]

    graph = [list(map(int, input().split())) for _ in range(N)]


    ans = 0

    for i in range(N):
        for j in range(M):
            flower = graph[i][j]
            for idx in range(4):
                ni = i+dr[idx]
                nj = j+dc[idx]
                if 0 <= ni < N and 0 <= nj < M:
                    flower += graph[ni][nj]

            if flower > ans:
                ans = flower

    print(f'#{tc} {ans}')