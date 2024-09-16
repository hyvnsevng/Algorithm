# 백준 17472번 다리 만들기 2

# 지난번 SW 역테 A형 2번과 같은 문제이다.
# 그 때 당시에는 최소 신장 트리와 같은 최단 경로 알고리즘을 모를 때여서 DFS를 이용해 섬을 확인하는 것까지밖에 구현하지 못했는데, 이제서야 prim 알고리즘을 이용해 풀게 되었다.

# 1. DFS로 각 섬의 좌표 저장
# 2. 반복&조건문 이용하여 각 섬의 간선 중 길이가 2인 것만 저장
# 3. 2의 간선 이용하여 MST의 가중치 합 구하기
# 3-1. 만약 MST 만들 수 없다면(MST 방문 리스트의 모든 요소가 True가 아니라면) -1 반환

from heapq import heappop, heappush


def dfs(row, col):
    if visited[row][col]:
        return

    visited[row][col] = True
    result = []
    result.append([row, col])

    for i in range(4):
        nr, nc = row+dr[i], col+dc[i]
        if 0 <= nr < n and 0 <= nc < m and graph[nr][nc] and not visited[nr][nc]:
            result += dfs(nr, nc)       # result에 섬으로 묶이는 모든 좌표 추가

    return result


def prim():
    MST = [False] * len(islands)
    hq = []
    heappush(hq, (0, 0))    # 0번째 섬부터 시작
    result = 0
    while hq:
        cost, now = heappop(hq)
        if MST[now]:
            continue
        MST[now] = True
        result += cost

        for next, new_cost in edges[now]:
            if not MST[next]:
                heappush(hq, (new_cost, next))

    if sum(MST) == len(islands):    # 모든 섬이 연결됐을 경우 다리 길이의 합 반환
        return result
    else:                           # 아니라면 -1 반환
        return -1


n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]     # 지도 정보
visited = [[False] * m for _ in range(n)]                       # DFS에서의 방문여부 확인용 배열

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

islands = []
for i in range(n):
    for j in range(m):
        if graph[i][j] and not visited[i][j]:       # islands 배열에 섬의 좌표 저장하기
            island = dfs(i, j)
            islands.append(island)

edges = [[] for _ in range(len(islands))]       # 간선 정보

for i in range(len(islands)):
    # 각 섬에 연결된 간선 정보 확인
    island = islands[i]
    edge = set()                # set로 중복 제거하기
    for row, col in island:     # 해당 섬의 모든 좌표에 대하여
        for j in range(4):      # 상하좌우 탐색
            c = 1
            while True:         # 1(땅)을 만날 때 까지
                nr = row + c * dr[j]
                nc = col + c * dc[j]

                if 0 <= nr < n and 0 <= nc < m:     # 인덱스 범위 확인
                    if graph[nr][nc]:               # 탐색한 곳이 땅이라면
                        if c < 3:                   # 다리의 길이가 2 이하인 경우 제외
                            break
                        for k in range(len(islands)):   # 어느 섬과 연결되었는지 확인하기
                            if [nr, nc] in islands[k]:
                                edge.add((k, c-1))  # 간선 정보 업데이트
                                break

                        break

                    c += 1  # 탐색한 곳이 바다라면 다음 칸 탐색
                else:       # 탐색한 곳이 배열 범위 밖이라면 반복 탈출
                    break
    edges[i] = list(edge)   # set -> list로 변환하여 간선정보 업데이트

print(prim())
