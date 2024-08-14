import sys
from collections import deque

sys.stdin = open('input.txt')

# Testcase 수
T = 10
# Testcase 만큼 반복
for tc in range(1, T+1):
    _ = int(input())
    n = 100                                             # 미로 사이즈
    maze = [list(map(int, input())) for _ in range(n)]  # 미로 행렬

    # delta
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]

    queue = deque()
    queue.append([1, 1])                # 큐에 시작지점 넣기

    is_break = 0                        # 0이면 도착x, 1이면 도착

    while queue:
        v = queue.popleft()             # dequeue
        maze[v[0]][v[1]] = 2            # 방문처리

        # 인접노드 탐색
        for i in range(4):
            nr = v[0] + dr[i]
            nc = v[1] + dc[i]

            if 0 <= nr < n and 0 <= nc < n:     # 인덱스 범위 확인
                node = maze[nr][nc]
                if not node:                    # 길이라면 큐에 추가
                    queue.append([nr, nc])

                elif node == 3:                 # 도착지점이라면 반복 탈출
                    is_break = 1
                    break

        if is_break:
            break

    print(f'#{tc} {is_break}')


