import heapq

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T + 1):
    n = int(input())
    graph = [list(map(int, input().split())) for _ in range(n)]

    MST = [[False]*n for _ in range(n)]         # 방문 확인용
    dr, dc = [1, -1, 0, 0], [0, 0, 1, -1]       # delta 탐색용
    answer = 0

    heap = []
    heapq.heappush(heap, [0, [0, 0]])           # 시작지점 우선순위 큐에 추가

    while heap:
        cost, [row, col] = heapq.heappop(heap)
        if MST[row][col]:                       # 방문한 노드일 경우 무시함
            continue

        if row == n-1 and col == n-1:           # 도착한 경우 값 저장하고 반복 탈출
            answer = cost
            break

        MST[row][col] = True                    # 방문처리

        for i in range(4):                      # 인접노드 탐색
            nr = row + dr[i]
            nc = col + dc[i]
            if 0 <= nr < n and 0 <= nc < n and not MST[nr][nc]:
                if graph[nr][nc] - graph[row][col] > 0:         # 높이 차이만큼 비용 더하기
                    plus = graph[nr][nc] - graph[row][col]
                else:
                    plus = 0
                heapq.heappush(heap, [plus+cost+1, [nr, nc]])

    print(f'#{tc} {answer}')