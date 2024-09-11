import heapq
INF = 1e9

T = int(input())
for tc in range(1, T+1):
    def dijkstra(start):
        distance = [INF] * (N + 1)
        q = []
        heapq.heappush(q, (0, start))
        distance[start] = 0

        # 시작 ~ X 거리 찾기
        while q:
            dist, now = heapq.heappop(q)
            if dist > distance[now]:
                continue

            for next, cost in graph[now]:
                new_cost = dist + cost
                if new_cost >= distance[next]:
                    continue
                distance[next] = new_cost
                heapq.heappush(q, (new_cost, next))

        return distance


    N, M, X = map(int, input().split())

    graph = [[] for _ in range(N+1)]

    for _ in range(M):
        x, y, c = map(int, input().split())
        graph[x].append((y, c))

    comeback = dijkstra(X)
    max_cost = 0

    for i in range(1, N+1):
        # if i == x:
        #     continue
        tmp = dijkstra(i)
        if tmp[X] + comeback[i] > max_cost:
            max_cost = tmp[X] + comeback[i]

    print(f'#{tc} {max_cost}')