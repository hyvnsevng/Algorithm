# import sys
# sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////

    n, m = map(int, input().split())        # 행과 열 수 입력

    balloons = [list(map(int, input().split())) for _ in range(n)]      # 풍선 격자판 생성

    # delta
    drow = [1, 0, -1, 0]
    dcol = [0, 1, 0, -1]

    # 최대값 초기화
    max_total = 0

    # 격자판 순회하기
    for row in range(n):
        for col in range(m):
            # 현재 위치 풍선의 꽃가루 개수
            total = balloons[row][col]

            # delta 이용해 상하좌우의 꽃가루 개수 더하기
            for i in range(4):
                nrow = row + drow[i]
                ncol = col + dcol[i]
                if 0 <= nrow < n and 0 <= ncol < m:     # 인덱스 범위 확인
                    total += balloons[nrow][ncol]

            # 최대값 갱신
            if max_total < total:
                max_total = total

    print(f'#{test_case} {max_total}')

    # ///////////////////////////////////////////////////////////////////////////////////
