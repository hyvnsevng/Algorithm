# 백준 1162번 도로포장

import heapq


def dijkstra(k):
    INF = 10000*1000000     # 10,000(최대노드개수) * 1,000,000(간선의 최대 가중치)
    distance = [[INF]*(k+1) for _ in range(n+1)]    # distance[x][y] : 1~x번 도시까지 도로를 k-y번 포장해서 갈 때 최소비용
    distance[1] = [0]*(k+1)

    hq = []
    heapq.heappush(hq, (0, k, 1))           # (가중치, 포장 가능 횟수, 노드 번호)

    while hq:
        dist, pave, now = heapq.heappop(hq)
        if distance[now][pave] < dist:      # 이미 처리한 노드인지 확인하기
            continue

        for next, cost in edges[now]:
            new_cost = cost + dist
            if new_cost < distance[next][pave]:                     # 다음 간선을 포장하지 않고 우선순위 큐에 삽입
                distance[next][pave] = new_cost
                heapq.heappush(hq, (new_cost, pave, next))
            if pave > 0 and dist < distance[next][pave-1]:          # 다음 간선을 포장하고 우선순위 큐에 삽입
                distance[next][pave-1] = dist                       # 도로 포장 시 가중치가 0이 되므로 기존의 dist가 누적 가중치가 된다.
                heapq.heappush(hq, (dist, pave-1, next))

    return min(distance[-1])                                        # 0~k번 포장한 최소비용 중 최솟값 반환


n, m, k = map(int, input().split())         # 도시 개수, 도로 개수, 포장할 수 있는 도로 개수

edges = [[] for _ in range(n+1)]
for _ in range(m):
    c1, c2, t = map(int, input().split())
    edges[c1].append([c2, t])
    edges[c2].append([c1, t])

print(dijkstra(k))
