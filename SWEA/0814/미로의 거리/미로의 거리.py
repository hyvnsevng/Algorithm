import sys
from collections import deque

sys.stdin = open('5105_input.txt')

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):
    n = int(input())
    maze = [list(map(int, input())) for _ in range(n)]
    # visited = [[False for _ in range(n)] for _ in range(n)]

    queue = deque()

    for i in range(n):
        for j in range(n):
            if maze[i][j] == 2:
                queue.append([i, j])
                maze[i][j] = 0
            elif maze[i][j] == 3:
                maze[i][j] = -1


    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]

    answer = 0

    while queue:
        v = queue.popleft()

        for i in range(4):
            nr, nc = v[0] + dr[i], v[1] + dc[i]
            if 0 <= nr < n and 0 <= nc < n:
                node = maze[nr][nc]
                if not node:
                    maze[nr][nc] = maze[v[0]][v[1]] + 1
                    queue.append([nr, nc])
                elif node == -1:
                    answer = maze[v[0]][v[1]]
                    break
        if answer:
            break

    print(f'#{tc} {answer}')








