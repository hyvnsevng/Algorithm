from collections import deque

def bfs(tomatoes):
    dx = [1, 0, -1, 0]
    dy = [0, -1, 0, 1]

    queue = deque()

    unripe = []

    is_it_already_ripen = 0

    for row in range(m):
        for col in range(n):
            v = tomatoes[row][col]
            if not v:
                unripe.append([row, col])
                is_it_already_ripen += 1
            elif v == 1:
                queue.append([row, col])

    if not is_it_already_ripen:
        return 0

    result = 0
    while queue:
        cycle = len(queue)
        for i in range(cycle):
            v = queue.popleft()
            for j in range(4):
                nx = v[0] + dx[j]
                ny = v[1] + dy[j]
                if 0 <= nx < m and 0 <= ny < n and not tomatoes[nx][ny]:
                    queue.append([nx, ny])
                    tomatoes[nx][ny] = 1

        result += 1

    for i in range(m):
        for j in range(n):
            if not tomatoes[i][j]:
                return -1

    return result-1


n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(m)]

date = bfs(graph)
print(date)