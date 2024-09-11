from heapq import heappush, heappop

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    edges = [[] for _ in range(V+1)]
    for _ in range(E):
        a, b, w = map(int, input().split())
        edges[a].append([b, w])
        edges[b].append([a, w])
    # edges = [list(map(int, input().split())) for _ in range(E)]

    def prim(start):
        q = []
        MST = [False] * (V+1)
        sum_w = 0
        heappush(q, (0, start))

        while q:
            weight, now = heappop(q)
            if MST[now]:
                continue
            MST[now] = True
            sum_w += weight

            for next, cost in edges[now]:
                if MST[next]:
                    continue
                heappush(q, (cost, next))

        return sum_w


    answer = prim(0)
    print(f'#{tc} {answer}')