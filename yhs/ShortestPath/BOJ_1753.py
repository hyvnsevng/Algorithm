# 백준 1753번 최단경로
# 최단경로 알고리즘 (다익스트라, 플로이드-워셜, 벨만-포드 등) 이용해서 풀 수 있음
# 다익스트라 사용할 경우, list 이용하면 시간 초과 발생할 수 있음 -> 시간복잡도 작은 우선순위 큐 이용하여 구현하기

import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

v, e = map(int, input().split())    # 정점, 간선 개수
k = int(input())    # 시작 정점
adj = [[] for _ in range(v+1)]
for i in range(e):
    a, b, c = map(int, input().split())
    adj[a].append([b, c])
dist_info = [INF for _ in range(v+1)]

# q : 우선순위 큐
q = []
heapq.heappush(q, (0, k))   # 시작노드의 거리 0으로 설정하여 q에 삽입
dist_info[k] = 0

while q:
    dist, now = heapq.heappop(q)    # 가장 가까운 거리의 노드

    if dist_info[now] >= dist:      # 확인하지 않은 노드일 경우 (갱신 X)
        for i in adj[now]:          # 현재 노드와 이어진 노드 모두 탐색 ( i[0]: now와 연결된 노드, i[1]: 거리 )
            # print(i)
            cost = dist + i[1]
            if cost < dist_info[i[0]]:   # 지금까지 확인한 거리 중 최단거리보다 작을 경우 갱신 후 우선순위 큐에 추가
                dist_info[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

for i in range(1, v + 1):
    if dist_info[i] == INF:
        print('INF')
    else:
        print(dist_info[i])

