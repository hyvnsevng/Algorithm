import sys

sys.stdin = open('2001_input.txt')

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):
    N, M = map(int, input().split())

    area = [list(map(int, input().split())) for _ in range(N)]

    max_val = 0


    for i in range(N-M+1):
        for j in range(N-M+1):
            total = 0
            for k in range(M):
                for l in range(M):
                    total += area[i+k][j+l]

            if total > max_val:
                max_val=total

    print(f'#{tc} {max_val}')