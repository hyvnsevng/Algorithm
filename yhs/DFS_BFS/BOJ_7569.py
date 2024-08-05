from collections import deque

def bfs(tomatoes):
    queue = deque()

    unripe = []     # 안 익은 토마토 위치

    # delta
    dr = [1, 0, 0, -1, 0, 0]
    dc = [0, 1, 0, 0, -1, 0]
    dh = [0, 0, 1, 0, 0, -1]

    time = 0        # 시간

    # 3차원 행렬 조회 : 안 익은 토마토는 unripe에, 익은 토마토는 queue에 추가
    for height in range(h):
        for row in range(n):
            for col in range(m):
                ripe = tomatoes[height][row][col]
                if not ripe:
                    unripe.append([height, row, col])
                elif ripe == 1:
                    queue.append([height, row, col])

    # queue가 빌 때 까지 반복
    while queue:
        # 현재 큐의 길이(하루)동안
        cycle = len(queue)

        for _ in range(cycle):
            ripe = queue.popleft()

            # 인접노드 탐색
            for i in range(6):
                height = ripe[0] + dh[i]
                row = ripe[1] + dr[i]
                col = ripe[2] + dc[i]

                # 인덱스 범위 내의 토마토가 안 익은 토마토일 경우 큐에 추가 후 익은 것으로 처리
                if 0 <= height < h and 0 <= row < n and 0 <= col < m and not tomatoes[height][row][col]:
                    queue.append([height, row, col])
                    tomatoes[height][row][col] = 1

        # 하루 끝~
        time += 1

    # 처음 저장했던 안 익은 토마토의 위치 조회하여 익었는지 확인
    for location in unripe:
        height, row, col = location
        # 안 익었으면 -1 반환
        if not tomatoes[height][row][col]:
            return -1

    # 위의 while문에서 토마토가 모두 익었어도 마지막 cycle은 돌아간다. 따라서 계산된 time에 -1을 빼서 반환
    return time-1


m, n, h = map(int, input().split())

tomatoes = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]  # 토마토 상자 배열
# tomatoes[h][n][m]

print(bfs(tomatoes))
