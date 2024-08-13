from collections import deque

def bfs(graph):
    queue = deque()
    queue.append([0, 0])
    graph[0][0] = 0

    dr = [1, 0, -1, 0]
    dc = [0, 1, 0, -1]

    result = 1

    while queue:
        for _ in range(len(queue)):
            v = queue.popleft()
            # print(v)
            for i in range(4):
                nrow = v[0] + dr[i]
                ncol = v[1] + dc[i]

                if 0 <= nrow < n and 0<= ncol < m and graph[nrow][ncol]:
                    queue.append([nrow, ncol])
                    graph[nrow][ncol] = 0

                if nrow == n-1 and ncol == m-1:
                   return result + 1

        result += 1


n, m = map(int, input().split())

graph = [list(map(int, input())) for _ in range(n)]

# print(graph)
print(bfs(graph))