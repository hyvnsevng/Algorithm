from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])      # 큐에 시작지점 추가
    visited[start] = True       # 시작지점 방문처리

    virus = 0                   # n번 컴퓨터를 통해 바이러스에 걸린 컴퓨터의 수

    # 큐에 원소가 남아있는 동안 반복
    while queue:
        # 현재 노드
        v = queue.popleft()

        # 인접 노드 탐색
        for node in graph[v]:
            # 방문 안 한 노드면 큐에 추가하고 방문처리
            if not visited[node]:
                queue.append(node)
                visited[node] = True
                virus += 1      # 바이러스 수 추가

    return virus


n = int(input())        # 컴퓨터의 수
m = int(input())        # 네트워크 연결 수

networks = [list(map(int, input().split())) for _ in range(m)]  # 네트워크
# 인접노드 리스트
graph = [[] for _ in range(n+1)]
for network in networks:
    graph[network[0]].append(network[1])
    graph[network[1]].append(network[0])
visited = [False for _ in range(n+1)]                           # 방문기록
v = 1    # 시작지점

print(bfs(graph, v, visited))