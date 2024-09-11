import heapq
INF = 1e9


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]:  # 이미 처리되었다면 무시
            continue
        for next, cost in graph[now]:
            new_cost = dist + cost
            if new_cost < distance[next]:
                distance[next] = new_cost
                heapq.heappush(q, (new_cost, next))


# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T + 1):
    n, m = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        s, e, w = map(int, input().split())
        graph[s].append((e, w))

    distance = [INF] * (n+1)

    dijkstra(0)

    print(f'#{tc} {distance[n]}')