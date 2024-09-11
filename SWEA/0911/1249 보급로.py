from heapq import heappush, heappop

T = int(input())
for tc in range(1, T+1):
    n = int(input())

    graph = [list(map(int, input())) for _ in range(n)]

    # print(graph)
    dr, dc = [1, -1, 0, 0], [0, 0, 1, -1]
    INF = 1E9
    distance = [[INF]*n for _ in range(n)]
    q = []
    heappush(q, (0, [0, 0]))
    distance[0][0] = 0
    while q:
        dist, [row, col] = heappop(q)
        if dist > distance[row][col]:
            continue

        for i in range(4):
            nr, nc = row+dr[i], col+dc[i]
            if 0 <= nr < n and 0 <= nc < n:
                cost = graph[nr][nc] + dist
                if cost < distance[nr][nc]:
                    distance[nr][nc] = cost
                    heappush(q, (cost, [nr, nc]))

    answer = distance[n-1][n-1]

    print(f'#{tc} {answer}')