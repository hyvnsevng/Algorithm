from collections import deque

v, e = map(int, input().split())
edge_info = list(map(int, input().split()))
adj = [[] for _ in range(v + 1)]
visited = [False for _ in range(v + 1)]

for i in range(e):
    v1 = edge_info[i * 2]
    v2 = edge_info[i * 2 + 1]
    adj[v1].append(v2)
    adj[v2].append(v1)

print(f'#{1} ', end='')
queue = deque([1])
visited[1] = True
while queue:
    vertex = queue.popleft()
    print(vertex, end=' ')
    for nodes in adj[vertex]:
        if not visited[nodes]:
            queue.append(nodes)
            visited[nodes] = True


