import heapq

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    xs = list(map(int, input().split()))
    ys = list(map(int, input().split()))
    E = float(input())

    def prim(start):
        visited = [False] * n
        q = []
        heapq.heappush(q, (0, start))
        fee = 0
        while q:
            cost, now = heapq.heappop(q)

            if visited[now]:
                continue
            visited[now] = True
            fee += cost
            x_now, y_now = xs[now], ys[now]

            for i in range(n):
                if i == now or visited[i]:
                    continue
                x_next, y_next = xs[i], ys[i]
                new_cost = (x_next-x_now)**2 + (y_next-y_now)**2
                heapq.heappush(q, (new_cost, i))

        return fee


    answer = prim(0)*E

    print(f'#{tc} {answer:.0f}')