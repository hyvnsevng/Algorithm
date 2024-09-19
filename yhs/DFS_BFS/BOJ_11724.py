from collections import deque


def find(n):
    if visited[n]:
        return 0

    q = deque()
    q.append(n)
    visited[n] = True
    while q:
        v = q.popleft()
        for node in edges[v]:
            if not visited[node]:
                q.append(node)
                visited[node] = True
    return 1


V, E = map(int, input().split())

visited = [False]*(V+1)
edges = [[] for _ in range(V+1)]
for _ in range(E):
    a, b = map(int, input().split())
    edges[a].append(b)
    edges[b].append(a)

answer = 0
for i in range(1, V+1):
    answer += find(i)

print(answer)