from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]

visited = [[[1e9, 1e9] for _ in range(m)] for _ in range(n)]
dcol, drow = [1, -1, 0, 0], [0, 0, 1, -1]

minDist = 1e9  # row, col, dist

q = deque()
q.append([0, 0, 1, False])  # row, col, dist, isBroken

# visited에 거리를 저장. -> 이전 거리보다 짧으면 걍 궈궈한다.
# 벽 부쉈을 때 방문 처리 어떻게 할까?
# 방문처리를 거리순으로 하면, 만약 벽을 부수고 더 짧은 거리 vs 벽을 안 부수고 더 먼 거리 인데? 지금 벽을 안 부수고 더 먼 거리
# 방문처리: visited 배열에 거리와 벽 부순 여부.
while q:
    # 큐에서 값 꺼내기
    row, col, dist, isBroken = q.popleft()

    # 최단거리 갱신
    if row == n-1 and col == m-1 and dist < minDist:
        minDist = dist

    # 방문처리: 벽 부순 경우
    if isBroken and visited[row][col][1] > dist:
        visited[row][col][1] = dist
    # 방문처리: 벽 안 부순 경우
    elif not isBroken and visited[row][col][0] > dist:
        visited[row][col] = [dist, dist]

    for i in range(4):
        ncol, nrow = col + dcol[i], row + drow[i]
        if 0 <= ncol < m and 0 <= nrow < n:
            # 벽 이미 부순 경우
            if isBroken and not graph[nrow][ncol] and dist + 1 < visited[nrow][ncol][1]:
                q.append([nrow, ncol, dist + 1, True])
                visited[nrow][ncol][1] = dist

            # 벽 아직 안 부순 경우
            elif not isBroken:
                # 부술 경우
                if dist + 1 < visited[nrow][ncol][1] and graph[nrow][ncol]:
                    q.append([nrow, ncol, dist + 1, True])
                    visited[nrow][ncol][1] = dist
                # 안 부술 경우
                elif dist + 1 < visited[nrow][ncol][0] and not graph[nrow][ncol]:
                    q.append([nrow, ncol, dist + 1, False])
                    visited[nrow][ncol] = [dist, dist]


print(-1 if minDist == 1e9 else minDist)