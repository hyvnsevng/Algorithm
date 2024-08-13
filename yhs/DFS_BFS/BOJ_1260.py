from collections import deque


def dfs(graph, node, visited):
    visited[node] = True        # 노드 방문처리

    print(node, end = ' ')      # 방문한 노드 출력

    # 인접 노드 탐색
    for nodes in graph[node]:
        # 방문 안 한 노드면 다음 인접 노드 방문
        if not visited[nodes]:
            dfs(graph, nodes, visited)      # 다음 노드 재귀적 호출


def bfs(graph, start_point, visited):
    visited[start_point] = True     # 시작 노드 방문처리
    queue = deque()
    queue.append(start_point)       # 큐에 시작노드 넣기

    # 큐에 요소가 있는동안 반복
    while queue:
        node = queue.popleft()      # 큐에서 원소 제거
        print(node, end = ' ')      # 방문한 노드 출력
        for nodes in graph[node]:   # 인접 노드 전부 탐색
            # 방문 안 한 노드면 큐에 추가하고 방문처리
            if not visited[nodes]:
                queue.append(nodes)
                visited[nodes] = True


n, m, v = map(int, input().split())         # 정점, 간선, 시작점

lines = [list(map(int, input().split())) for _ in range(m)]         # 간선 정보

graph = [[] for _ in range(n+1)]            # 인접 노드 배열 생성
for line in lines:
    graph[line[0]].append(line[1])
    graph[line[1]].append(line[0])

# 인접 노드 중 작은 수의 노드부터 탐색하도록 정렬
for nodes in graph:
    nodes.sort()

# 방문노드 초기화
visited_dfs = [False for _ in range(n+1)]
visited_bfs = [False for _ in range(n+1)]

dfs(graph, v, visited_dfs)
print()
bfs(graph, v, visited_bfs)